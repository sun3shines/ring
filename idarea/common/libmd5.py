# -*- coding: utf-8 -*-

import os
import os.path
import shutil
from idarea.migrate.static import migrateObj
from idarea.common.utils import MD5_HEAD,MD5_TEMP
from idarea.proxy.transmit import recvfile,delfile
def set_md5_src(part,md5,hostUuid):
    
    # print 'set md5 src hostUuid: %s %s' % (md5,hostUuid)
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

def get_md5_head_path(part,md5):
    
    part_dir = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part)])
    md5_obj_path = '/'.join([part_dir,md5+MD5_HEAD])
    return md5_obj_path

def get_md5_tmp_path(part,md5):
    part_dir = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part)])
    md5_tmp_path = '/'.join([part_dir,md5+MD5_TEMP])
    return md5_tmp_path

def get_md5_path(part,md5):
    part_dir = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part)])
    md5_tmp_path = '/'.join([part_dir,md5])
    return md5_tmp_path
    
def get_obj_md5(md5_obj):
    return md5_obj[:-5]

def download_remote_md5(host,port,part,md5):
    
    md5_tmp_path = get_md5_tmp_path(part, md5)
    try:
        with open(md5_tmp_path,'w') as f:
            for data in recvfile(host, port, part, md5):
                f.write(data)
    except:
        print 'download error %s %s %s %s' % (md5,str(part),host,str(port))
        os.remove(md5_tmp_path)
    else:
        md5_head_path = get_md5_head_path(part, md5)
        os.remove(md5_head_path)
        md5_path = get_md5_path(part, md5)
        shutil.move(md5_tmp_path,md5_path)
        print 'download %s %s %s %s' % (md5,str(part),host,str(port))
    
def delete_remote_md5(host,port,part,md5):
    delfile(host, port, part, md5)
    