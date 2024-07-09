from blockscout.enums.actions_enum import ActionsEnum as Actions
from blockscout.enums.rpc_fields_enum import RPCFieldsEnum as RPCFields
from blockscout.enums.rest_fields_enum import RestFieldsEnum as RestFields
from blockscout.enums.modules_enum import ModulesEnum as Modules
from blockscout.enums.tags_enum import TagsEnum as Tags



class Stats:
    
    @staticmethod
    def get_total_token_supply() -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.STATS}"
            f"{RPCFields.ACTION}"
            f"{Actions.TOKEN_SUPPLY}"
        )
        return url
