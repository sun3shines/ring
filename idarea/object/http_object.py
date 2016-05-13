# -*- coding: utf-8 -*-

import json
from idarea.common.http import jresponse
from idarea.object.md5st import MSt
from webob import Request, Response

def doObjectPut(request):
    
    md5 = request.headers.get('md5')
    part = request.headers.get('part')
    seq = request.headers.get('part_seq')
    fileinput = request.environ['wsgi.input']
    print part
    
    m = MSt(str(part),md5,seq=seq)
    if m.exists:
        return jresponse('0','file alread exists',request,200)
    m.put(fileinput)
    
    return jresponse('0','',request,200)

def doObjectGet(request):
    
    param = json.loads(request.body)
    md5 = param.get('md5') 
    part = param.get('part')

    print part
    
    m = MSt(str(part),md5)
    if not m.exists:
        return jresponse('0','file not exists',request,409)

    app_iter = m.get()
    response = Response(app_iter=app_iter,request=request)
    return request.get_response(response)

