from django.db import models
from user.models import User, Exchange


class Strategies(models.Model):
    name = models.CharField(max_length=15, blank=False)
    description = models.TextField(max_length=200, null=True, blank=True)
    coin = models.TextField(max_length=10, default='BTCUSDT')
    timeframe = models.TextField(max_length=10, default='4h')

    objects = models.Manager()

    def __str__(self):
        return self.name


class UserStrategies(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    strategy = models.ForeignKey(Strategies, on_delete=models.CASCADE)
    exchange = models.ForeignKey(Exchange, on_delete=models.DO_NOTHING, null=True, blank=False)
    trade_percent = models.FloatField()

    def __str__(self):
        return self.user.username


class Signal(models.Model):
    objects = models.Manager()
    position = (
        ('S', 'Sell'),
        ('B', 'Buy')
    )
    strategy = models.CharField(max_length=15, blank=False)
    coin = models.CharField(max_length=15, blank=False)
    timeframe = models.CharField(max_length=15, blank=False)
    position = models.CharField(max_length=1, choices=position)
    price = models.FloatField()
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.strategy

