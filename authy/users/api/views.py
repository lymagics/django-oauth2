from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.decorators import input
from users import services
from users.api.schemas import UserIn


@api_view(['POST'])
@input(UserIn)
def user_create(request):
    data = request.data
    services.user_create(
        data['email'],
        data['username'],
        data['password'],
    )
    return Response(status=200)
