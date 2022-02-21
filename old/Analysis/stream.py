"""
Mr.Kataei 8/15/2021
updated at 9/16/2021
updated at 2/22/2022

"""
from emerald import Emerald
from old.Libraries import *
from old.Interfaces import *
from old import config, sleep, time, datetime, process_time, telegram, threading

API_KEY = config('API_KEY')
# @testkourosh2bot -> address // use this bot for test your code set in .env

_bot_ins = telegram.TeleBot(API_KEY)


class StreamIStrategies(Stream):
    def __init__(self, symbol: str):
        Stream.__init__(self, symbol=symbol)

    def customer_strategy(self):
        while True:
            delay = 59
            if 1 <= round(time()) % 60 <= 3:
                print('1min', datetime.fromtimestamp(time()))
                data = candles(symbol=self.symbol, number=1, unit='m', limit=10)
                if data[0]:
                    emerald = Emerald(data=data[1], coin_id=self.coin_id, timeframe_id=5, bot_ins=_bot_ins)
                    emerald.signal()
                delay = process_time()
            sleep(abs(60 - delay))
            sleep(60)


class StrategiesThreads:
    def __init__(self, *symbols: str):
        self.symbols = symbols
        self.threads = []
        for symbol in symbols:
            self.threads.append(threading.Thread(target=StreamIStrategies(symbol=symbol).run))

    def start_threads(self):
        threading.Thread(target=check_validate_stream).start()
        for thread in self.threads:
            thread.daemon = True
            thread.start()

    def join_threads(self):
        for thread in self.threads:
            thread.join()
