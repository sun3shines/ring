
import json
from idarea.common.http import jresponse
from idarea.proxy.ring.query import objid2address
from idarea.proxy.transmit import sendfile,recvfile

def doProxyPut(request):

    import pdb;pdb.set_trace()    
    md5 = request.headers.get('md5')
    length = request.headers.get('Content-Length')

    fileinput = request.environ['wsgi.input']
    host,port,part = objid2address(md5)
    print host,port,part
    sendfile(host, port, part, md5, length,fileinput)
    
    return jresponse('0','',request,200)

def doProxyGet(request):
    
    param = json.loads(request.body)
    md5 = param.get('md5') 
    host,port,part = objid2address(md5)
    print host,port,part
    recvfile(host, port, part, md5)
        
    return jresponse('0','',request,200)

