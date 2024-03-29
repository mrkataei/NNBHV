from django.contrib import admin
from . import models


@admin.register(models.Strategies)
class Strategy(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.UserStrategies)
class UserStrategies(admin.ModelAdmin):
    list_display = ('user', 'strategy', 'exchange', 'trade_percent')


