from blockscout.enums.actions_enum import ActionsEnum as Actions
from blockscout.enums.rpc_fields_enum import RPCFieldsEnum as RPCFields
from blockscout.enums.rest_fields_enum import RestFieldsEnum as RestFields
from blockscout.enums.modules_enum import ModulesEnum as Modules
from blockscout.enums.tags_enum import TagsEnum as Tags

class RPCStats:
    
    @staticmethod
    def get_total_token_supply(contractaddress: str) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.STATS}"
            f"{RPCFields.ACTION}"
            f"{Actions.TOKEN_SUPPLY}"
            f"{RPCFields.CONTRACT_ADDRESS}"
            f"{contractaddress}"        
        )
        return url

    @staticmethod
    def get_total_eth_supply(contractaddress: str) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.STATS}"
            f"{RPCFields.ACTION}"
            f"{Actions.ETH_SUPPLY}"
            f"{RPCFields.CONTRACT_ADDRESS}"
            f"{contractaddress}"        
        )
        return url

    @staticmethod
    def get_total_coin_supply(contractaddress: str) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.STATS}"
            f"{RPCFields.ACTION}"
            f"{Actions.COIN_SUPPLY}"
            f"{RPCFields.CONTRACT_ADDRESS}"
            f"{contractaddress}"        
        )
        return url

    @staticmethod
    def get_eth_price(contractaddress: str) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.STATS}"
            f"{RPCFields.ACTION}"
            f"{Actions.ETH_PRICE}"
            f"{RPCFields.CONTRACT_ADDRESS}"
            f"{contractaddress}"        
        )
        return url

    @staticmethod
    def get_coin_price(contractaddress: str) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.STATS}"
            f"{RPCFields.ACTION}"
            f"{Actions.ETH_PRICE}"
            f"{RPCFields.CONTRACT_ADDRESS}"
            f"{contractaddress}"        
        )
        return url
