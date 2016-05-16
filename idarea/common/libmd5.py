# -*- coding: utf-8 -*-

import os
import os.path
from idarea.migrate.static import migrateObj
from idarea.common.utils import MD5_HEAD

def set_md5_src(part,md5,hostUuid):
    
    print 'set md5 src hostUuid: %s %s' % (md5,hostUuid)
    path = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part),md5+MD5_HEAD])
    with open(path,'w') as f:
        f.write(hostUuid)

def del_md5_head(part,md5):
    
    print 'del md5 head: %s' % (md5)
    path = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part),md5+MD5_HEAD])
    os.remove(path)
    
def get_md5_head(path):
    
    with open(path,'r') as f:
        hostUuid = f.read()
    return hostUuid
