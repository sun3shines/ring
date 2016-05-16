
from idarea.ring.variable import LOAD_HOST_LIST

def get_http_addr(dstHostUuid):
    
    exists = False
    for host_info in LOAD_HOST_LIST:
        if host_info[0] == dstHostUuid:
            host = host_info[1]
            port = int(host_info[2])
            exists = True  
            break
    if exists:
        return host,port
    else:
        return None,None 