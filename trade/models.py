from django.db import models


class Trade(models.Model):
    objects = models.Manager()
    position = (
        ('S', 'Sell'),
        ('B', 'Buy')
    )
    strategy = models.CharField(max_length=15, blank=False)
    coin = models.CharField(max_length=15, blank=False)
    timeframe = models.CharField(max_length=15, blank=False)
    status = models.CharField(max_length=15, blank=False)
    position = models.CharField(max_length=1, choices=position)
    price = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    create_at = models.DateTimeField(auto_now=True)
    signal_at = models.DateTimeField()

    def __str__(self):
        return self.strategy
