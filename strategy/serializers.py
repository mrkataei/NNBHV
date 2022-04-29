from .models import UserStrategies, Strategies
from rest_framework import serializers
from user.models import Exchange


class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategies
        fields = ('name', 'description')


class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = ('name',)


class UserStrategySerializer(serializers.ModelSerializer):
    strategy = StrategySerializer()
    exchange = ExchangeSerializer()

    class Meta:
        model = UserStrategies
        fields = ('user', 'strategy', 'exchange', 'coin', 'trade_percent')



