# -*- coding: utf-8 -*-

import os
import os.path
import time
from idarea.common.utils import OBJECT_SUFFIX,MIGRATE_SUFFIX

from idarea.migrate.static import migrateObj
from idarea.ring.variable import CURRENT_RING_SEQ
from idarea.ring.query import part2addressEx
from idarea.migrate.queue.lib import get_seq,fs_get_part_list

def process_init_parts():
    
    while True:
        latest_seq = CURRENT_RING_SEQ
        part_objs = fs_get_part_list()
        for part_obj in part_objs:
            
            if migrateObj.PROCESS_OBJS.has_val(int(part_obj)):
                continue
            migrateObj.PROCESS_OBJS.put(int(part_obj))
            
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
        

