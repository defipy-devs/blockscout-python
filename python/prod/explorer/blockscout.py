import json
from importlib import resources

import requests

import blockscout
from .. import configs
from ..enums.fields_enum import FieldsEnum as fields
from ..enums.explorers_enum import ExplorersEnum as Explorers
from ..utils.parsing import ResponseParser as parser

class Blockscout:
    def __new__(cls, net: str = "main"):
        with resources.path(configs, f"{net.upper()}-stable.json") as path:
            config_path = str(path)
        return cls.from_config(config_path=config_path, net=net)

    @staticmethod
    def __load_config(config_path: str) -> dict:
        with open(config_path, "r") as f:
            return json.load(f)

    @staticmethod
    def __run(func, net: str):
        
        def wrapper(*args, **kwargs):
            explorer = Explorers().get_explorer(net)
            url = (
                f"{fields.HTTPS}"
                f"{explorer}"
                f"{func(*args, **kwargs)}"
            )
            print(f'url: {url}')
            r = requests.get(url, headers={"User-Agent": ""})
            return parser.parse(r)

        return wrapper    

    @classmethod
    def from_config(cls, config_path: str, net: str):
        print(config_path)
        config = cls.__load_config(config_path)
        for func, v in config.items():
            if not func.startswith("_"):  # disabled if _
                attr = getattr(getattr(blockscout, v["module"]), func)
                setattr(cls, func, cls.__run(attr, net))
        return cls
