from rest_framework.response import Response


def paginated_response(
    pagination_class,
    schema_class,
    queryset,
    request,
) -> Response:
    paginator = pagination_class()
    page = paginator.paginate_queryset(queryset, request)

    if page is not None:
        schema = schema_class(page, many=True)
        return paginator.get_paginated_response(schema.data)

    schema = schema_class(queryset, many=True)
    return Response(schema.data)
