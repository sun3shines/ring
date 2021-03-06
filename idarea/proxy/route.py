# -*- coding: utf-8 -*-

from idarea.common.http import jresponse
from idarea.common.urls.proxy import strProxyGet,strProxyPut
from idarea.proxy.http_proxy import doProxyGet,doProxyPut

url2view = {}

url2view.update({strProxyPut:doProxyPut})

url2view.update({strProxyGet:doProxyGet})

def process_request(request):

    url = request.path
    print url
    if url not in url2view:
        return jresponse('-1','url error',request,404)
    return url2view[url](request)
