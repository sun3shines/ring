# -*- coding: utf-8 -*-

import sys

from idarea.common.utils import object_uuid_will_use,loadObjectProc
import idarea.object.static
from idarea.common.wsgi import run_wsgi
from idarea.ring.variable import LOAD_HOST_LIST

def start():

    hosts = LOAD_HOST_LIST
    
    try_times = False
    for uuid,ip,port,home in hosts:
        if not object_uuid_will_use(uuid, ip, port, home):
            continue
        try_times = True
        break
    
    if not try_times:
        print 'no uuid can be use,exit'
        sys.exit(0) 
    
    loadObjectProc(uuid, ip, port, home)
    print 'load object proc finished'
    print idarea.object.static.PROC_HOST,idarea.object.static.PROC_PORT,idarea.object.static.PROC_UUID
    
    run_wsgi(idarea.object.static.PROC_PASTE_CONF, 
             idarea.object.static.PROC_PASTE_APP_SECTION, 
             idarea.object.static.PROC_HOST,
             idarea.object.static.PROC_PORT)
    
if __name__ == '__main__':
    start()
    
