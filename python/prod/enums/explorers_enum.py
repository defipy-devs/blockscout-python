from dataclasses import dataclass
from .nets_enum import NetsEnum

DEFAULT_NET = NetsEnum.ROLLUX

@dataclass(frozen=True)
class ExplorersEnum:
    ROLLUX: str = "explorer.rollux.com/"
    MAIN: str = "eth.blockscout.com/"
    GOERLI: str = "eth-goerli.blockscout.com/"
    
    ROLLUX_COIN_DAT = {'coin_symbol': 'SYS', 'coin_name': 'Syscoin', 'coin_decimal': 18}
    MAIN_COIN_DAT = {'coin_symbol': 'ETH', 'coin_name': 'Ethereum', 'coin_decimal': 18}
    GOERLI_COIN_DAT = {'coin_symbol': 'ETH', 'coin_name': 'Ethereum', 'coin_decimal': 18}

    def get_explorer(self, net = DEFAULT_NET) -> str:
             
        match net:
            case NetsEnum.ROLLUX:
                select_explorer = self.ROLLUX
            case NetsEnum.MAIN:
                select_explorer = self.MAIN  
            case NetsEnum.GOERLI:
                select_explorer = self.GOERLI 

        return select_explorer 


    def get_coin_dat(self, net = DEFAULT_NET) -> str:
             
        match net:
            case NetsEnum.ROLLUX:
                select_coin_dat = self.ROLLUX_COIN_DAT
            case NetsEnum.MAIN:
                select_coin_dat = self.MAIN_COIN_DAT  
            case NetsEnum.GOERLI:
                select_coin_dat = self.GOERLI_COIN_DAT 

        return select_coin_dat 