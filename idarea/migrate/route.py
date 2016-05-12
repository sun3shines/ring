# -*- coding: utf-8 -*-

from idarea.common.http import jresponse
from idarea.common.urls.migrate import strPartTransmit
from idarea.migrate.http_migrate import doPartTransmit

url2view = {}

url2view.update({strPartTransmit:doPartTransmit})

def process_request(request):

    url = request.path
    print url
    if url not in url2view:
        return jresponse('-1','url error',request,404)
     
    return url2view[url](request)
