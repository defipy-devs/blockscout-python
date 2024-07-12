from blockscout.enums.actions_enum import ActionsEnum as Actions
from blockscout.enums.rpc_fields_enum import RPCFieldsEnum as RPCFields
from blockscout.enums.rest_fields_enum import RestFieldsEnum as RestFields
from blockscout.enums.modules_enum import ModulesEnum as Modules
from blockscout.enums.tags_enum import TagsEnum as Tags

class RPCTransactions:
    
    @staticmethod
    def get_tx_info(txhash: str) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.TRANSACTION}"
            f"{RPCFields.ACTION}"
            f"{Actions.GET_TX_INFO}"
            f"{RPCFields.TXHASH}"
            f"{txhash}"
        )
        return url

    @staticmethod
    def get_tx_receipt_status(txhash: str) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.TRANSACTION}"
            f"{RPCFields.ACTION}"
            f"{Actions.GET_TX_RECEIPT_STATUS}"
            f"{RPCFields.TXHASH}"
            f"{txhash}"
        )
        return url


    @staticmethod
    def get_status(txhash: str) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.TRANSACTION}"
            f"{RPCFields.ACTION}"
            f"{Actions.GET_STATUS}"
            f"{RPCFields.TXHASH}"
            f"{txhash}"
        )
        return url

