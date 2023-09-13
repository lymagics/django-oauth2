from django.urls import path

from oauth2 import views

urlpatterns = [
    path('authorize/<provider>/', views.oauth2_authorize, name='authorize'),
]

app_name = 'oauth2'
