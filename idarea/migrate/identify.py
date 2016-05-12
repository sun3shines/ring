# -*- coding: utf-8 -*-

import os
import os.path
from idarea.common.utils import OBJECT_SUFFIX,MIGRATE_SUFFIX

from idarea.migrate.static import migrateObj
from idarea.ring.variable import CURRENT_RING_SEQ
from idarea.ring.query import part2addressEx
from idarea.migrate.lib import get_part_seq

def process_init_parts():
    
    latest_seq = CURRENT_RING_SEQ
    objs = os.listdir(migrateObj.MIGRATE_DATA_DIR)
    for obj in objs:
        if obj in [OBJECT_SUFFIX,MIGRATE_SUFFIX]:
            continue
        if obj.endswith(migrateObj.PULL_SUFFIX):
            migrateObj.PULLED_PARTS.append(int(obj))
            continue 
        if obj.endswith(migrateObj.PUSH_SUFFIX):
            migrateObj.PULLED_PARTS.append(int(obj))
            continue
        
        seq = get_part_seq(obj,latest_seq)
        if seq < latest_seq:
            migrateObj.PAST_PARTS.append((int(obj),seq)) 
        else:
            migrateObj.LATEST_PARTS.append(int(obj))
            
def process_past_parts():
    
    for part,seq in migrateObj.PAST_PARTS:
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
            

