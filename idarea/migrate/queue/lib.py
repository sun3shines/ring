
import os
import os.path
import shutil
from idarea.migrate.static import migrateObj
from idarea.common.utils import PART_SEQ,MD5_HEAD
from idarea.ring.variable import CURRENT_RING_SEQ
from idarea.common.utils import OBJECT_SUFFIX,MIGRATE_SUFFIX

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

def get_md5_head(path):
    
    with open(path,'r') as f:
        hostUuid = f.read()
    return hostUuid

def fs_get_md5_list(part):
    
    part_dir = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part)])
    md5_objs = []
    all_objs = os.listdir(part_dir)
    for obj in all_objs:
        if obj in [PART_SEQ]:
            continue
        md5_objs.append(int(obj))

    return md5_objs

def fs_get_part_list():

    part_objs = []
    all_objs = os.listdir(migrateObj.MIGRATE_DATA_DIR)
    for part_obj in all_objs:
        if part_obj in [OBJECT_SUFFIX,MIGRATE_SUFFIX]:
            continue
        part_objs.append(part_obj)
        
    return part_objs
    
def fs_make_part(part,seq,md5_list):
    
    part_dir = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part)])
    if not os.path.exists(part_dir):
        os.mkdir(part_dir)
    
    alread_md5_ojbs = fs_get_md5_list(part)
    
    set_seq(part, seq)
    
    