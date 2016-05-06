
import json
from idarea.common.http import jresponse
from idarea.proxy.ring.query import objid2address

def doObjectPut(request):
    
    md5 = request.headers.get('md5')
    part = request.headers.get('part')
    fileinput = request.environ['wsgi.input']
    print part
    print len(fileinput.read())
    return jresponse('0','',request,200)

def doObjectGet(request):
    
    param = json.loads(request.body)
    md5 = param.get('md5') 
    part = param.get('part')

    print part
    return jresponse('0','',request,200)

