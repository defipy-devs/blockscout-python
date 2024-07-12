# blockscout-python

Python API for [blockscout.com](https://www.blockscout.com/); currently tested on Rollux

___

## REST Endpoints

The following REST endpoints are provided:

<details><summary>Accounts <a href="https://docs.blockscout.com/for-users/api/rpc-endpoints/account">(source)</a>
<a href="https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/tutorials/rest_account.ipynb">(test notebook)</a>
</summary>
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

<details><summary>Block <a href="https://docs.blockscout.com/for-users/api/rpc-endpoints/block">(source)</a></summary>
<p>

* `get_block_reward_by_block_number`
* `get_est_block_countdown_time_by_block_number`
* `get_block_number_by_timestamp`

</details>

<details><summary>Contract <a href="https://docs.blockscout.com/for-users/api/rpc-endpoints/contract">(source)</a></summary>
<p>

* `get_contract_list`
* `get_contract_abi`
* `get_source_code`
* `get_contract_creation`

</details>

<details><summary>Stats <a href="https://docs.blockscout.com/for-users/api/rpc-endpoints/stats">(source)</a></summary>
<p>

* `get_total_token_supply`
* `get_total_eth_supply`
* `get_total_coin_supply`
* `get_eth_price`
* `get_coin_price`

</details>

<details><summary>Tokens <a href="https://docs.blockscout.com/for-users/api/rpc-endpoints/token">(source)</a></summary>
<p>

* `get_total_supply_by_contract_address`
* `get_total_holders_by_contract_address`
* `get_tx_info`
* `get_tx_receipt_status`
* `get_status`

</details>

## RPC Endpoints

The following RPC endpoints are provided:

<details><summary>Accounts <a href="https://docs.blockscout.com/for-users/api/rpc-endpoints/account">(source)</a>
<a href="https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/tutorials/rpc_account.ipynb">(test notebook)</a>
</summary>
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

<details><summary>Block <a href="https://docs.blockscout.com/for-users/api/rpc-endpoints/block">(source)</a></summary>
<p>

* `get_block_reward_by_block_number`
* `get_est_block_countdown_time_by_block_number`
* `get_block_number_by_timestamp`

</details>

<details><summary>Contract <a href="https://docs.blockscout.com/for-users/api/rpc-endpoints/contract">(source)</a></summary>
<p>

* `get_contract_list`
* `get_contract_abi`
* `get_source_code`
* `get_contract_creation`

</details>

<details><summary>Stats <a href="https://docs.blockscout.com/for-users/api/rpc-endpoints/stats">(source)</a></summary>
<p>

* `get_total_token_supply`
* `get_total_eth_supply`
* `get_total_coin_supply`
* `get_eth_price`
* `get_coin_price`

</details>

<details><summary>Tokens <a href="https://docs.blockscout.com/for-users/api/rpc-endpoints/token">(source)</a></summary>
<p>

* `get_total_supply_by_contract_address`
* `get_total_holders_by_contract_address`
* `get_tx_info`
* `get_tx_receipt_status`
* `get_status`

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

If you found this package helpful, please leave a :star:!

___

 Powered by [Blockscout.com APIs](https://eth.blockscout.com/api-docs).
