from dataclasses import dataclass

@dataclass(frozen=True)
class RestFieldsEnum:
    ADDRESSES: str = "addresses"
