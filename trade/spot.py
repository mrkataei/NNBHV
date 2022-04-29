"""
    Mr.Kataei 11/12/2021
    update 2/22/2022
"""
from old.Account import BitfinexClient, Nobitex
from old.Inc import functions
from old import datetime

symbols_bitfinix = {'BTCUSDT': 'tBTCUST', 'ETHUSDT': 'tETHUST', 'ADAUSDT': 'tADAUST', 'DOGEUSDT': 'tDOGE:UST',
                    'BCHUSDT': 'tBCHN:UST', 'ETCUSDT': 'tETCUST'}  # bitfinex symbols dictionary
symbols_nobitex = {'ETHUSDT': 'ETHUSDT', 'BTCUSDT': 'BTCUSDT', 'BCHUSDT': 'BCHUSDT', 'ETCUSDT': 'ETCUSDT',
                   'DOGEUSDT': 'DOGEUSDT', 'ADAUSDT': 'ADAUSDT'}
symbols = {  # add others symbol dictionary in here buy exchange id already define in db
    1: symbols_bitfinix,
    3: symbols_nobitex
}


def get_exchange_class(exchange_id: int, public: str, secret: str):
    if exchange_id == 1:
        return True, BitfinexClient(public=public, secret=secret)
    elif exchange_id == 3:
        return True, Nobitex(public=public, secret=secret)
    else:
        return False, ''


def submit_order(coin_id: int, analysis_id: int, time_receive_signal, position: str):
    orders = functions.get_users_submit_order_detail(analysis_id=analysis_id, coin_id=coin_id)
    # get all users already have this strategy by analysis_id and coin_id
    for order in orders:
        client = get_exchange_class(exchange_id=order[3], public=order[1], secret=order[2])
        # fet user exchange account for submit order
        if not client[0]:
            continue  # user use demo account or not valid exchange
        else:
            client = client[1]
        symbol = symbols[order[3]][order[4]]  # symbol for trade
        if position == 'buy' and client is not None:
            error, result = client.buy_market(symbol=symbol, percent=float(order[5]))
            if error:
                functions.set_trade_history(user_setting_id=order[0], coin=order[4], analysis_id=analysis_id,
                                            position='buy', signal_time=time_receive_signal,
                                            status='failed,' + str(result))
            else:
                result['order_submit_time'] = str(datetime.fromtimestamp(result['order_submit_time'] / 1000.0))
                functions.set_trade_history(user_setting_id=order[0], coin=order[4], analysis_id=analysis_id,
                                            position='buy', signal_time=time_receive_signal,
                                            price=float(result['price']),
                                            amount=result['amount'], order_status=result['order_status'],
                                            order_submit_time=result['order_submit_time'],
                                            status=result['status'])
                functions.update_sell_amount(user_setting_id=order[0], analysis_id=analysis_id, coin_id=order[8],
                                             username=order[7], sell_amount=result['amount'])
        elif position == 'sell' and client is not None:
            amount = float(order[6])
            if amount != 0:
                error, result = client.sell_market(symbol=symbol, amount=float(order[6]))
            else:
                error, result = client.sell_market(symbol=symbol)
            if error:
                functions.set_trade_history(user_setting_id=order[0], coin=order[4], analysis_id=analysis_id,
                                            position='sell', signal_time=time_receive_signal,
                                            status='failed,' + str(result))
            else:
                result['order_submit_time'] = str(datetime.fromtimestamp(result['order_submit_time'] / 1000.0))
                functions.set_trade_history(user_setting_id=order[0], coin=order[4], analysis_id=analysis_id,
                                            position='sell', signal_time=time_receive_signal, price=result['price'],
                                            amount=result['amount'], order_status=result['order_status'],
                                            order_submit_time=result['order_submit_time'], status=result['status'])

# test sell/buy for signals
# submit_order(coin_id=2, analysis_id=2, time_receive_signal=datetime.datetime.now(), position='buy')
# orders = functions.get_users_submit_order_detail(analysis_id=2, coin_id=2)
# print(orders)
