from ..explorer.blockscout import Blockscout 
from ..enums.explorers_enum import ExplorersEnum as Explorers
from ..enums.nets_enum import NetsEnum as Net
from ..enums.api_enum import APIEnum as API
from .data_dictionary import DataDict 

from datetime import datetime

class TokenTransfers:

    def __init__(self, net: str = Net.ROLLUX, verbose: bool = False):
        self.net_rpc = Blockscout(net, API.RPC)  
        self.net_rest = Blockscout(net, API.REST) 
        self.tkn_balances = {} 
        self.verbose = verbose  

    def apply(self, tkn_addr):
        tkn_transfers = self.pull_data(tkn_addr)
        dict_transfers = self.to_dict(tkn_addr, tkn_transfers)
        dd_tx = DataDict(dict_transfers)
        dd_tx.sort_dict('blk_num')
        dict_transfers = dd_tx.get_data_dict()
        dict_transfers = self.add_tkn_balances(dict_transfers)
        return dict_transfers

    def get_tkn_timeseries(self, dict_transfers, tkn_symbol_nm, ascending = True):

        dd_tx = DataDict(dict_transfers)
        dd_tx.filter_dict('tkn_symbol',tkn_symbol_nm)
        dd_tx.sort_dict('timestamp')
        filtered_dict = dd_tx.get_data_dict()

        timestamps = [filtered_dict[ind]['timestamp'] for k, ind in enumerate(filtered_dict)]
        coin_balances = [filtered_dict[ind]['tkn_human_balance'] for k, ind in enumerate(filtered_dict)]
        dates = [datetime.fromtimestamp(ts) for ts in timestamps]
        return dates, coin_balances

    def get_tkn_balances(self):
        return self.tkn_balances
        
    def pull_data(self, tkn_addr, sort_direction = "desc"):
        tkn_transfers = []
        page_nm = 1
        pull_tkn_transfers = True
        while(pull_tkn_transfers):
            erc20_tkn_transfers = self.net_rpc.get_erc20_token_transfer_events_by_address(address=tkn_addr, page=page_nm, offset=0, sort=sort_direction)
            tkn_transfers.extend(erc20_tkn_transfers['result'])
            pull_tkn_transfers = pull_tkn_transfers if len(erc20_tkn_transfers['result']) > 0 else False
            page_nm+=1  

        return tkn_transfers

    def to_dict(self, tkn_addr, tkn_transfers):   
        dict_transfers = {}
        n_transfers = len(tkn_transfers)
        c = 0
        for k in range(n_transfers):
            tx = tkn_transfers[k]
            if('value' in tx):
                dict_transfers[c] = {}
                dict_transfers[c]['blk_num'] = int(tx['blockNumber'])
                dict_transfers[c]['timestamp'] = int(tx['timeStamp'])
                dict_transfers[c]['tkn_symbol'] = tx['tokenSymbol']
                dict_transfers[c]['tkn_name'] = tx['tokenName']
                dict_transfers[c]['tkn_decimal'] = int(tx['tokenDecimal'])
                dict_transfers[c]['tkn_address'] = tx['contractAddress']
                dict_transfers[c]['transfer_value'] = int(tx['value'])
                transfer_value = dict_transfers[c]['transfer_value']
                tkn_decimal = dict_transfers[c]['tkn_decimal']            
                dict_transfers[c]['human_transfer_value'] = transfer_value/(10**tkn_decimal)
                dict_transfers[c]['transfer_in'] = tx['to'] == tkn_addr.lower()
                dict_transfers[c]['transfer_gas'] = int(tx['gasUsed'])
                dict_transfers[c]['transfer_hash'] = tx['hash']
                c+=1

        return dict_transfers

    def add_tkn_balances(self, dict_transfers):
        tkn_balances = {}
        N = len(dict_transfers)
        for k in range(N, 0, -1):
            tx = dict_transfers[k-1]
            tkn_symbol = tx['tkn_symbol']
            tkn_decimal = tx['tkn_decimal']
            transfer_value = tx['transfer_value']
            transfer_in = tx['transfer_in']
        
            self.tkn_balances[tkn_symbol] = {} if tkn_symbol not in self.tkn_balances else self.tkn_balances[tkn_symbol]
            self.tkn_balances[tkn_symbol]['tkn_balance'] = 0 if 'tkn_balance' not in self.tkn_balances[tkn_symbol] else self.tkn_balances[tkn_symbol]['tkn_balance']
        
            if(transfer_in):
                self.tkn_balances[tkn_symbol]['tkn_balance'] += transfer_value
            elif self.tkn_balances[tkn_symbol]['tkn_balance'] >= transfer_value:     
                self.tkn_balances[tkn_symbol]['tkn_balance'] -= transfer_value
            else:
                self.tkn_balances[tkn_symbol]['tkn_balance'] = 0
            self.tkn_balances[tkn_symbol]['tkn_decimal'] = tkn_decimal
            
            dict_transfers[k-1]['tkn_balance'] = self.tkn_balances[tkn_symbol]['tkn_balance']
            dict_transfers[k-1]['tkn_human_balance'] = self.tkn_balances[tkn_symbol]['tkn_balance']/(10**tkn_decimal)

        return dict_transfers




        