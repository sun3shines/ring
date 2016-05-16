# -*- coding: utf-8 -*-

import os
import time
import os.path
import shutil
from idarea.migrate.static import migrateObj
from idarea.common.utils import PART_SEQ
from idarea.ring.variable import CURRENT_RING_SEQ

def get_seq(part):
    
    path = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part),PART_SEQ])
    if not os.path.exists(path):
        return CURRENT_RING_SEQ
    
    path = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part),PART_SEQ])
    with open(path,'r') as f:
        seq = int(f.read())
    return seq
    
def set_seq(part,seq):
    
    path = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part),PART_SEQ])
    with open(path,'w') as f:
        f.write(str(seq))