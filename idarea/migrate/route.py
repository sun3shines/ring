# -*- coding: utf-8 -*-

from idarea.common.http import jresponse
from idarea.common.urls.migrate import strPartTransmit,strPartListTransmit
from idarea.migrate.http_migrate import doPartTransmit,doMergePartList

url2view = {}

url2view.update({strPartTransmit:doPartTransmit})
url2view.update({strPartListTransmit:doMergePartList})

def process_request(request):

    url = request.path
    print url
    if url not in url2view:
        return jresponse('-1','url error',request,404)
     
    return url2view[url](request)
