# -*- coding: utf-8 -*-

import os
import time
import os.path
import shutil
from idarea.migrate.static import migrateObj
from idarea.common.utils import PART_SEQ,MD5_HEAD,SLEEP_INTERVAL,MD5_TEMP
from idarea.ring.variable import CURRENT_RING_SEQ
from idarea.common.utils import OBJECT_SUFFIX,MIGRATE_SUFFIX,QUEUE_TIMEOUT_INTERVAL
from idarea.ring.variable import LOAD_HOST_LIST
from idarea.common.libseq import set_seq
from idarea.common.libmd5 import set_md5_src,del_md5_head,get_obj_md5

def get_http_addr(dstHostUuid):
    
    for host_info in LOAD_HOST_LIST:
        if host_info[0] == dstHostUuid:
            host = host_info[1]
            port = int(host_info[2])  
            break
    return host,port

def get_md5_list(part):
    
    part_dir = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part)])
    md5_objs = []
    all_objs = os.listdir(part_dir)
    for obj in all_objs:
        if len(obj) not in [32,37]:
            continue
        if obj in [PART_SEQ]:
            continue
        if obj.endswith(MD5_TEMP):
            continue
        md5_objs.append(obj)

    return md5_objs

def get_part_list():

    part_objs = []
    all_objs = os.listdir(migrateObj.MIGRATE_DATA_DIR)
    for part_obj in all_objs:
        
        if part_obj in [OBJECT_SUFFIX,MIGRATE_SUFFIX]:
            continue
        try:
            int_obj = int(part_obj)
        except:
            continue
        
        part_objs.append(part_obj)
        
    return part_objs
    
def merge_part(part,seq,md5_list):
    
    part_dir = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part)])
    
    if not os.path.exists(part_dir):
        os.mkdir(part_dir)
        
    set_seq(part, seq)
    
    alread_md5_ojbs = get_md5_list(part)
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
        if alread_md5_obj.endswith(MD5_HEAD) and get_obj_md5(alread_md5_obj) not in md5_list.keys():
            del_md5_head(part, md5)
            
            