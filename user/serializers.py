from .models import User, UserExchange, Plan
from rest_framework import serializers


class UserExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExchange
        fields = ('name',)


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExchange
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    plan_id = PlanSerializer()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'chat_id', 'email', 'password',
                  'date_joined', 'plan_id')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

