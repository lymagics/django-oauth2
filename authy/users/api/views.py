from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.decorators import input, output
from users import services, selectors
from users.api.schemas import UserIn, UserOut


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


@api_view(['GET'])
@output(UserOut)
def user_get(request, pk: int):
    user = selectors.user_get(pk)
    if user is None:
        raise Http404
    return user
