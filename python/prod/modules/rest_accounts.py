from functools import reduce
from typing import List

from blockscout.enums.actions_enum import ActionsEnum as Actions
from blockscout.enums.delimiters_enum import DelimitersEnum as Delimiters
from blockscout.enums.rest_fields_enum import RestFieldsEnum as RestFields
from blockscout.enums.rest_filters_enum import RestFiltersEnum as RestFilters
from blockscout.enums.modules_enum import ModulesEnum as Modules
from blockscout.enums.tags_enum import TagsEnum as Tags


class RESTAccounts:

    @staticmethod
    def get_addresses() -> str:
        url = (
            f"{RestFields.ADDRESSES}"
        )
        return url

    @staticmethod
    def get_address_info(address: str) -> str:
        url = (
            f"{RestFields.ADDRESSES}"
            f"/{address}"
        )
        return url

    @staticmethod
    def get_address_counters(address: str) -> str:
        url = (
            f"{RestFields.ADDRESSES}"
            f"/{address}"
            f"/{RestFields.COUNTERS}"
        )
        return url

    @staticmethod
    def get_address_transactions(address: str) -> str:
        url = (
            f"{RestFields.ADDRESSES}"
            f"/{address}"
            f"/{RestFields.TX}"
        )
        return url

    @staticmethod
    def get_address_logs(address: str) -> str:
        url = (
            f"{RestFields.ADDRESSES}"
            f"/{address}"
            f"/{RestFields.LOGS}"
        )
        return url

    @staticmethod
    def get_blocks_validated(address: str) -> str:
        url = (
            f"{RestFields.ADDRESSES}"
            f"/{address}"
            f"/{RestFields.BLOCKS_VALIDATED}"
        )
        return url

    @staticmethod
    def get_token_balances(address: str) -> str:
        url = (
            f"{RestFields.ADDRESSES}"
            f"/{address}"
            f"/{RestFields.TOKEN_BALANCES}"
        )
        return url

    @staticmethod
    def get_token_balances_with_filtering(address: str) -> str:
        url = (
            f"{RestFields.ADDRESSES}"
            f"/{address}"
            f"/{RestFields.TOKENS}"
            f"/{Delimiters.QUES}"
            f"/{RestFilters.TYPE}"
        )
        return url

    @staticmethod
    def get_coin_balance_history(address: str) -> str:
        url = (
            f"{RestFields.ADDRESSES}"
            f"/{address}"
            f"/{RestFields.COIN_BALANCE_HISTORY}"
        )
        return url

    @staticmethod
    def get_coin_balance_history_by_day(address: str) -> str:
        url = (
            f"{RestFields.ADDRESSES}"
            f"/{address}"
            f"/{RestFields.COIN_BALANCE_HISTORY_BY_DAY}"
        )
        return url