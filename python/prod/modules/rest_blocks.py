from functools import reduce
from typing import List

from blockscout.enums.actions_enum import ActionsEnum as Actions
from blockscout.enums.rest_fields_enum import RestFieldsEnum as RestFields
from blockscout.enums.rest_filters_enum import RestFiltersEnum as RestFilters
from blockscout.enums.modules_enum import ModulesEnum as Modules
from blockscout.enums.tags_enum import TagsEnum as Tags


class RESTBlocks:

    @staticmethod
    def get_block_info(block_number: str) -> str:
        url = (
            f"{RestFields.BLOCKS}"
            f"/{block_number}"
        )
        return url    

    @staticmethod
    def get_block_transactions(block_number: str) -> str:
        url = (
            f"{RestFields.BLOCKS}"
            f"/{block_number}"
            f"/{RestFields.TX}"
        )
        return url  

    @staticmethod
    def get_block_withdrawals(block_number: str) -> str:
        url = (
            f"{RestFields.BLOCKS}"
            f"/{block_number}"
            f"/{RestFields.WITHDRAWALS}"
        )
        return url  
        
    @staticmethod
    def get_main_page_blocks() -> str:
        url = (
            f"{RestFields.MAIN_PAGE}"
            f"/{Modules.BLOCKS}"
        )
        return url