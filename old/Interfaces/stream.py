"""
    Mr.Kataei 11/12/2021
"""
from old import threading
from old.Inc.functions import get_coin_id
from old.Conf import get_analysis_setting


class Stream:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.coin_id = get_coin_id(symbol)

    # there is 4 functions for 4 timeframes after all used in main async
    def customer_strategy(self):
        raise Exception("NotImplementedException")

    def stream(self):
        # multi threading study !!!!!!!!!!!!!!!
        customer_strategy = threading.Thread(target=self.customer_strategy)
        customer_strategy.start()

    def get_setting_analysis(self, analysis_id: int, timeframe_id: int):
        settings = get_analysis_setting(coin_id=self.coin_id, timeframe_id=timeframe_id,
                                        analysis_id=analysis_id)
        return settings

    def run(self):
        self.stream()
