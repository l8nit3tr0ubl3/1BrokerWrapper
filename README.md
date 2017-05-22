# 1BrokerWrapper
Python wrapper for the 1Broker.com 2.1 API

This wrapper works for all 1Broker API functions.
BE SURE TO SUPPLY API INFO

EXAMPLE USE Py2.7:

`from BrokerWrapper import Functions

API = "your-api-info"

run = Functions()

print run.user_details(API)

print run.user_overview(API)

print run.deposit_address(API)

print run.transaction_log(API)

print run.quota_status(API)

print run.open_orders(API)

print run.create_order(API, symbol, TRADE_AMOUNT, direction, leverage, trade_type, stoploss, takeprofit, REF)

print run.cancel_order(API, id)

print run.open_positions(API)

print run.position_history(API, limit, start, end)

print run.position_edit(API, id, stoploss, takeprofit, False)

print run.position_close(API, id)

print run.cancel_close(API, id)

print run.shared_info(API, id)

print run.market_categories(API)

print run.market_list(API, market_type)

print run.market_details(API, symbol)

print run.market_prices(API, symbol)

print run.market_bars(API, symbol, seconds, start, end, limit)

print run.market_ticks(API, symbol, limit)

print run.profile_stats(API, user_id)

print run.profile_trades(API, user_id, limit)`
