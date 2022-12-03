from tick_downloader import tick_downloader
from parse_ticks import parse_ticks
from ibapi.contract import Contract

contract = Contract()
contract.symbol = "agm prc"
contract.secType = "STK"
contract.exchange = "SMART"
contract.currency = "USD"
contract.primaryExchange = "NASDAQ" 
num_ticks = 1000  

tick_downloader(contract, num_ticks)
parse_ticks(contract.symbol)