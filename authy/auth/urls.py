from django.urls import path

from auth.api import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]

app_name = 'auth'
