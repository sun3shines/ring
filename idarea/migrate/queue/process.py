# -*- coding: utf-8 -*-

import os
from idarea.migrate.static import migrateObj
from idarea.migrate.queue.lib import get_md5_head,set_seq,fs_get_md5_list
from idarea.common.utils import PART_SEQ,MD5_HEAD
from idarea.client.transmit import http_transmit_part

def transmit(part,seq):
    
    # 如果网络传输失败，则应该继续放入队列中来处理了
     
    part_dir = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part)])
    print 'transmit part: %s %s' % (part_dir,str(seq))
    
    msg_list = {}
    md5_objs = fs_get_md5_list(part)
    for md5_obj in md5_objs:
        if md5_obj.endswith(MD5_HEAD):
            md5 = md5_obj[-5]
            md5_obj_path = '/'.join([part_dir,md5_obj])
            hostUuid = get_md5_head(md5_obj_path)
        else:
            md5 = md5_obj
            hostUuid = migrateObj.MIGRATE_UUID
        msg_list.update({md5:hostUuid})
    http_transmit_part(part, seq, msg_list)
    
def upgrade(part,seq):
    
    print 'upgrade part: %s %s' % (str(part),str(seq))
    # set_seq(part, seq)
    
def transmit_parts():
    
    while True:
        part_info = migrateObj.TRANSMIT_QUEUE.get()
        part = part_info[2]
        seq = part_info[4]
        transmit(part,seq)
        
def upgrade_parts():
    
    while True:
        part_info = migrateObj.UPGRADED_QUEUE.get()
        part,upgrade_seq = part_info
        upgrade(part, upgrade_seq)
        migrateObj.LATEST_QUEUE.put(int(part))
        
def latest_parts():
    
    while True:
        part = migrateObj.LATEST_QUEUE.get()
        print 'latest part: %s' %(str(part))
    
