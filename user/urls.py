from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('create-user', views.create_user),
    path('profile', views.profile)
]
