from tick_downloader import tick_downloader
from parse_ticks import parse_ticks
from ibapi.contract import Contract

contract = Contract()
contract.symbol = "ZIONL"
contract.secType = "STK"
contract.exchange = "SMART"
contract.currency = "USD"
contract.primaryExchange = "NASDAQ"   

tick_downloader(contract)
parse_ticks(contract.symbol)