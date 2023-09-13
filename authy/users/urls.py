from django.urls import path

from users.api import views

urlpatterns = [
    path('create/', views.user_create, name='create'),
]

app_name = 'users'
