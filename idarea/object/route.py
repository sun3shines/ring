# -*- coding: utf-8 -*-

from idarea.common.http import jresponse
from idarea.common.urls.object import strObjectGet,strObjectPut,strObjectDel
from idarea.object.http_object import doObjectGet,doObjectPut,doObjectDel

url2view = {}

url2view.update({strObjectPut:doObjectPut})
url2view.update({strObjectGet:doObjectGet})
url2view.update({strObjectDel:doObjectDel})

def process_request(request):

    url = request.path
    print url
    if url not in url2view:
        return jresponse('-1','url error',request,404)
     
    return url2view[url](request)
