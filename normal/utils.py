def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_client_ip(request):
    try:
        dataquery = request.headers['Forwarded'].split(';')
        data = {}
        for i in dataquery:
            a, b = i.split('=')
            data[a] = b
        ip = data['for']
        return ip
    except KeyError:
        return '127.0.0.1'

or 
# in flask
request.environ['REMOTE_ADDR']

