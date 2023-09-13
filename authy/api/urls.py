from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),
]

app_name = 'api'
