from dataclasses import dataclass
from .nets_enum import NetsEnum

DEFAULT_NET = NetsEnum.ROLLUX

@dataclass(frozen=True)
class ExplorersEnum:
    ROLLUX: str = "explorer.rollux.com/"
    MAIN: str = "eth.blockscout.com/"
    GOERLI: str = "eth-goerli.blockscout.com/"

    def get_explorer(self, net = DEFAULT_NET) -> str:
             
        match net:
            case NetsEnum.ROLLUX:
                select_explorer = self.ROLLUX
            case NetsEnum.MAIN:
                select_explorer = self.MAIN  
            case NetsEnum.GOERLI:
                select_explorer = self.GOERLI 

        return select_explorer 