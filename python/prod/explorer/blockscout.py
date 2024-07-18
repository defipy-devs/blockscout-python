import json
from importlib import resources

import requests

import blockscout
from .. import configs
from ..enums.fields_enum import FieldsEnum as Fields
from ..enums.explorers_enum import ExplorersEnum as Explorers
from ..enums.api_enum import APIEnum as API
from ..utils.parsing import ResponseParser as parser

class Blockscout:
    def __new__(cls, net: str = Explorers.ROLLUX, api: str = API.RPC, verbose = False):
        instance = super(Blockscout, cls).__new__(cls)
        
        if(api == API.RPC):
            json_file_nm = f"{net.upper()}-RPC-stable.json"
        elif(api == API.REST):
            json_file_nm = f"{net.upper()}-REST-stable.json"
        
        with resources.path(configs, json_file_nm) as path:
            config_path = str(path)
        return cls.from_config(config_path=config_path, net=net, api=api)

    def __init__(self, verbose):
        self.verbose = verbose 

    @staticmethod
    def __load_config(config_path: str) -> dict:
        with open(config_path, "r") as f:
            return json.load(f)

    @staticmethod
    def __run(func, net: str, api: str):
        
        def wrapper(*args, **kwargs):
            explorer = Explorers().get_explorer(net)
            url = (
                f"{Fields.HTTPS}"
                f"{explorer}"
                f"{api}"
                f"{func(*args, **kwargs)}"
            )
            print(f'url: {url}')
            r = requests.get(url, headers={"User-Agent": ""})
            return parser.parse(r)

        return wrapper    

    @classmethod
    def from_config(cls, config_path: str, net: str, api: str):
        config = cls.__load_config(config_path)
        for func, v in config.items():
            if not func.startswith("_"):  # disabled if _
                attr = getattr(getattr(blockscout, v["module"]), func)
                setattr(cls, func, cls.__run(attr, net, api))
        return cls
