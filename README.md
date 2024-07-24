# blockscout-python

Python API for [blockscout.com](https://www.blockscout.com/) as currently tested on:
* [Rollux](https://explorer.rollux.com/)

___

## REST Endpoints

The following REST endpoints are provided:

<details><summary>Accounts <a href="https://eth.blockscout.com/api-docs">(source)</a>
<a href="https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/test/rest_account.ipynb">(test notebook)</a>
</summary>
<p>

* `get_addresses`
* `get_address_info`
* `get_address_counters`
* `get_address_transactions`
* `get_address_logs`
* `get_blocks_validated`
* `get_token_balances`
* `get_token_balances_with_filtering`
* `get_coin_balance_history`
* `get_coin_balance_history_by_day`

</details>

<details><summary>Block <a href="https://eth.blockscout.com/api-docs">(source)</a>
<a href="https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/test/rest_blocks.ipynb">(test notebook)</a>
</summary>
<p>

* `get_block_info`
* `get_block_transactions`
* `get_block_withdrawals`
* `get_main_page_blocks`

</details>

<details><summary>Contract <a href="https://eth.blockscout.com/api-docs">(source)</a>
<a href="https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/test/rest_contracts.ipynb">(test notebook)</a>
</summary>
<p>

* `get_smart_contracts`
* `get_smart_contract_counters`
* `get_smart_contract`

</details>

<details><summary>Stats <a href="https://eth.blockscout.com/api-docs">(source)</a>
<a href="https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/test/rest_stats.ipynb">(test notebook)</a>
</summary>
<p>

* `get_stats_transactions_chart`
* `get_stats_counters`

</details>

<details><summary>Tokens <a href="https://eth.blockscout.com/api-docs">(source)</a>
<a href="https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/test/rest_tokens.ipynb">(test notebook)</a>
</summary>
<p>

* `get_tokens_list`
* `get_token_info`
* `get_token_transfers`
* `get_token_holders`
* `get_token_counters`

</details>

<details><summary>Transactions <a href="https://eth.blockscout.com/api-docs">(source)</a>
<a href="https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/test/rest_transactions.ipynb">(test notebook)</a>
</summary>
<p>

* `get_state_changes`
* `get_transaction_logs`
* `get_internal_transactions`
* `get_token_hash_transfers`
* `get_transaction_info`
* `get_main_page_transactions`

</details>

## RPC Endpoints

The following RPC endpoints are provided:

<details><summary>Accounts <a href="https://docs.blockscout.com/for-users/api/rpc-endpoints/account">(source)</a>
<a href="https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/test/rpc_account.ipynb">(test notebook)</a>
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

<details><summary>Block <a href="https://docs.blockscout.com/for-users/api/rpc-endpoints/block">(source)</a>
<a href="https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/test/rpc_block.ipynb">(test notebook)</a>
</summary>
<p>

* `get_block_reward_by_block_number`
* `get_est_block_countdown_time_by_block_number`
* `get_block_number_by_timestamp`

</details>

<details><summary>Contract <a href="https://docs.blockscout.com/for-users/api/rpc-endpoints/contract">(source)</a>
<a href="https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/test/rpc_contracts.ipynb">(test notebook)</a>
</summary>
<p>

* `get_contract_list`
* `get_contract_abi`
* `get_source_code`
* `get_contract_creation`

</details>

<details><summary>Stats <a href="https://docs.blockscout.com/for-users/api/rpc-endpoints/stats">(source)</a>
<a href="https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/test/rpc_stats.ipynb">(test notebook)</a>
</summary>
<p>

* `get_total_token_supply`
* `get_total_eth_supply`
* `get_total_coin_supply`
* `get_eth_price`
* `get_coin_price`

</details>

<details><summary>Tokens <a href="https://docs.blockscout.com/for-users/api/rpc-endpoints/token">(source)</a>
<a href="https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/test/rpc_tokens.ipynb">(test notebook)</a>
</summary>
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

## Basic Usage

``` python
from blockscout import Blockscout
from blockscout import Net
eth = Blockscout(Net.ROLLUX, API.RPC)  
```
Then you can call all available methods, e.g.:

``` python
eth.get_balance(address="0xBb8b9456F615545c88528653024E87C6069d1598")

> {'message': 'OK', 'result': '2010991698475838058402243', 'status': '1'}
```

## Token Transfers: Time Series 

* See [test notebook](https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/cull/address_tkn_transfers.ipynb) 
for example

Pull data for specified address
```
from blockscout import TokenTransfers
from blockscout import Net

addr = '0x8A4AA176007196D48d39C89402d3753c39AE64c1'
tkn_trans = TokenTransfers(Net.ROLLUX)
dict_transfers = tkn_trans.apply(addr)
tkn_balances = tkn_trans.get_tkn_balances()
tkn_balances
```

#### OUTPUT:
{'USDT': {'tkn_balance': 89590009236, 'tkn_decimal': 6}, <br/>
 'USDC': {'tkn_balance': 238003477125, 'tkn_decimal': 6}, <br/>
 'ETH': {'tkn_balance': 2689089808644384766235, 'tkn_decimal': 18}, <br/>
 'BTC': {'tkn_balance': 999799972, 'tkn_decimal': 8}, <br/>
 'WSYS': {'tkn_balance': 65787771636449164370510, 'tkn_decimal': 18}} <br/><br/> 

Plot token transfers
```
import matplotlib.pyplot as plt

tkn_symbol = 'USDC' 
dates, tkn_coin_balances = tkn_trans.get_tkn_timeseries(dict_transfers, tkn_symbol)
fig, (TKN_ax) = plt.subplots(nrows=1, sharex=False, sharey=False, figsize=(16, 3))
TKN_ax.plot(dates, tkn_coin_balances, color = 'r',linestyle = 'dashdot', label=tkn_symbol) 
TKN_ax.set_ylabel(f'{tkn_symbol} Balance', size=14)
TKN_ax.set_xlabel('Date', size=14)
```

![plot](./docs/img/addr_tkn_balances.jpg)

## Coin Transfers: Time Series 

* See [test notebook](https://github.com/defipy-devs/blockscout-python/blob/main/notebooks/cull/address_coin_transfers.ipynb) 
for example

Pull data for specified address
```
from blockscout import CoinTransfers
from blockscout import Net

addr = '0x8A4AA176007196D48d39C89402d3753c39AE64c1'
coin_trans = CoinTransfers(Net.ROLLUX)
txs = coin_trans.pull_coin_transactions(addr)
coin_tx = coin_trans.pull_coin_balances(addr, txs)
```

Plot token transfers
```
import matplotlib.pyplot as plt

tkn_symbol = 'SYS' 
dates, tkn_coin_balances = coin_trans.get_tkn_timeseries(coin_tx)
fig, (TKN_ax) = plt.subplots(nrows=1, sharex=False, sharey=False, figsize=(16, 3))
TKN_ax.plot(dates, tkn_coin_balances, color = 'r',linestyle = 'dashdot', label=tkn_symbol) 
TKN_ax.set_ylabel(f'{tkn_symbol} Balance', size=14)
TKN_ax.set_xlabel('Date', size=14)
```

![plot](./docs/img/addr_coin_balances.jpg)

If you found this package helpful, please leave a :star:!

___

 Powered by [Blockscout.com APIs](https://eth.blockscout.com/api-docs).
