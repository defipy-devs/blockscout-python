from datetime import datetime
import pandas as pd

class DataDict:

    def __init__(self, data_dict):
        self.__data_dict = data_dict

    def get_data_dict(self):
        return self.__data_dict

    def filter_dict(self, col_nm, value):
        self.__data_dict = {k:v for k,v in self.__data_dict.items() if col_nm in v and v[col_nm] == value}
        
    def sort_dict(self, col_nm, ascending = False):
        self.__data_dict = dict(sorted(self.__data_dict.items(), key=lambda item: item[1][col_nm], reverse= (not ascending)))
        
        dict_transfers_reindex = {}
        for k, old_k in enumerate(self.__data_dict):
            dict_transfers_reindex[k] = self.__data_dict[old_k]
        self.__data_dict = dict_transfers_reindex

    def to_dataframe(self, dict_transfers):
        return pd.DataFrame.from_dict(dict_transfers, orient='index') 

