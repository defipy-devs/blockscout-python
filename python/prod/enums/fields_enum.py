from dataclasses import dataclass

@dataclass(frozen=True)
class FieldsEnum:
    PREFIX: str = "https://api-{}.etherscan.io/api?"
    HTTPS: str = "https://"
