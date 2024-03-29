from django.contrib import admin
from . import models


@admin.register(models.Plan)
class Plan(admin.ModelAdmin):
    list_display = ('name', 'duration_day', 'strategy_number', 'exchange_number', 'cost')


@admin.register(models.Coin)
class Coin(admin.ModelAdmin):
    list_display = ('name', 'amount')


class CoinInline(admin.TabularInline):
    model = models.Coin
    extra = 4


@admin.register(models.Demo)
class Demo(admin.ModelAdmin):
    list_display = ('name', 'user')
    # inlines = [CoinInline, ]


class DemoInline(admin.TabularInline):
    model = models.Demo
    extra = 1


@admin.register(models.Exchange)
class Exchange(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.UserExchange)
class UserExchange(admin.ModelAdmin):
    list_display = ('name', 'user')


class ExchangeInline(admin.TabularInline):
    model = models.UserExchange
    extra = 2


@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = ('username', 'chat_id', 'plan_id', 'last_login')
    list_filter = ('last_login',)
    inlines = [ExchangeInline, DemoInline]
