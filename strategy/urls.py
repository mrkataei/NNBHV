from django.urls import path
from . import views

app_name = 'strategy'

urlpatterns = [
    path('', views.strategies),
    path('get-update-delete/<pk>', views.get_update_delete_strategy),
]
