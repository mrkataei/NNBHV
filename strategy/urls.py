from django.urls import path
from . import views

app_name = 'strategy'

urlpatterns = [
    path('', views.strategies),
    # path('get-update-delete/<pk>', views.strategy),
    # path('/edit/<pk>', views.edit),
]
