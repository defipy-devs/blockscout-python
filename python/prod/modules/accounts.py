from functools import reduce
from typing import List

from blockscout.enums.actions_enum import ActionsEnum as actions
from blockscout.enums.fields_enum import FieldsEnum as fields
from blockscout.enums.modules_enum import ModulesEnum as modules
from blockscout.enums.tags_enum import TagsEnum as tags


class Accounts:

    @staticmethod
    def get_addresses() -> str:
        url = (
            f"{fields.ADDRESSES}"
        )
        return url

