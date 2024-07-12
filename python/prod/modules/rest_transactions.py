from functools import reduce
from typing import List

from blockscout.enums.actions_enum import ActionsEnum as Actions
from blockscout.enums.rest_fields_enum import RestFieldsEnum as RestFields
from blockscout.enums.rest_filters_enum import RestFiltersEnum as RestFilters
from blockscout.enums.modules_enum import ModulesEnum as Modules
from blockscout.enums.tags_enum import TagsEnum as Tags


class RESTTransactions:

    @staticmethod
    def get_state_changes(tx_hash: str) -> str:
        url = (
            f"{Modules.TRANSACTIONS}"
            f"/{tx_hash}"
            f"/{RestFields.STATE_CHANGES}"
        )
        return url

    @staticmethod
    def get_transaction_logs(tx_hash: str) -> str:
        url = (
            f"{Modules.TRANSACTIONS}"
            f"/{tx_hash}"
            f"/{RestFields.LOGS}"
        )
        return url

    @staticmethod
    def get_internal_transactions(tx_hash: str) -> str:
        url = (
            f"{Modules.TRANSACTIONS}"
            f"/{tx_hash}"
            f"/{RestFields.INTERNAL_TRANSACTIONS}"
        )
        return url

    @staticmethod
    def get_token_hash_transfers(tx_hash: str) -> str:
        url = (
            f"{Modules.TRANSACTIONS}"
            f"/{tx_hash}"
            f"/{RestFields.TOKEN_TRANSFERS}"
            f"?{RestFilters.TYPE}"
        )
        return url

    @staticmethod
    def get_transaction_info(tx_hash: str) -> str:
        url = (
            f"{Modules.TRANSACTIONS}"
            f"/{tx_hash}"
        )
        return url

    @staticmethod
    def get_main_page_transactions() -> str:
        url = (
            f"{Modules.TRANSACTIONS}"
        )
        return url


