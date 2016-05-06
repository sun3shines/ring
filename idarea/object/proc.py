# -*- coding: utf-8 -*-

import sys
from idarea.host import getUuids
from idarea.object.utils import uuid_will_use,loadProc
import idarea.object.static
from idarea.common.wsgi import run_wsgi

def start():

    hosts = getUuids()
    try_times = False
    for uuid,ip,port,home in hosts:
        if not uuid_will_use(uuid, ip, port, home):
            continue
        try_times = True
        break
    
    if not try_times:
        print 'no uuid can be use,exit'
        sys.exit(0) 
    
    loadProc(uuid, ip, port, home)
    
    print idarea.object.static.PROC_HOST,idarea.object.static.PROC_PORT,idarea.object.static.PROC_UUID
    
    run_wsgi(idarea.object.static.PROC_PASTE_CONF, 
             idarea.object.static.PROC_PASTE_APP_SECTION, 
             idarea.object.static.PROC_HOST,
             idarea.object.static.PROC_PORT)
    
if __name__ == '__main__':
    start()
    
