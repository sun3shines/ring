# -*- coding: utf-8 -*-

from array import array
from hashlib import md5
from struct import unpack_from
from idarea.proxy.host import getUuids

_NODE_UUIDS = getUuids()
_PARTITION_POWER = 16
_NODE_COUNT = len(_NODE_UUIDS)

def _node2uuid():
    
    # 排序会重新排序了。采用字符串转化为整数的方式，目前为临时
    # unpack_from('>I',md5(str(data_id)).digest())[0] 
    
    node2Uuid = sorted(_NODE_UUIDS, key=lambda host : unpack_from('>I',md5(str(host[0])).digest())[0])
    return node2Uuid

def _part2node(): 
    part2node = []
    for part in xrange(2**_PARTITION_POWER):
        part2node.append(part % _NODE_COUNT)
   
    return part2node
