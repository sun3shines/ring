# -*- coding: utf-8 -*-

import os
import sys
import os.path
import time
import json
import copy
from hashlib import md5
from struct import unpack_from

from idarea.ring.static import RING_SET_DIR,PART_TOTAL
from idarea.ring.host import NODE_UUIDS,RING_SET_LIST

def get_previous_set():
    
    part_set = {}
    if not RING_SET_LIST:
        return part_set,-1

    parent_time,parent_seq = RING_SET_LIST[-1]
    
    ring_set_path = '/'.join([RING_SET_DIR,'_'.join(list(RING_SET_LIST[-1]))])
    with open(ring_set_path,'r') as f:
        part_set = json.load(f)
        
    return part_set,parent_seq

def get_new_hosts():
    
    node2Uuid = sorted(NODE_UUIDS, key=lambda host : unpack_from('>I',md5(str(host[0])).digest())[0])
    return node2Uuid

def dump_ring_set(ring_set,current_sequence):
    
    ring_set_path = '/'.join([RING_SET_DIR,'_'.join([str(int(time.time())),str(current_sequence)])])
    with open(ring_set_path,'w') as f:
        json.dump(ring_set,f)
        

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
    for part in xrange(PART_TOTAL):
        node = part % _NODE_COUNT
        part2node.append(node)
        hostUuid = new_hosts[node][0]
        ring_set[hostUuid].append(part)
        
        
    dump_ring_set(ring_set, current_sequence)

def create_latest_set(old_ring_set,old_seq,new_hosts,old_hosts,new_host):
    
    new_host_uuid = new_host[0]
    new_ring_set = copy.deepcopy(old_ring_set)
    
    new_ring_set.update({new_host_uuid:[]})
        
    vnodes_to_reassign = PART_TOTAL / len(new_hosts)
    while vnodes_to_reassign > 0:
           
            for old_host in old_hosts:
                old_host_uuid = old_host[0]
                move_part =  new_ring_set[old_host_uuid].pop(0)
                new_ring_set[new_host_uuid].append(move_part)
                vnodes_to_reassign -= 1
                if vnodes_to_reassign <= 0:
                    break
                    
            if vnodes_to_reassign <= 0:
                break
            
    new_ring_set.update({'hostList':new_hosts})
    new_seq = int(old_seq) + 1
    
    dump_ring_set(new_ring_set, new_seq)
    

def build_set():
    
    old_ring_set,old_seq = get_previous_set()
    if not old_ring_set:
        create_first_set()
        return
    
    old_hosts = old_ring_set.get('hostList')
    new_hosts = get_new_hosts()
    if len(new_hosts) != len(old_hosts) + 1:
        print 'add hosts error,exit'
        sys.exit(0)
     
    for new_host in new_hosts:
        exists = False
        for old_host in old_hosts:
            if new_host[0] == old_host[0]:
                exists = True
                break
        if not exists:
            break
        
    create_latest_set(old_ring_set, old_seq, new_hosts, old_hosts, new_host)
        
if __name__ == '__main__':

    build_set()
 
