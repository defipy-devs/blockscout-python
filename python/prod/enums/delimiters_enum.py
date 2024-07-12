from dataclasses import dataclass


@dataclass(frozen=True)
class DelimitersEnum:
    QUES: str = "?"
    AND: str = "&"