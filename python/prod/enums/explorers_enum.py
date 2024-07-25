from dataclasses import dataclass
from .nets_enum import NetsEnum

DEFAULT_NET = NetsEnum.ROLLUX

@dataclass(frozen=True)
class ExplorersEnum:
    ROLLUX: str = "explorer.rollux.com/"
    ETH: str = "eth.blockscout.com/"
    ARB: str = "arbitrum.blockscout.com/"
    OP: str = "optimism.blockscout.com/"
    MATIC: str = "polygon.blockscout.com/"
    
    ROLLUX_COIN_DAT = {'coin_symbol': 'SYS', 'coin_name': 'Syscoin', 'coin_decimal': 18}
    ETH_COIN_DAT = {'coin_symbol': 'ETH', 'coin_name': 'Ethereum', 'coin_decimal': 18}
    ARB_COIN_DAT = {'coin_symbol': 'ARB', 'coin_name': 'Arbitrum', 'coin_decimal': 18}
    OP_COIN_DAT = {'coin_symbol': 'OP', 'coin_name': 'Optimism', 'coin_decimal': 18}
    MATIC_COIN_DAT = {'coin_symbol': 'MATIC', 'coin_name': 'Polygon', 'coin_decimal': 18}

    def get_explorer(self, net = DEFAULT_NET) -> str:
             
        match net:
            case NetsEnum.ROLLUX:
                select_explorer = self.ROLLUX
            case NetsEnum.ETH:
                select_explorer = self.ETH  
            case NetsEnum.ARB:
                select_explorer = self.ARB 
            case NetsEnum.OP:
                select_explorer = self.OP 
            case NetsEnum.MATIC:
                select_explorer = self.MATIC                 

        return select_explorer 


    def get_coin_dat(self, net = DEFAULT_NET) -> str:
             
        match net:
            case NetsEnum.ROLLUX:
                select_coin_dat = self.ROLLUX_COIN_DAT
            case NetsEnum.ETH:
                select_coin_dat = self.ETH_COIN_DAT  
            case NetsEnum.ARB:
                select_coin_dat = self.ARB_COIN_DAT 
            case NetsEnum.OP:
                select_coin_dat = self.OP_COIN_DAT 
            case NetsEnum.MATIC:
                select_coin_dat = self.MATIC_COIN_DAT                 

        return select_coin_dat 