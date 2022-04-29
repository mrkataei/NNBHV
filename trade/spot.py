"""
    Mr.Kataei 11/12/2021
    update 2/22/2022
"""
from .exchange import BitfinexClient, Nobitex
from datetime import datetime
from strategy.models import UserStrategies
from .models import Trade

symbols_bitfinix = {'BTCUSDT': 'tBTCUST', 'ETHUSDT': 'tETHUST', 'ADAUSDT': 'tADAUST', 'DOGEUSDT': 'tDOGE:UST',
                    'BCHUSDT': 'tBCHN:UST', 'ETCUSDT': 'tETCUST'}  # bitfinex symbols dictionary

symbols_nobitex = {'ETHUSDT': 'ETHUSDT', 'BTCUSDT': 'BTCUSDT', 'BCHUSDT': 'BCHUSDT', 'ETCUSDT': 'ETCUSDT',
                   'DOGEUSDT': 'DOGEUSDT', 'ADAUSDT': 'ADAUSDT'}

exchanges = {'bitfinex': BitfinexClient}


def sub_order(strategy: str, position: str, time_receive_signal):
    # get all users already have this strategy
    orders = UserStrategies.objects.filter(strategy__name__contains=strategy)
    for order in orders:
        exchange = exchanges[order.exchange.name]
        error, result = exchange.order(coin=order.strategy.coin, percent=float(order.trade_percent))
        if error:
            Trade(strategy=strategy, position=position, coin=order.strategy.coin, timeframe=order.strategy.timeframe,
                  status='failed,' + str(result), signal_at=time_receive_signal,).save()

        else:
            Trade(strategy=strategy, position=position, coin=order.strategy.coin, timeframe=order.strategy.timeframe,
                  price=float(result['price']), status=result['status'],
                  signal_at=time_receive_signal, amount=result['amount']).save()

            # update sell amount
