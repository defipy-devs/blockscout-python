from ..explorer.blockscout import Blockscout 
from ..enums.explorers_enum import ExplorersEnum as Explorers
from ..enums.nets_enum import NetsEnum as Net
from ..enums.api_enum import APIEnum as API
from .data_dictionary import DataDict 

from datetime import datetime
import pandas as pd
import time

DEFAULT_N_BLOCKS = 54000
DEFAULT_N_SEGMENTS = 14 
DEFAULT_N_PULLS = 25

class CoinTransfers:

    def __init__(self, net: str = Net.ROLLUX, verbose: bool = False):
        self.net = net
        self.net_rpc = Blockscout(net, API.RPC)  
        self.net_rest = Blockscout(net, API.REST) 
        self.tkn_balances = {} 
        self.verbose = verbose

    def get_tkn_timeseries(self, dict_transfers, ascending = True):

        tkn_symbol_nm = 'SYS'    
        dd_tx = DataDict(dict_transfers)
        dd_tx.filter_dict('tkn_symbol',tkn_symbol_nm)
        dd_tx.sort_dict('timestamp')
        filtered_dict = dd_tx.get_data_dict()

        timestamps = [filtered_dict[ind]['timestamp'] for k, ind in enumerate(filtered_dict)]
        coin_balances = [filtered_dict[ind]['tkn_coin_balance'] for k, ind in enumerate(filtered_dict)]
        dates = [datetime.fromtimestamp(ts) for ts in timestamps]
        return dates, coin_balances    

    def pull_coin_transactions(self, tkn_addr, sort_direction = "desc"):
        tkn_info = self.net_rest.get_address_info(address = tkn_addr)
        last_block_tx = tkn_info['block_number_balance_updated_at']
        delta_blks = DEFAULT_N_SEGMENTS*DEFAULT_N_BLOCKS
        
        c = 0
        coin_txs = {}
        for k in range(DEFAULT_N_PULLS):
            prev_block_tx = last_block_tx - delta_blks
            out = self.net_rpc.get_txs_by_address_paginated(address=tkn_addr, startblock=prev_block_tx, endblock=last_block_tx, 
                                                       page=1, offset=0, sort=sort_direction)
            last_block_tx = prev_block_tx
            if len(out['result']) > 0:
                for res in out['result']:
                    coin_txs[c] = res      
                    time.sleep(0.5)
                    c+=1 
            else:
                pass

        return coin_txs

    def get_coin_dat(self):
        explorer = Explorers(self.net)
        return explorer.get_coin_dat()        

    def pull_coin_balances(self, tkn_addr, coin_txs):

        coin_dat = self.get_coin_dat()
        native_tkn_symbol = coin_dat['coin_symbol']
        native_tkn_name = coin_dat['coin_name']
        native_tkn_decimal = coin_dat['coin_decimal']

        dict_transfers = {}
        dict_tx_state_changes = {}
        
        for k in range(len(coin_txs)):
            tx = coin_txs[k]
            tx_hash = tx['hash']
            try:
                tx_state_changes = self.net_rest.get_state_changes(tx_hash = tx_hash)
                dict_tx_state_changes[k] = tx_state_changes['items']
                dict_transfers[k] = {}
                
                for tx_chng in tx_state_changes['items']:
                    tx_value_chng = abs(int(tx_chng['change']))
                    if(tx_chng['address']['hash'] == tkn_addr and tx_chng['type'] == 'coin'): 
                        transfer_value = abs(int(tx_chng['change']))
                        dict_transfers[k]['blk_num'] = int(tx['blockNumber'])
                        dict_transfers[k]['timestamp'] = int(tx['timeStamp'])
                        dict_transfers[k]['tkn_symbol'] = native_tkn_symbol
                        dict_transfers[k]['tkn_name'] = native_tkn_name
                        dict_transfers[k]['tkn_decimal'] = native_tkn_decimal
                        dict_transfers[k]['tkn_address'] = tx_state_changes['items'][0]['address']['hash']
                        dict_transfers[k]['transfer_value'] = transfer_value
                        dict_transfers[k]['coin_transfer_value'] = transfer_value/(10**native_tkn_decimal)
                        dict_transfers[k]['transfer_in'] = int(tx_chng['balance_after']) > int(tx_chng['balance_before'])
                        dict_transfers[k]['transfer_gas'] = 0
                        dict_transfers[k]['transfer_hash'] = tx['hash']
                        dict_transfers[k]['tkn_balance'] = int(tx_chng['balance_after'])
                        dict_transfers[k]['tkn_coin_balance'] = dict_transfers[k]['tkn_balance']/(10**native_tkn_decimal)         
                time.sleep(0.5)
            except:    
                time.sleep(1)

        return dict_transfers
        