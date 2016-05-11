# -*- coding: utf-8 -*-

import os
import os.path
from idarea.common.utils import OBJECT_SUFFIX,MIGRATE_SUFFIX

from idarea.migrate.static import migrateObj
from idarea.ring.variable import CURRENT_RING_SEQ

def get_part_seq(obj,latest_seq):
    
    path = '/'.join([migrateObj.MIGRATE_DATA_DIR,obj,'seq'])
    if not os.path.exists(path):
        return latest_seq
    
    with open(path,'r') as f:
        seq = int(f.read())
    return seq

def get_not_latest_parts():
    
    latest_seq = CURRENT_RING_SEQ
    objs = os.listdir(migrateObj.MIGRATE_DATA_DIR)
    not_latest_parts = []
    for obj in objs:
        
        if obj in [OBJECT_SUFFIX,MIGRATE_SUFFIX]:
            continue
        if obj.endswith(migrateObj.PULL_SUFFIX) or obj.endswith(migrateObj.PUSH_SUFFIX):
            continue
        
        seq = get_part_seq(obj,latest_seq)
        if seq < latest_seq:
            not_latest_parts.append(obj) 
            
    return not_latest_parts

