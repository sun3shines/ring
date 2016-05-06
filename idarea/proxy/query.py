# -*- coding: utf-8 -*-

from array import array
from hashlib import md5
from struct import unpack_from

from idarea.proxy.static import PARTITION_SHIFT,PART2NODE,NODE2UUID

def objid2uuid(idstr):
    part = unpack_from('>I',md5(str(idstr)).digest())[0] >> PARTITION_SHIFT 
    node = PART2NODE[part] 
    uuid = NODE2UUID[node]
    return uuid

if __name__ == '__main__':
    
    print objid2uuid('a')
    print objid2uuid('b')
