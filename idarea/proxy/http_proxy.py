
import json
from idarea.common.http import jresponse
from idarea.proxy.ring.query import objid2address

def doProxyPut(request):
    
    md5 = request.headers.get('md5')
    fileinput = request.environ['wsgi.input']
    host,port,part = objid2address(md5)
    print host,port,part
    return jresponse('0','',request,200)

def doProxyGet(request):
    
    param = json.loads(request.body)
    md5 = param.get('md5') 
    host,port,part = objid2address(md5)
    print host,port,part
        
    return jresponse('0','',request,200)

