# -*- coding: utf-8 -*-

# 导入python 内置的 WSGI server

from typing import Dict
from wsgiref.simple_server import make_server


def app(environ: Dict, res):
    print(environ.keys())
    status = '200 OK'
    headers = [('Content-Type', 'text/html;charset=utf8')]
    res(status, headers)
    return [b"<h1>Hello World</h1>"]


if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8080, app)
    httpd.serve_forever()
