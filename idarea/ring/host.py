# -*- coding: utf-8 -*-
import os
from idarea.ring.static import HOST_PROC_CONF,RING_SET_DIR

def getUuids():
    
    uuid_list = []
    with open(HOST_PROC_CONF) as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            
            line = line.strip()
            if not line:
                continue
            info = line.split(',')
            if len(info) != 4:
                continue
            uuid_list.append(tuple(info))
    return uuid_list

def get_ring_list():
    
    if not os.path.exists(RING_SET_DIR):
        return []

    objs = os.listdir(RING_SET_DIR)
    if not objs:
        return []
    
    set_info = [tuple(obj.split('_')) for obj in objs]
    new_set_info = sorted(set_info, key=lambda host : host[1])
    return new_set_info

NODE_UUIDS = getUuids()
RING_SET_LIST = get_ring_list()
