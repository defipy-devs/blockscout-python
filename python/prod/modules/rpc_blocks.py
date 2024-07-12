from blockscout.enums.actions_enum import ActionsEnum as Actions
from blockscout.enums.rpc_fields_enum import RPCFieldsEnum as RPCFields
from blockscout.enums.rest_fields_enum import RestFieldsEnum as RestFields
from blockscout.enums.modules_enum import ModulesEnum as Modules
from blockscout.enums.tags_enum import TagsEnum as Tags


class RPCBlocks:
    
    @staticmethod
    def get_block_reward_by_block_number(block_no: str) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.BLOCK}"
            f"{RPCFields.ACTION}"
            f"{Actions.GET_BLOCK_REWARD}"
            f"{RPCFields.BLOCKNO}"
            f"{block_no}"
        )
        return url


    @staticmethod
    def get_est_block_countdown_time_by_block_number(block_no: str) -> str:
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.BLOCK}"
            f"{RPCFields.ACTION}"
            f"{Actions.GET_BLOCK_COUNTDOWN}"
            f"{RPCFields.BLOCKNO}"
            f"{block_no}"
        )
        return url


    @staticmethod
    def get_block_number_by_timestamp(timestamp: int, closest: str) -> str:
        # NOTE: Supports UNIX timestamps in seconds
        url = (
            f"{RPCFields.MODULE}"
            f"{Modules.BLOCK}"
            f"{RPCFields.ACTION}"
            f"{Actions.GET_BLOCK_NUMBER_BY_TIME}"
            f"{RPCFields.TIMESTAMP}"
            f"{timestamp}"
            f"{RPCFields.CLOSEST}"
            f"{closest}"
        )
        return url


