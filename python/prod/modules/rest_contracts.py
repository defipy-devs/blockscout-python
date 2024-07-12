from functools import reduce
from typing import List

from blockscout.enums.actions_enum import ActionsEnum as Actions
from blockscout.enums.delimiters_enum import DelimitersEnum as Delimiters
from blockscout.enums.rest_fields_enum import RestFieldsEnum as RestFields
from blockscout.enums.rest_filters_enum import RestFiltersEnum as RestFilters
from blockscout.enums.modules_enum import ModulesEnum as Modules
from blockscout.enums.tags_enum import TagsEnum as Tags


class RESTContracts:

    @staticmethod
    def get_smart_contracts(contract_type: str) -> str:
        url = (
            f"{RestFields.SMART_CONTRACTS}"
            f"?{RestFields.QUERY}"
            f"{contract_type}"
            f"&{RestFilters.SMART_CONTRACT_FILTER}"
        )
        return url

    @staticmethod
    def get_smart_contract_counters() -> str:
        url = (
            f"{RestFields.SMART_CONTRACTS}"
            f"/{RestFields.COUNTERS}"
        )
        return url

    @staticmethod
    def get_smart_contract(address: str) -> str:
        url = (
            f"{RestFields.SMART_CONTRACTS}"
            f"/{address}"
        )
        return url
    
    