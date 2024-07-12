from functools import reduce
from typing import List

from blockscout.enums.actions_enum import ActionsEnum as Actions
from blockscout.enums.rest_fields_enum import RestFieldsEnum as RestFields
from blockscout.enums.rest_filters_enum import RestFiltersEnum as RestFilters
from blockscout.enums.modules_enum import ModulesEnum as Modules
from blockscout.enums.tags_enum import TagsEnum as Tags


class RESTStats:

    @staticmethod
    def get_stats_transactions_chart() -> str:
        url = (
            f"{Modules.STATS}"
            f"/{RestFields.CHARTS}"
            f"/{RestFields.TX}"
        )
        return url

    @staticmethod
    def get_stats_counters() -> str:
        url = (
            f"{Modules.STATS}"
        )
        return url
    