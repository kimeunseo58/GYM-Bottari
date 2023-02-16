

def request_parse(request):
    return f"\tMethod : {request.method}\n\t여기에서 : {request.client.host}:{request.client.port}\n\t여기로 : {request.url}"

def response_parse(response):
    return f"\t응답코드 : {response.status_code}"