from functools import reduce
from typing import List

from blockscout.enums.actions_enum import ActionsEnum as Actions
from blockscout.enums.rpc_fields_enum import RPCFieldsEnum as RPCFields
from blockscout.enums.rest_fields_enum import RestFieldsEnum as RestFields
from blockscout.enums.modules_enum import ModulesEnum as Modules
from blockscout.enums.tags_enum import TagsEnum as Tags


class RPCAccounts:

    @staticmethod
    def get_balance(address: str) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.ACCOUNT}"
            f"{RPCFields.ACTION}"
            f"{Actions.BALANCE}"            
            f"{RPCFields.ADDRESS}"
            f"{address}"
        )
        return url

    @staticmethod
    def get_balance_multiple(addresses: List[str]) -> str:
        address_list = reduce(lambda w1, w2: str(w1) + "," + str(w2), addresses)
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.ACCOUNT}"
            f"{RPCFields.ACTION}"
            f"{actions.BALANCE_MULTI}"
            f"{RPCFields.ADDRESS}"
            f"{address_list}"
            f"{RPCFields.TAG}"
            f"{Tags.LATEST}"
        )
        return url

    @staticmethod
    def get_pending_txs_by_address_paginated(
        address: str, page: int, offset: int) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.ACCOUNT}"
            f"{RPCFields.ACTION}"
            f"{Actions.PENDING_TX_LIST}"
            f"{RPCFields.ADDRESS}"
            f"{address}"
            f"{RPCFields.PAGE}"
            f"{str(page)}"
            f"{RPCFields.OFFSET}"
            f"{str(offset)}"
        )
        return url

    @staticmethod
    def get_txs_by_address_paginated(
        address: str, startblock: int, endblock: int, page: int, offset: int, sort: str) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.ACCOUNT}"
            f"{RPCFields.ACTION}"
            f"{Actions.TX_LIST}"
            f"{RPCFields.ADDRESS}"
            f"{address}"
            f"{RPCFields.START_BLOCK}"
            f"{startblock}"
            f"{RPCFields.END_BLOCK}"
            f"{endblock}"
            f"{RPCFields.PAGE}"
            f"{str(page)}"
            f"{RPCFields.OFFSET}"
            f"{str(offset)}"
            f"{RPCFields.SORT}"
            f"{str(sort)}"
        )
        return url

    @staticmethod
    def get_erc20_token_transfer_events_by_address(
        address: str,  page: int, offset: int, sort: str,
    ) -> str:
        # NOTE: Returns the last 10k events
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.ACCOUNT}"
            f"{RPCFields.ACTION}"
            f"{Actions.TOKEN_TX}"
            f"{RPCFields.ADDRESS}"
            f"{address}"
            f"{RPCFields.PAGE}"
            f"{str(page)}"
            f"{RPCFields.OFFSET}"
            f"{str(offset)}"
            f"{RPCFields.SORT}"
            f"{sort}"
        )
        return url

    @staticmethod
    def get_erc721_token_transfer_events_by_address(
        address: str,  page: int, offset: int, sort: str,
    ) -> str:
        # NOTE: Returns the last 10k events
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.ACCOUNT}"
            f"{RPCFields.ACTION}"
            f"{Actions.TOKEN_NFT_TX}"
            f"{RPCFields.ADDRESS}"
            f"{address}"
            f"{RPCFields.PAGE}"
            f"{str(page)}"
            f"{RPCFields.OFFSET}"
            f"{str(offset)}"
            f"{RPCFields.SORT}"
            f"{sort}"
        )
        return url


    @staticmethod
    def get_erc20_balance_by_contract_address(
        contractaddress: str, address: str, 
    ) -> str:

        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.ACCOUNT}"
            f"{RPCFields.ACTION}"
            f"{Actions.TOKEN_BALANCE}"
            f"{RPCFields.CONTRACT_ADDRESS}"
            f"{contractaddress}"
            f"{RPCFields.ADDRESS}"
            f"{address}"
        )
        return url

    @staticmethod
    def get_erc20_tokens_by_address(
        address: str 
    ) -> str:

        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.ACCOUNT}"
            f"{RPCFields.ACTION}"
            f"{Actions.TOKEN_LIST}"
            f"{RPCFields.ADDRESS}"
            f"{address}"
        )
        return url

    @staticmethod
    def get_account_list_balances(
        address: str, page: int, offset: int
    ) -> str:

        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.ACCOUNT}"
            f"{RPCFields.ACTION}"
            f"{Actions.LIST_ACCOUNTS}"
            f"{RPCFields.ADDRESS}"
            f"{address}"
        )
        return url

