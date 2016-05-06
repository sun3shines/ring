
import json
from idarea.common.http import jresponse

def doProxyPut(request):
    
    md5 = request.headers.get('md5')
    fileinput = request.environ['wsgi.input']
    
    return jresponse('0','',request,200)

def doProxyGet(request):
    param = json.loads(request.body)
    md5 = param.get('md5') 
    
    return jresponse('0','',request,200)

