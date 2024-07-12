from dataclasses import dataclass

@dataclass(frozen=True)
class RestFiltersEnum:
    TYPE: str = "type=ERC-20%2CERC-721%2CERC-1155"
    SMART_CONTRACT_FILTER: str = "filter=vyper%20%7C%20solidity%20%7C%20yul"