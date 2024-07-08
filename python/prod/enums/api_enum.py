from dataclasses import dataclass

@dataclass(frozen=True)
class APIEnum:

    REST: str = "api/v2/"
    RPC: str = "api?"