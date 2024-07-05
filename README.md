# blockscout-python

Python API for [blockscout.com](https://www.blockscout.com/) 

Currently building and testing out on Rollux ...

___

## Endpoints

The following endpoints are provided:

<details><summary>Accounts <a href="https://eth.blockscout.com/api-docs">(source)</a></summary>
<p>

* `get_addresses`

</details>

## Installation

Install from source:

``` bash
pip install git+https://github.com/defipy-devs/blockscout-python.git
```

Alternatively, install from [PyPI](https://pypi.org/project/etherscan-python/):

```bash
pip install blockscout-python
```

## Usage

``` python
from blockscout import Blockscout
eth = Blockscout(Net.ROLLUX) # key in quotation marks
```
Then you can call all available methods, e.g.:

``` python
eth.get_addresses()

> {'exchange_rate': None,
 'items': [{'coin_balance': '3562345790348679629254255',
   'tx_count': '0',
   'ens_domain_name': None,
   'hash': '0x4200000000000000000000000000000000000016',
   'implementation_name': 'L2ToL1MessagePasser',
   'is_contract': True,
   'is_verified': True,
   'metadata': None,
   'name': 'Proxy',
   'private_tags': [],
   'public_tags': [],
   'watchlist_names': []}, ... }
```

* See [test notebook](https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/tutorials/basic.ipynb) for basic usage

If you found this package helpful, please leave a :star:!

___

 Powered by [Blockscout.com APIs](https://eth.blockscout.com/api-docs).
