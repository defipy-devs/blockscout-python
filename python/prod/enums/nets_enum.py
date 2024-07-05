from dataclasses import dataclass

@dataclass(frozen=True)
class NetsEnum:
    ROLLUX: str = "rollux"
    MAIN: str = "main"
    GOERLI: str = "goerli"