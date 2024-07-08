from functools import reduce
from typing import List

from blockscout.enums.actions_enum import ActionsEnum as actions
from blockscout.enums.rpc_fields_enum import RPCFieldsEnum as rpc_fields
from blockscout.enums.rest_fields_enum import RestFieldsEnum as rest_fields
from blockscout.enums.modules_enum import ModulesEnum as modules
from blockscout.enums.tags_enum import TagsEnum as tags


class Accounts:

    @staticmethod
    def get_addresses() -> str:
        url = (
            f"{rest_fields.ADDRESSES}"
        )
        return url

    @staticmethod
    def get_address_balance() -> str:
        url = (
            f"{modules.ACCOUNT}"
            f"{rpc_fields.ACTION}"
            f"{rpc_fields.ADDRESS}"
        )
        return url