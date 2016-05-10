# -*- coding: utf-8 -*-

from idarea.ring.static import HOST_PROC_CONF

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


