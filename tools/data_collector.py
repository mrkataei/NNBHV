"""
Mr.Kataei 8/4/2021
update 2/22/2022
"""
import pandas as pd
from requests import get

symbols_bitfinix = {'BTCUSDT': 'tBTCUST', 'ETHUSDT': 'tETHUST', 'ADAUSDT': 'tADAUST', 'DOGEUSDT': 'tDOGE:UST',
                    'BCHUSDT': 'tBCHN:UST', 'ETCUSDT': 'tETCUST'}


def get_candle_binance(coin: str, limit: int = 1000, timeframe: str = '4h'):
    params = {'interval': timeframe, 'symbol': coin, 'limit': limit}
    url = 'https://api1.binance.com/api/v3/klines'
    try:
        r = get(url=url, params=params)
        data = r.json()
        data = pd.DataFrame(data=data, columns=['date', 'open', 'high', 'low', 'close', 'volume', 'close_time',
                                                'Qav', 'trade-number', 'TBbav', 'TBbqv', 'ignore']).astype(float)
        data = data[data.columns[0:6]]
        return False, data
    except Exception as e:
        result = 'something wrong getting data from binance:\n' + str(e)
        return True, result


def get_candle_bitfinex(coin: str, timeframe: str, limit: int):
    coin = symbols_bitfinix[coin]
    params = {'limit': limit, 'sort': -1}
    url = f'https://api-pub.bitfinex.com/v2/candles/trade:{timeframe}:{coin}/hist'
    try:
        r = get(url=url, params=params)
        data = r.json()
        data = pd.DataFrame(data=data, columns=['date', 'open', 'close', 'high', 'low', 'volume'])
        data.date = pd.DatetimeIndex(pd.to_datetime(data['date'], unit='ms', yearfirst=True)
                                     ).tz_localize('UTC').tz_convert('Asia/Tehran')
        data = data.iloc[::-1]
        data = data.reset_index(drop=True)
        return data
    except Exception as e:
        print('something wrong on get data from bitfinex:\n', e)

