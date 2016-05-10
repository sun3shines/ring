# -*- coding: utf-8 -*-

from array import array
from hashlib import md5
from struct import unpack_from

from idarea.proxy.static import PARTITION_SHIFT
from idarea.ring.load import load_ring
LOAD_RING_SET = load_ring()
LOAD_HOST_LIST = LOAD_RING_SET.pop('hostList')

def objid2address(idstr):
    
    part = unpack_from('>I',md5(str(idstr)).digest())[0] >> PARTITION_SHIFT
    ring_set = LOAD_RING_SET 
    host_list = LOAD_HOST_LIST 
    for hostUuid  in ring_set:
        if part in ring_set[hostUuid]:
            break
        
    for host_info in host_list:
        if host_info[0] == hostUuid:
            host = host_info[1]
            port = host_info[2]  
    
    return host,port,part

if __name__ == '__main__':
    import pdb;pdb.set_trace() 
    print objid2address('a')
    print objid2address('b')
    print objid2address('c')
