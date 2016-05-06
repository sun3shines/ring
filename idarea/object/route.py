# -*- coding: utf-8 -*-

from idarea.common.http import jresponse
from idarea.common.urls.object import strObjectGet,strObjectPut
from idarea.object.http_object import doObjectGet,doObjectPut

url2view = {}

url2view.update({strObjectPut:doObjectPut})
url2view.update({strObjectGet:doObjectGet})

def process_request(request):

    url = request.path
    print url
    if url not in url2view:
        return jresponse('-1','url error',request,404)
     
    return url2view[url](request)
