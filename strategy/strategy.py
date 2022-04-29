import threading
from .models import Signal
import pandas as pd
import pandas_ta as ta
from tools.data_collector import get_candle_binance


class StrategyInterface:
    def __init__(self, name: str, coin: str, timeframe: str, candles: pd.DataFrame):
        self.name = name
        self.coin = coin
        self.timeframe = timeframe
        self.data = candles
        self.last_signal = Signal.objects.filter(coin=coin,
                                                 timeframe=timeframe, strategy=name).order_by('-create_at')[0]
        self.last_position = self.last_signal.postion
        self.last_price = self.last_signal.price
        self.preprocess()

    def preprocess(self):
        raise NotImplementedError()

    def logic(self):
        raise NotImplementedError()

    def broadcast(self):
        raise NotImplementedError()

    def submit_order(self):
        raise NotImplementedError("need")

    def create(self):
        Signal(strategy=self.name, coin=self.coin, timeframe=self.timeframe,
               position=self.last_position, price=self.last_price).save()

    def signal(self):
        self.logic()
        threading.Thread(target=self.broadcast).start()
        threading.Thread(target=self.submit_order).start()
        threading.Thread(target=self.create).start()


class Amir(StrategyInterface):
    def __init__(self, name: str = 'Amir', coin: str = 'BTCUSDT', timeframe: str = '4h',
                 candles: pd.DataFrame = pd.DataFrame()):
        super().__init__(name, coin, timeframe, candles)

    def preprocess(self):
        self.data = get_candle_binance(coin=self.coin, timeframe=self.timeframe)
        self.data = self.data[1] if not self.data[0] else pd.DataFrame()
        self.data[['macd', 'historical', 'signal']] = ta.macd(close=self.data, fast=12, slow=26, signal=9)

    def logic(self):
        pass

    def broadcast(self):
        pass

    def submit_order(self):
        pass
