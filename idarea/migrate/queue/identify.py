# -*- coding: utf-8 -*-

import os
import os.path
import time
from idarea.common.utils import OBJECT_SUFFIX,MIGRATE_SUFFIX

from idarea.migrate.static import migrateObj
from idarea.ring.variable import CURRENT_RING_SEQ
from idarea.ring.query import part2addressEx
from idarea.migrate.queue.lib import get_seq,fs_get_part_list
from idarea.migrate.queue.process import transmit,upgrade

def process_init_parts():
    
    while True:
        latest_seq = CURRENT_RING_SEQ
        part_objs = fs_get_part_list()
        for part_obj in part_objs:
            
            seq = get_seq(int(part_obj))
            if seq < latest_seq:
                migrateObj.PAST_QUEUE.put((int(part_obj),seq)) 
            else:
                migrateObj.LATEST_QUEUE.put(int(part_obj))
                
        time.sleep(60)
        
def process_past_parts():
    
    while True:
        part,seq = migrateObj.PAST_QUEUE.get()
        while True:
            stepping_seq = str(int(seq)+1)
            stepping_ring = migrateObj.ALL_RING_SET.get(stepping_seq)
            host,port,_,hostUuid = part2addressEx(part,stepping_ring)
            if hostUuid != migrateObj.MIGRATE_UUID:
                migrateObj.TRANSMIT_QUEUE.put((host,port,part,hostUuid,stepping_seq))
                break
            
            if int(stepping_seq) == int(CURRENT_RING_SEQ):
                migrateObj.UPGRADED_QUEUE.put((part,stepping_seq))
                migrateObj.LATEST_QUEUE.put(part)
                break
            
            seq = stepping_seq
        

def transmit_parts():
    
    while True:
        part_info = migrateObj.TRANSMIT_QUEUE.get()
        host = part_info[0]
        port = part_info[1]
        part = part_info[2]
        seq = part_info[4]
        port = int(port) + migrateObj.PORT_ADDITION
        transmit(part,seq,host,port)
        
def upgrade_parts():
    
    while True:
        part_info = migrateObj.UPGRADED_QUEUE.get()
        part,upgrade_seq = part_info
        upgrade(part, upgrade_seq)
        migrateObj.LATEST_QUEUE.put(int(part))
        
def latest_parts():
    
    while True:
        part = migrateObj.LATEST_QUEUE.get()
        print 'latest part: %s' %(str(part))
    
