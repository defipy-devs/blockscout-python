from ..explorer.blockscout import Blockscout 
from ..enums.explorers_enum import ExplorersEnum as Explorers
from ..enums.nets_enum import NetsEnum as Net
from ..enums.api_enum import APIEnum as API
from .data_dictionary import DataDict 

from datetime import datetime
import math

MAX_PAGE_NUM = 5

class TokenTransfers:

    def __init__(self, net: str = Net.ROLLUX, max_tkn_pulls : int = None, verbose: bool = False):
        self.net_rpc = Blockscout(net, API.RPC)  
        self.net_rest = Blockscout(net, API.REST) 
        self.max_tkn_pulls = MAX_PAGE_NUM if max_tkn_pulls == None else max_tkn_pulls
        self.tkn_balances = {} 
        self.init_tkn_balances = {} 
        self.verbose = verbose  

    def apply(self, tkn_addr):
        self.init_tkn_balances = self.pull_current_balances(tkn_addr)
        tkn_transfers = self.pull_data(tkn_addr)
        dict_transfers = self.to_dict(tkn_addr, tkn_transfers)
        dd_tx = DataDict(dict_transfers)
        dd_tx.sort_dict('blk_num')
        dict_transfers = dd_tx.get_data_dict()
        self.tkn_balances = self.add_tkn_balances(dict_transfers)
        return self.tkn_balances

    def get_tkn_timeseries(self, dict_transfers, tkn_symbol_nm, ascending = True):

        dd_tx = DataDict(dict_transfers)
        dd_tx.filter_dict('tkn_symbol',tkn_symbol_nm)
        dd_tx.sort_dict('timestamp')
        filtered_dict = dd_tx.get_data_dict()

        assert len(filtered_dict) > 1, 'Blockscout API: INSUFFICIENT TOKEN TRANSFER DATA' 

        tkn_decimal = filtered_dict[0]['tkn_decimal']
        timestamps = [filtered_dict[ind]['timestamp'] for k, ind in enumerate(filtered_dict)]
        coin_balances = [filtered_dict[ind]['tkn_balance']/(10**tkn_decimal) for k, ind in enumerate(filtered_dict)]
        
        dates = [datetime.fromtimestamp(ts) for ts in timestamps]
        return dates, coin_balances

    def get_tkn_balances(self):
        return self.tkn_balances

    def pull_current_balances(self, tkn_addr):
        erc20_tkn_balances = self.net_rest.get_token_balances(address = tkn_addr)

        assert len(erc20_tkn_balances) > 1, 'Blockscout API: INSUFFICIENT TOKEN BALANCE DATA'    
        
        init_tkn_balances = {}
        for tkn in erc20_tkn_balances:
            if(tkn['token']['decimals'] != None):
                contract_address = tkn['token']['address'].lower()
                init_tkn_balances[contract_address] = {} if contract_address not in init_tkn_balances else {}
                init_tkn_balances[contract_address]['tkn_balance'] = int(tkn['value'])
                init_tkn_balances[contract_address]['tkn_name'] = tkn['token']['name']
                init_tkn_balances[contract_address]['tkn_symbol'] = tkn['token']['symbol']
                init_tkn_balances[contract_address]['tkn_decimal'] = int(tkn['token']['decimals']) 

        return init_tkn_balances
        
    def pull_data(self, tkn_addr, sort_direction = "desc"):
        tkn_transfers = []
        page_nm = 1
        pull_tkn_transfers = True
        while(pull_tkn_transfers and page_nm < self.max_tkn_pulls):
            erc20_tkn_transfers = self.net_rpc.get_erc20_token_transfer_events_by_address(address=tkn_addr, page=page_nm, offset=0, sort="desc")
            tkn_transfers.extend(erc20_tkn_transfers['result'])
            pull_tkn_transfers = pull_tkn_transfers if len(erc20_tkn_transfers['result']) > 0 else False
            page_nm+=1

        return tkn_transfers

    def to_dict(self, tkn_addr, tkn_transfers):      
    
        dict_transfers = {}
        n_transfers = len(tkn_transfers)

        assert n_transfers > 1, 'Blockscout API: INSUFFICIENT TOKEN TRANSFER DATA' 
        
        c = 0
        for k in range(n_transfers):
            tx = tkn_transfers[k]
            if('value' in tx):
                dict_transfers[k] = {}
                dict_transfers[k]['blk_num'] = int(tx['blockNumber'])
                dict_transfers[k]['timestamp'] = int(tx['timeStamp'])
                dict_transfers[k]['tkn_symbol'] = tx['tokenSymbol']
                dict_transfers[k]['tkn_name'] = tx['tokenName']
                dict_transfers[k]['tkn_decimal'] = int(tx['tokenDecimal'])
                dict_transfers[k]['tkn_contract_address'] = tx['contractAddress']
                dict_transfers[k]['transfer_value'] = int(tx['value'])
                transfer_value = dict_transfers[k]['transfer_value']
                tkn_decimal = dict_transfers[k]['tkn_decimal']
                dict_transfers[k]['coin_value'] = transfer_value/(10**tkn_decimal)
                dict_transfers[k]['transfer_in'] = tx['to'] == tkn_addr.lower()
                dict_transfers[k]['transfer_gas'] = int(tx['gasUsed'])
                dict_transfers[k]['transfer_hash'] = tx['hash']
                c+=1

        return dict_transfers

    def add_tkn_balances(self, dict_transfers):
        tkn_balances = {}
        n_transfers = len(dict_transfers)

        assert n_transfers > 1, 'Blockscout API: INSUFFICIENT TOKEN TRANSFER DATA' 
        
        for k in range(n_transfers):
            tx = dict_transfers[k]
            tkn_contract_address = tx['tkn_contract_address']
            transfer_value = tx['transfer_value']
            transfer_in = tx['transfer_in']
            if(tkn_contract_address in self.init_tkn_balances):
        
                if tkn_contract_address not in tkn_balances:
                    tkn_balances[tkn_contract_address] = {} 
        
                if('prev_transfer' in tkn_balances[tkn_contract_address]):
                    tkn_balances[tkn_contract_address]['prev_tkn_balance'] = tkn_balances[tkn_contract_address]['tkn_balance']
                    if(tkn_balances[tkn_contract_address]['prev_transfer_direction']):
                        tkn_balances[tkn_contract_address]['tkn_balance'] -= tkn_balances[tkn_contract_address]['prev_transfer']
                    else:    
                        tkn_balances[tkn_contract_address]['tkn_balance'] += tkn_balances[tkn_contract_address]['prev_transfer']
                else:  
                    init_tkn_balance = self.init_tkn_balances[tkn_contract_address]['tkn_balance'] 
                    tkn_balances[tkn_contract_address]['tkn_balance'] = init_tkn_balance if 'tkn_balance' not in tkn_balances[tkn_contract_address] else tkn_balances[tkn_contract_address]['tkn_balance']
                
                tkn_balances[tkn_contract_address]['prev_transfer'] = transfer_value
                tkn_balances[tkn_contract_address]['prev_transfer_direction'] = transfer_in
                dict_transfers[k]['tkn_balance'] = tkn_balances[tkn_contract_address]['tkn_balance']
            else:
                dict_transfers[k]['tkn_balance'] = math.nan

        return dict_transfers




        