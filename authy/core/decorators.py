from functools import wraps
from typing import Callable

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer

from core.utils import paginated_response


def input(schema: BaseSerializer, partial: bool = False):
    """
    Input settings for view.
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            s = schema(data=request.data, partial=partial)
            s.is_valid(raise_exception=True)
            return func(request, *args, **kwargs)
        return wrapper
    return decorator


def output(
    schema: BaseSerializer,
    many: bool = False,
    status: int = 200,
):
    """
    Output settings for view.
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            result = func(request, *args, **kwargs)
            if isinstance(result, Response):
                return result
            if not many:
                s = schema(result)
                return Response(s.data, status=status)
            return paginated_response(
                pagination_class=PageNumberPagination,
                schema_class=schema,
                queryset=result,
                request=request,
            )
        return wrapper
    return decorator
