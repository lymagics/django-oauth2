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
