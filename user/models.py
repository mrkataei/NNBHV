from django.contrib.auth.models import AbstractUser
from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    cost = models.FloatField(default=0)
    duration_day = models.IntegerField(default=30)
    strategy_number = models.IntegerField(default=1)
    exchange_number = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(primary_key=True, max_length=150, unique=True)
    chat_id = models.CharField(max_length=15, null=True, blank=False)
    phone = models.CharField(max_length=15, null=True, blank=False)
    plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username


class Exchange(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class UserExchange(models.Model):
    name = models.ForeignKey(Exchange, on_delete=models.CASCADE, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.CharField(max_length=300)
    secret = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username


class Coin(models.Model):
    name = models.CharField(primary_key=True, max_length=150, unique=True)
    amount = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Demo(models.Model):
    name = models.CharField(primary_key=True, max_length=150, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.ManyToManyField(Coin)

    def __str__(self):
        return self.name



