# -*- coding: utf-8 -*-
import os
from idarea.ring.static import HOST_PROC_CONF,RING_SET_DIR,STARTUP_PROC_LIST

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

def get_startup_list():

    uuid_list = []
    with open(STARTUP_PROC_LIST) as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            
            line = line.strip()
            if not line:
                continue
            if len(line) != len('ewBcdo1A-wniYbw-NctK'):
                continue
            
            uuid_list.append(line)
    return uuid_list
    
def get_ring_list():
    
    if not os.path.exists(RING_SET_DIR):
        return []

    ring_objs = os.listdir(RING_SET_DIR)
    if not ring_objs:
        return []
    
    set_info = [tuple(ring_obj.split('_')) for ring_obj in ring_objs]
    new_set_info = sorted(set_info, key=lambda host : host[1])
    return new_set_info

NODE_UUIDS = getUuids()
RING_SET_LIST = get_ring_list()
