import sys
import numpy as np
import pandas as pd


class StrategyTaster:
    def __init__(self, name: str, coin: str, timeframe: str, dataframe, initial_value: int):
        self.coin = coin
        self.name = name
        self.timeframe = timeframe
        self.dataframe = dataframe

        self.initial_value = initial_value
        self.current_value = initial_value
        self.old_price = 0
        self.old_position = "sell"
        self.low_price = sys.float_info.min
        self.trades_list = self.taster(dataframe=self.dataframe, function=self.strategy)
        self.result = self.results()

    def reset(self):
        self.current_value = self.initial_value
        self.old_price = 0
        self.old_position = "sell"
        self.low_price = sys.float_info.min

    def taster(self, dataframe, function):
        self.reset()
        output_df = dataframe.apply(lambda row: function(row), axis=1)
        output_df = output_df.dropna()
        return pd.DataFrame(output_df.to_list(),
                            columns=['date', 'position', 'close', "amount", "value", "profit",
                                     "profit", "low price"])

    def strategy(self, row):
        date = row["date"]
        close = row["close"]
        recommendation = row["recommendation"]
        if close <= self.low_price:
            self.low_price = close
        if self.old_position != recommendation:
            if recommendation == 'buy':
                self.old_position = "buy"
                self.old_price = close
                self.low_price = close
                return date, "buy", close, self.current_value / close, self.current_value, "----", "----", "----"
            elif recommendation == "sell":
                self.old_position = "sell"
                self.current_value = self.current_value * (close / self.old_price)
                low = self.low_price
                self.low_price = sys.float_info.min
                return date, "sell", close, \
                       self.current_value / close, self.current_value, close - self.old_price, \
                       round((close / self.old_price) * 100 - 100, 4), ((low - self.old_price) / self.old_price) * 100

    def results(self, result_df=None):
        try:
            starter_amount = self.trades_list["amount"][0]
            dataframe = self.trades_list.drop(self.trades_list[self.trades_list["position"] == "buy"].index)
            net_profit = (np.array(dataframe["value"].tail(1))[0] - self.initial_value) / self.initial_value
            positive_trades = dataframe[dataframe["profit"] >= 0].count()
            total_trades = int(len(dataframe))
            accuracy = positive_trades.date / total_trades
            average_trade_profit = net_profit / total_trades
            profitpercoin = (dataframe["amount"].tail(1).item() - starter_amount) / starter_amount
            result = self.name, self.coin, self.timeframe, round(
                positive_trades.date), round(total_trades), round(accuracy * 100, 2), round(net_profit * 100, 4), round(
                average_trade_profit * 100, 4), round(profitpercoin * 100, 4), \
                     round(dataframe["value"].tail(1).item(), 4)
        except Exception:
            result = self.name, self.coin, self.timeframe, 0, 0, 0, 0, 0, 0, 0

        try:
            return result_df.append(pd.DataFrame(np.asarray(result).reshape(1, 12),
                                                 columns=['strategy', 'coin', 'timeframe', 'starttime', 'endtime',
                                                          "positive_trades", "total_trades", "accuracy",
                                                          "net_profit", "average_trade_profit",
                                                          'profit_per_coin', "final_amount"]))
        except Exception:
            return pd.DataFrame(np.asarray(result).reshape(1, 12),
                                columns=['strategy', 'coin', 'timeframe', 'starttime', 'endtime',
                                         "positive_trades", "total_trades", "accuracy", "net_profit",
                                         "average_trade_profit", 'profit_per_coin', "final_amount"])
