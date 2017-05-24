#!/usr/bin/python
"""1Broker Wrapper for python written by L8nit3"""

import requests

BASE_URL = "https://1broker.com/api/v2/"

class Functions:
    def user_details(self, API):
	url_data = "user/details.php?token=" + API
	response = requests.get(BASE_URL + url_data).json()
        return response
    def user_overview(self, API):
	url_data = "user/overview.php?token=" + API
	response = requests.get(BASE_URL + url_data).json()
	return response
    def deposit_address(self, API):
        url_data = "user/bitcoin_deposit_address.php?token=" + API
        response = requests.get(BASE_URL + url_data).json()
        return response
    def transaction_log(self, API):
        url_data = "user/transaction_log.php?token=" + API + "&limit=5"
        response = requests.get(BASE_URL + url_data).json()
        return response
    def quota_status(self, API):
        url_data = "user/quota_status.php?token=" + API
        response = requests.get(BASE_URL + url_data).json()
        return response
		
    def open_orders(self, API):
        url_data = "order/open.php?token=" + API
        response = requests.get(BASE_URL + url_data).json()
        return response
    def create_order(self, API, symbol, amount, direction, leverage, tradetype, stoploss, takeprofit, ref):
        url_data1 = "order/create.php?token=" + API + "&symbol=" + symbol + "&margin=" + str(amount)
        url_data2 = "&direction=" + direction + "&leverage=" + str(leverage) + "&order_type=" + tradetype
        url_data3 = "&referral_id=" + str(ref)
        url_data = str(url_data1 + url_data2 + url_data3)
        if stoploss == "" or None:
            pass
        else:
            url_data3 = url_data3 + "&stop_loss=" + stoploss
        if takeprofit == "" or None:
            pass
    	else:
            url_data3 = url_data3 + "&take_profit=" + takeprofit
    	response = requests.get(BASE_URL + url_data).json()
	return response
    def cancel_order(self, API, order_id):
        url_data = "order/cancel.php?token=" + API + "&order_id=" + str(order_id)
        response = requests.get(BASE_URL + url_data).json()
        return response

    def open_positions(self, API):
        url_data = "position/open.php?token=" + API
        response = requests.get(BASE_URL + url_data).json()
        return response
    def position_history(self, API, limit, start, end):
        url_data = "position/history.php?token=" + API
        if limit == "None":
            pass
        else:
            url_data = url_data + "&limit=" + str(limit)
        if start == "None":
            pass
	else:
            url_data = url_data + "&date_start=" + start
        if end == "None":
            pass
	else:
            url_data = url_data + "&date_end=" + end
	response = requests.get(BASE_URL + url_data).json()
	return response
    def position_edit(self, API, id, stoploss, takeprofit, trail):
        url_data = "position/edit.php?token=" + API + "&position_id=" + str(id)
        if stoploss == "None":
            pass
        else:
            url_data = url_data + "&stop_loss=" + stoploss
        if takeprofit == "None":
            pass
        else:
            url_data = url_data + "&take_profit=" + takeprofit
        response = requests.get(BASE_URL + url_data).json()
        return response
    def position_close(self, API, id):
        url_data = "position/close.php?token=" + API + "&position_id=" + str(id)
        response = requests.get(BASE_URL + url_data).json()
        return response
    def cancel_close(self, API, id):
        url_data = "position/close_cancel.php?token=" + API + "&position_id=" + str(id)
        response = requests.get(BASE_URL + url_data).json()
        return response
    def shared_info(self, API, id):
        url_data = "position/shared/get.php?token=" + API + "&position_id=" + str(id)
        response = requests.get(BASE_URL + url_data).json()
        return response

    def market_categories(self, API):
        url_data = "market/categories.php?token=" + API
        response = requests.get(BASE_URL + url_data).json()
        return response
    def market_list(self, API, category):
        url_data = "market/list.php?token=" + API + "&category=" + category
        response = requests.get(BASE_URL + url_data).json()
        return response
    def market_details(self, API, symbol):
        url_data = "market/details.php?token=" + API + "&symbol=" + symbol
        response = requests.get(BASE_URL + url_data).json()
        return response
    def market_prices(self, API, symbol):
        url_data = "market/quotes.php?token=" + API + "&symbols=" + symbol
        response = requests.get(BASE_URL + url_data).json()
        return response
    def market_bars(self, API, symbol, seconds, start, end, limit):
        url_data = "market/bars.php?token=" + API + "&symbol=" + symbol + "&resolution=" + str(seconds)
        if start == "None":
            pass
        else:
            url_data = url_data + "&date_start=" + str(start)
        if end == "None":
            pass
        else:
            url_data = url_data + "&date_end=" + str(end)
        if limit == "None":
            pass
        else:
            url_data = url_data + "&limit=" + str(limit)
        response = requests.get(BASE_URL + url_data).json()
        return response
    def market_ticks(self, API, symbol, limit):
        url_data = "market/ticks.php?token=" + API + "&symbol=" + symbol
        if limit == "None":
            pass
        else:
            url_data = url_data + "&limit=" + str(limit)
        response = requests.get(BASE_URL + url_data).json()
        return response
		
    def profile_stats(self, API, user_id):
        url_data = "social/profile_statistics.php?token=" + API + "&user_id=" + str(user_id)
        response = requests.get(BASE_URL + url_data).json()
        return response
    def profile_trades(self, API, user_id, limit):
        url_data = "social/profile_trades.php?token=" + API + "&user_id=" + str(user_id)
        if limit == "None":
            pass
        else:
            url_data = url_data + "&limit=" + str(limit)
        response = requests.get(BASE_URL + url_data).json()
        return response
