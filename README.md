# 1BrokerWrapper
Python wrapper for the 1Broker.com 2.1 API

This wrapper works for all 1Broker API functions.  
BE SURE TO SUPPLY API INFO

### Example use Py2.7 
  
from BrokerWrapper import Functions  
API = "your-api-info"  
run = Functions()  
  
### Possible arguments  
API = Your 1Broker API key  
ID = Position id or Order id  
TRADE_TYPE = market buy or limit trade  
SYMBOL = What you are trading (eg. GOLD)  
DIRECTION = Whether your trading (eg. LONG)  
TRADE_AMOUNT = Amount of BTC per trade (eg. 0.01)  
LEVERAGE = Amount trade is leveraged by (eg. 10)  
STOPLOSS = When to stop trade to save money  
TAKEPROFIT = When to stop trade to protect profits  
REF = Referral id  
LIMIT = Max number of responses  
TRAIL = Set a trailing stop or not (eg. True)  
START = Date to start responses from  
END = Date to stop responses at  
SECONDS = Chart timeframe (eg. 60, 300, 600)  
USER_ID = User to check trades  

### Possible choices  
run.user_details(API)  
run.user_overview(API)  
run.deposit_address(API)  
run.transaction_log(API)  
run.quota_status(API)  
run.open_orders(API)  
run.create_order(API, SYMBOL, TRADE_AMOUNT, DIRECTION, LEVERAGE, TRADE_TYPE, STOPLOSS, TAKEPROFIT, REF)  
run.cancel_order(API, ID)  
run.open_positions(API)  
run.position_history(API, LIMIT, START, END)  
run.position_edit(API, ID, STOPLOSS, TAKEPROFIT, TRAIL)  
run.position_close(API, ID)  
run.cancel_close(API, ID)  
run.shared_info(API, ID)  
run.market_categories(API)  
run.market_list(API, MARKET_TYPE)  
run.market_details(API, SYMBOL)  
run.market_prices(API, SYMBOL)  
run.market_bars(API, SYMBOL, SECONDS, START, END, LIMIT)  
run.market_ticks(API, SYMBOL, LIMIT)  
run.profile_stats(API, USER_ID)  
run.profile_trades(API, USER_ID, LIMIT)  

