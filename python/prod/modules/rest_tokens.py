from functools import reduce
from typing import List

from blockscout.enums.actions_enum import ActionsEnum as Actions
from blockscout.enums.rest_fields_enum import RestFieldsEnum as RestFields
from blockscout.enums.rest_filters_enum import RestFiltersEnum as RestFilters
from blockscout.enums.modules_enum import ModulesEnum as Modules
from blockscout.enums.tags_enum import TagsEnum as Tags


class RESTTokens:

    @staticmethod
    def get_tokens_list(token_name: str) -> str:
        url = (
            f"{RestFields.TOKENS}"
            f"?{RestFields.QUERY}"
            f"{token_name}"
            f"&{RestFilters.TYPE}"
        )
        return url

    @staticmethod
    def get_token_info(address: str) -> str:
        url = (
            f"{RestFields.TOKENS}"
            f"/{address}"
        )
        return url

    @staticmethod
    def get_token_transfers(address: str) -> str:
        url = (
            f"{RestFields.TOKENS}"
            f"/{address}"
            f"/{RestFields.TRANSFERS}"
        )
        return url

    @staticmethod
    def get_token_holders(address: str) -> str:
        url = (
            f"{RestFields.TOKENS}"
            f"/{address}"
            f"/{RestFields.HOLDERS}"
        )
        return url

    @staticmethod
    def get_token_counters(address: str) -> str:
        url = (
            f"{RestFields.TOKENS}"
            f"/{address}"
            f"/{RestFields.COUNTERS}"
        )
        return url