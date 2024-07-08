# blockscout-python

Python API for [blockscout.com](https://www.blockscout.com/) 

Currently building and testing out on Rollux ...

___

## Endpoints

The following endpoints are provided:

<details><summary>Accounts <a href="https://docs.blockscout.com/for-users/api/rpc-endpoints/account">(source)</a></summary>
<p>

* `get_balance`
* `get_pending_txs_by_address_paginated`
* `get_txs_by_address_paginated`
* `get_erc20_token_transfer_events_by_address`
* `get_erc721_token_transfer_events_by_address`
* `get_erc20_balance_by_contract_address`
* `get_erc20_tokens_by_address`
* `get_account_list_balances`

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
from blockscout import Net
eth = Blockscout(Net.ROLLUX, API.RPC)  # key in quotation marks
```
Then you can call all available methods, e.g.:

``` python
eth.get_balance(address="0xBb8b9456F615545c88528653024E87C6069d1598")

> {'message': 'OK', 'result': '2010991698475838058402243', 'status': '1'}
```

* See [test notebook](https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/tutorials/basic.ipynb) for basic usage

If you found this package helpful, please leave a :star:!

___

 Powered by [Blockscout.com APIs](https://eth.blockscout.com/api-docs).
