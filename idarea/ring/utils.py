# -*- coding: utf-8 -*-

import os
import sys
import os.path
import time
import json
from hashlib import md5
from struct import unpack_from
from idarea.ring.host import getUuids

from idarea.ring.static import RING_SET_DIR,_PARTITION_POWER

def get_previous_set():
    
    part_set = {}
    if not os.path.exists(RING_SET_DIR):
        return part_set,-1

    objs = os.listdir(RING_SET_DIR)
    if not objs:
        return part_set,-1
    
    set_info = [tuple(obj.split('_')) for obj in objs]
    new_set_info = sorted(set_info, key=lambda host : host[1])
    parent_time,parent_seq = new_set_info[-1]
    ring_set_path = '/'.join([RING_SET_DIR,'_'.join(list(new_set_info[-1]))])
    with open(ring_set_path,'r') as f:
        part_set = json.load(f)
    return part_set,parent_seq

def get_new_hosts():
    
    _NODE_UUIDS = getUuids()
    node2Uuid = sorted(_NODE_UUIDS, key=lambda host : unpack_from('>I',md5(str(host[0])).digest())[0])
    return node2Uuid

def create_first_set():
    
    if not os.path.exists(RING_SET_DIR):
        os.mkdir(RING_SET_DIR)
        
    current_sequence = 0
    
    ring_set = {}
    
    new_hosts = get_new_hosts()
    ring_set.update({'hostList':new_hosts})
    for host in new_hosts:
        hostUuid = host[0]
        ring_set.update({hostUuid:[]})
    
    _NODE_COUNT = len(new_hosts)
    
    part2node = []
    for part in xrange(2**_PARTITION_POWER):
        node = part % _NODE_COUNT
        part2node.append(node)
        hostUuid = new_hosts[node][0]
        ring_set[hostUuid].append(part)
        # part & node
        
    ring_set_path = '/'.join([RING_SET_DIR,'_'.join([str(int(time.time())),str(current_sequence)])])
    with open(ring_set_path,'w') as f:
        json.dump(ring_set,f)

def build_set():
    
    old_set,old_seq = get_previous_set()
    if not old_set:
        create_first_set()
        return
    
    old_hosts = old_set.get('hostList')
    new_hosts = get_new_hosts()
    if len(new_hosts) != len(old_hosts) + 1:
        print 'add hosts error,exit'
        sys.exit(0)
     
    for new_host in new_hosts:
        
        for old_host in old_hosts:
            if new_host[0] == old_host[0]:
                break
            
if __name__ == '__main__':

    build_set()
 
