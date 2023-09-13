from django.urls import path

from oauth2 import views

urlpatterns = [
    path('authorize/<provider>/', views.oauth2_authorize, name='authorize'),
    path('callback/<provider>/', views.oauth2_callback, name='callback'),
]

app_name = 'oauth2'
