from django.db import models


class BackTest(models.Model):
    strategy = models.CharField(max_length=30)
    create_at = models.DateTimeField(auto_now=True)
    coin = models.CharField(max_length=10)
    timeframe = models.CharField(max_length=4)
    total_tades = models.IntegerField(default=0)
    net_profit = models.FloatField()
    accuracy = models.FloatField()
    positive_trades = models.FloatField()
    average_trade_profit = models.FloatField()
    profit_per_coin = models.FloatField()
    final_amount = models.FloatField()
