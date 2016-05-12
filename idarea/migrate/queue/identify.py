# -*- coding: utf-8 -*-

import os
import os.path
import time
from idarea.common.utils import OBJECT_SUFFIX,MIGRATE_SUFFIX

from idarea.migrate.static import migrateObj
from idarea.ring.variable import CURRENT_RING_SEQ
from idarea.ring.query import part2addressEx
from idarea.migrate.queue.lib import get_part_seq

def process_init_parts():
    
    while True:
        latest_seq = CURRENT_RING_SEQ
        objs = os.listdir(migrateObj.MIGRATE_DATA_DIR)
        for obj in objs:
            if migrateObj.PROCESS_OBJS.has_val(int(obj)):
                continue
            migrateObj.PROCESS_OBJS.put(int(obj))
            if obj in [OBJECT_SUFFIX,MIGRATE_SUFFIX]:
                continue
            
            seq = get_part_seq(obj,latest_seq)
            if seq < latest_seq:
                migrateObj.PAST_QUEUE.put((int(obj),seq)) 
            else:
                migrateObj.LATEST_QUEUE.put(int(obj))
                
        time.sleep(60)
        
def process_past_parts():
    
    while True:
        part,seq = migrateObj.PAST_QUEUE.get()
        while True:
            stepping_seq = str(int(seq)+1)
            stepping_ring = migrateObj.ALL_RING_SET.get(stepping_seq)
            host,port,_,hostUuid = part2addressEx(part,stepping_ring)
            if hostUuid != migrateObj.MIGRATE_UUID:
                migrateObj.TRANSMIT_PARTS.append((host,port,part,hostUuid,stepping_seq))
                break
            
            if int(stepping_seq) == int(CURRENT_RING_SEQ):
                migrateObj.UPGRADED_PARTS.append((part,stepping_seq))
                migrateObj.LATEST_PARTS.append(part)
                break
            
            seq = stepping_seq
        

