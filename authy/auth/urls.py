from django.urls import path

from auth.api import views

urlpatterns = [
    path('login/', views.login, name='login'),
]

app_name = 'auth'
