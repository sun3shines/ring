# -*- coding: utf-8 -*-

import os
from idarea.migrate.static import migrateObj
from idarea.common.libpart import fs_get_md5_list
from idarea.common.libseq import set_seq
from idarea.common.libmd5 import get_md5_head
from idarea.common.utils import MD5_HEAD
from idarea.client.transmit import http_transmit_part

def transmit(part,seq,host,port):
    
    # 如果网络传输失败，则应该继续放入队列中来处理了
     
    part_dir = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part)])
    # print 'transmit part: %s %s' % (part_dir,str(seq))
    
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
        
    print 'transmit %s %s %s to %s %s' %(str(part),str(seq),str(msg_list),str(host),str(port))
    
    http_transmit_part(part, seq, msg_list,host,port)
    
def upgrade(part,seq):
    
    pass
    # print 'upgrade part: %s %s' % (str(part),str(seq))
    # set_seq(part, seq)

