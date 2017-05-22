# 1BrokerWrapper
Python wrapper for the 1Broker.com 2.1 API

This wrapper works for all 1Broker API functions.
BE SURE TO SUPPLY API INFO

EXAMPLE USE Py2.7:

from BrokerWrapper import Functions
API = "your-api-info"

run = Functions()

print run.user_details(API)
print run.user_overview(API)
print run.deposit_address(API)
print run.transaction_log(API)
print run.quota_status(API)
print run.open_orders(API)
print run.create_order(API, "symbol", TRADE_AMOUNT "long", leverage, "market", "stoploss", "takeprofit", REF)
print run.cancel_order(API, "id")
print run.open_positions(API)
print run.position_history(API, limit, "None", "None")
print run.position_edit(API, id, stoploss, takeprofit, False)
print run.position_close(API, 7654)
print run.cancel_close(API, 9876543)
print run.shared_info(API, 1329780)
print run.market_categories(API)
print run.market_list(API, "forex")
print run.market_details(API, "GOLD")
print run.market_prices(API, "GOLD")
print run.market_bars(API, "GOLD", 60, "None", "None", 5)
print run.market_ticks(API, "GOLD", 10)
print run.profile_stats(API, "3456")
print run.profile_trades(API, 3940, 5)
