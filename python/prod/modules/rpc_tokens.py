from blockscout.enums.actions_enum import ActionsEnum as Actions
from blockscout.enums.rpc_fields_enum import RPCFieldsEnum as RPCFields
from blockscout.enums.rest_fields_enum import RestFieldsEnum as RestFields
from blockscout.enums.modules_enum import ModulesEnum as Modules
from blockscout.enums.tags_enum import TagsEnum as Tags


class RPCTokens:
    
    @staticmethod
    def get_total_supply_by_contract_address(contractaddress: str) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.TOKEN}"
            f"{RPCFields.ACTION}"
            f"{Actions.GET_TOKEN}"
            f"{RPCFields.CONTRACT_ADDRESS}"
            f"{contractaddress}"
        )
        return url


    @staticmethod
    def get_total_holders_by_contract_address(contractaddress: str, page: int, offset: int) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.TOKEN}"
            f"{RPCFields.ACTION}"
            f"{Actions.GET_TOKEN_HOLDERS}"
            f"{RPCFields.CONTRACT_ADDRESS}"
            f"{contractaddress}"
            f"{RPCFields.PAGE}"
            f"{str(page)}"
            f"{RPCFields.OFFSET}"
            f"{str(offset)}"        
        )
        return url