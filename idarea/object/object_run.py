# -*- coding: utf-8 -*-

import sys

from idarea.object.utils import uuid_will_use,loadProc
import idarea.object.static
from idarea.common.wsgi import run_wsgi
from idarea.ring.load import load_ring
LOAD_RING_SET = load_ring()
LOAD_HOST_LIST = LOAD_RING_SET.pop('hostList')

def start():

    hosts = LOAD_HOST_LIST
    
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
    print 'load proc finished'
    print idarea.object.static.PROC_HOST,idarea.object.static.PROC_PORT,idarea.object.static.PROC_UUID
    
    run_wsgi(idarea.object.static.PROC_PASTE_CONF, 
             idarea.object.static.PROC_PASTE_APP_SECTION, 
             idarea.object.static.PROC_HOST,
             idarea.object.static.PROC_PORT)
    
if __name__ == '__main__':
    start()
    
