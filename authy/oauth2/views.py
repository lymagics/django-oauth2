from django.conf import settings

from django.contrib.auth import login as django_login
from django.http import JsonResponse, HttpResponseRedirect

from oauth2 import services
from oauth2.errors import OAuth2Error


def oauth2_authorize(request, provider: str):
    try:
        oauth2 = services.oauth2_authorize(provider)
        request.session['oauth2_state'] = oauth2.state
        return HttpResponseRedirect(oauth2.url)
    except OAuth2Error as e:
        detail = {'detail': str(e)}
        return JsonResponse(detail)


def oauth2_callback(request, provider: str):
    data = request.GET
    session = request.session
    try:
        user = services.oauth2_callback(
            provider, data.get('code'),
            data.get('state'), session.get('oauth2_state'),
        )
    except OAuth2Error as e:
        detail = {'detail': str(e)}
        return JsonResponse(detail)

    django_login(request, user)
    response = HttpResponseRedirect(settings.FRONTEND_URL)
    response.set_cookie('access', user.jwt_token)
    return response
