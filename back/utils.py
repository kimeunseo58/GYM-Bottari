


def request_parse(request):
    return f"{request.method} To {request.url} From {request.client.host}:{request.client.port}"