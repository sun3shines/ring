# -*- coding: utf-8 -*-

from idarea.migrate.static import migrateObj
from idarea.common.libpart import fs_get_part_list,fs_get_md5_list
from idarea.common.libseq import get_seq
from idarea.common.libmd5 import get_md5_head
from idarea.common.utils import MD5_HEAD,MD5_TEMP
from idarea.common.signal import signal_handler,signal_sleep

def mirror_init():

    part_objs = fs_get_part_list()
    for part_obj in part_objs:
        
        seq = get_seq(int(part_obj))
        migrateObj.mirror.append_part(part_obj,seq)
        md5_ojbs = fs_get_md5_list(int(part_obj))
        for md5_obj in md5_ojbs:
            if md5_obj.endswith(MD5_HEAD):
                md5_obj_path = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part_obj),md5_obj])
                hostUuid = get_md5_head(md5_obj_path)
            else:
                hostUuid = migrateObj.MIGRATE_UUID
            migrateObj.mirror.append_md5(md5_obj, hostUuid, part_obj)
        