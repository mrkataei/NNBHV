from django.urls import path
from . import views

app_name = 'strategy'

urlpatterns = [
    path('', views.backtest),
]
