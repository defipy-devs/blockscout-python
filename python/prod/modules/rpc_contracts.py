from functools import reduce
from typing import List

from blockscout.enums.actions_enum import ActionsEnum as Actions
from blockscout.enums.rpc_fields_enum import RPCFieldsEnum as RPCFields
from blockscout.enums.rest_fields_enum import RestFieldsEnum as RestFields
from blockscout.enums.modules_enum import ModulesEnum as Modules
from blockscout.enums.tags_enum import TagsEnum as Tags


class RPCContracts:

    @staticmethod
    def get_contract_list() -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.CONTRACT}"
            f"{RPCFields.ACTION}"
            f"{Actions.LIST_CONTRACTS}"
        )
        return url


    @staticmethod
    def get_contract_abi(address: str) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.CONTRACT}"
            f"{RPCFields.ACTION}"
            f"{Actions.GET_ABI}"
            f"{RPCFields.ADDRESS}"
            f"{address}"
        )
        return url


    @staticmethod
    def get_source_code(address: str) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.CONTRACT}"
            f"{RPCFields.ACTION}"
            f"{Actions.GET_SOURCE_CODE}"
            f"{RPCFields.ADDRESS}"
            f"{address}"
        )
        return url

    @staticmethod
    def get_contract_creation(contractaddresses: str) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.CONTRACT}"
            f"{RPCFields.ACTION}"
            f"{Actions.GET_CONTRACT_CREATION}"
            f"{RPCFields.CONTRACT_ADDRESSES}"
            f"{contractaddresses}"
        )
        return url