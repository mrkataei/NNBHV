from rest_framework import serializers


class BackSerializer(serializers.Serializer):
    coin = serializers.CharField(max_length=5, required=True)
    timeframe = serializers.CharField(max_length=3)
