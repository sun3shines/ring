# -*- coding: utf-8 -*-

import json
from idarea.common.http import jresponse
from idarea.ring.query import objid2address
from idarea.ring.variable import CURRENT_RING_SEQ
from idarea.proxy.transmit import sendfile,recvfile
from idarea.common.webobx import Request, Response

def doProxyPut(request):

    md5 = request.headers.get('md5')
    length = request.headers.get('Content-Length')

    fileinput = request.environ['wsgi.input']
    host,port,part = objid2address(md5)
    
    seq = CURRENT_RING_SEQ
    print host,port,part,seq
    sendfile(host, port, part,seq, md5, length,fileinput)
    
    return jresponse('0','',request,200)

def doProxyGet(request):
    
    param = json.loads(request.body)
    md5 = param.get('md5') 
    host,port,part = objid2address(md5)
    print host,port,part
    app_iter = recvfile(host, port, part, md5)
        
    response = Response(app_iter=app_iter,request=request)
    return request.get_response(response)


