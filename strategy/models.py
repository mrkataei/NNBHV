from django.db import models
from user.models import User, Exchange


class Strategies(models.Model):
    name = models.CharField(max_length=15, blank=False)
    description = models.TextField(max_length=200, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Coin(models.Model):
    objects = models.Manager()
    name = models.CharField(primary_key=True, max_length=150, unique=True)

    def __str__(self):
        return self.name


class UserStrategies(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    strategy = models.ForeignKey(Strategies, on_delete=models.CASCADE)
    exchange = models.ForeignKey(Exchange, on_delete=models.DO_NOTHING, null=True, blank=False)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
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

