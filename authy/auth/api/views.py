from django.contrib.auth import login as django_login

from rest_framework.decorators import api_view
from rest_framework.response import Response

from auth import services
from auth.api.schemas import CredentialsIn
from auth.errors import InvalidCredentials
from core.decorators import input


@api_view(['POST'])
@input(CredentialsIn)
def login(request):
    data = request.data
    try:
        user = services.login(
            data['username'], data['password']
        )
    except InvalidCredentials as e:
        detail = {'detail': str(e)}
        return Response(detail, status=403)
    
    django_login(request, user)
    response = Response(status=200)
    response.set_cookie('access', user.jwt_token)
    return response


@api_view(['POST'])
def logout(request):
    response = Response(status=200)
    response.delete_cookie('access')
    return response
