# -*- coding: utf-8 -*-

import os
import time
import os.path
import shutil
from idarea.migrate.static import migrateObj
from idarea.common.utils import PART_SEQ,MD5_HEAD,SLEEP_INTERVAL
from idarea.ring.variable import CURRENT_RING_SEQ
from idarea.common.utils import OBJECT_SUFFIX,MIGRATE_SUFFIX,QUEUE_TIMEOUT_INTERVAL
from idarea.ring.variable import LOAD_HOST_LIST

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

def get_http_addr(dstHostUuid):
    
    for host_info in LOAD_HOST_LIST:
        if host_info[0] == dstHostUuid:
            host = host_info[1]
            port = int(host_info[2])  
            break
    return host,port

def fs_get_md5_list(part):
    
    part_dir = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part)])
    md5_objs = []
    all_objs = os.listdir(part_dir)
    for obj in all_objs:
        if obj in [PART_SEQ]:
            continue
        md5_objs.append(obj)

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
        
    set_seq(part, seq)
    
    alread_md5_ojbs = fs_get_md5_list(part)
    for md5,hostUuid in md5_list.items():
        exists = False
        for alread_md5 in alread_md5_ojbs:
            if alread_md5 == md5:
                exists = True
                break
            if alread_md5 == md5 + MD5_HEAD:
                set_md5_src(part, md5, hostUuid)
                exists = True
                break
        if exists:
            continue
        set_md5_src(part, md5, hostUuid)

    # 若源在md5list中不存在，说明当前md5文件已经传输结束了。
    # 并可以增加API，传输part 列表，如果当前的主机中的part不在此part列表中，且所有的文件为md5.head
    # 则说明part已经传输完毕了，可以删除part了。
    for alread_md5_obj in alread_md5_ojbs:
        if alread_md5_obj.endswith(MD5_HEAD) and alread_md5_obj[:-5] not in md5_list.keys():
            del_md5_head(part, md5)
            
def signal_handler():
    if migrateObj.interruptEvent.isSet():  
        print 'thread finished'  
        raise KeyboardInterrupt
       
def signal_sleep(seconds):
    
    total = 0
    while total < seconds:
        signal_handler()
        time.sleep(SLEEP_INTERVAL)
        total = total + SLEEP_INTERVAL
        
def getQueuItem(queue):
    
    while True:
        try:
            item = queue.get(timeout=QUEUE_TIMEOUT_INTERVAL)
        except:
            signal_handler()
        else:
            break    
    return item

