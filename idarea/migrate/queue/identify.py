# -*- coding: utf-8 -*-

from idarea.migrate.static import migrateObj
from idarea.ring.variable import CURRENT_RING_SEQ
from idarea.ring.query import part2addressEx
from idarea.common.libseq import get_seq
from idarea.common.libpart import get_part_list,get_md5_list
from idarea.common.libmd5 import get_md5_head,get_md5_head_path,get_obj_md5,\
    download_remote_md5,delete_remote_md5
from idarea.common.signal import signal_handler,signal_sleep,getQueuItem
from idarea.migrate.queue.process import transmit,upgrade
from idarea.common.utils import MD5_HEAD
from idarea.common.libhost import get_http_addr

def process_init_parts():
   
    print CURRENT_RING_SEQ 
    while True:
        signal_handler()
        part_objs = get_part_list()
        for part_obj in part_objs:
            
            seq = get_seq(int(part_obj))
            if seq < CURRENT_RING_SEQ:
                print 'put',part_obj,seq
                migrateObj.PAST_QUEUE.put((int(part_obj),seq)) 
            else:
                migrateObj.LATEST_QUEUE.put(int(part_obj))
                
        signal_sleep(60)
        
def process_past_parts():
    
    while True:
        
        part,seq = getQueuItem(migrateObj.PAST_QUEUE)
        while True:
            stepping_seq = str(int(seq)+1)
            stepping_ring = migrateObj.ALL_RING_SET[stepping_seq]
            host,port,_,hostUuid = part2addressEx(part,stepping_ring)
            if hostUuid != migrateObj.MIGRATE_UUID:
                migrateObj.TRANSMIT_QUEUE.put((host,port,part,hostUuid,stepping_seq))
                break
            
            if int(stepping_seq) == int(CURRENT_RING_SEQ):
                migrateObj.UPGRADED_QUEUE.put((part,stepping_seq))
                migrateObj.LATEST_QUEUE.put(part)
                break
            
            seq = stepping_seq
        
def transmit_parts():
   
    while True:
        part_info = getQueuItem(migrateObj.TRANSMIT_QUEUE)
        host = part_info[0]
        port = part_info[1]
        part = part_info[2]
        seq = part_info[4]
        port = int(port) + migrateObj.PORT_ADDITION
        transmit(part,seq,host,port)
        
def upgrade_parts():
    
    while True:
        part_info = getQueuItem(migrateObj.UPGRADED_QUEUE)
        part,upgrade_seq = part_info
        upgrade(part, upgrade_seq)
        migrateObj.LATEST_QUEUE.put(int(part))
        
def latest_parts():
    
    while True:
        part = getQueuItem(migrateObj.LATEST_QUEUE)
        md5_objs = get_md5_list(part)
        for md5_obj in md5_objs:
            if not md5_obj.endswith(MD5_HEAD):
                continue
            md5 = get_obj_md5(md5_obj)
            if md5 not in migrateObj.PULL_MD5_LIST:
                migrateObj.PULL_MD5_LIST.append(md5)
                hostUuid = get_md5_head(get_md5_head_path(part, md5))
                migrateObj.PULL_MD5_QUEUE.put((md5,hostUuid,part)) 
        
    
def transmit_md5s():
    while True:
        md5,hostUuid,part = getQueuItem(migrateObj.PULL_MD5_QUEUE)
        host,port = get_http_addr(hostUuid)
        download_remote_md5(host, port, part, md5)
        delete_remote_md5(host, port, part, md5)
        
