from dataclasses import dataclass

@dataclass(frozen=True)
class RestFieldsEnum:
    QUERY: str = "q="
    ADDRESSES: str = "addresses"
    COUNTERS: str = "counters"
    TX: str = "transactions"
    LOGS: str = "logs"
    BLOCKS_VALIDATED: str = "blocks-validated"
    TOKEN_BALANCES: str = "token-balances"
    TOKENS: str = "tokens"
    TRANSFERS: str = "transfers"
    COUNTERS: str = "counters"
    HOLDERS: str = "holders"
    SMART_CONTRACTS: str = "smart-contracts"
    COIN_BALANCE_HISTORY: str = "coin-balance-history"
    COIN_BALANCE_HISTORY_BY_DAY: str = "coin-balance-history-by-day"
