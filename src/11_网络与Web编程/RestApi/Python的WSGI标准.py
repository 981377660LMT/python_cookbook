import cgi


def wsgi_app(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    # Parse the query parameters
    params = cgi.FieldStorage(environ['wsgi.input'], environ=environ)
    start_response('200 OK', [('Content-type', 'text/plain')])
    # 为了返回数据，一个WSGI程序必须返回一个字节字符串序列
    resp = []
    resp.append(b'Hello World\n')
    resp.append(b'Goodbye!\n')
    return resp
