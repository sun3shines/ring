# -*- coding: utf-8 -*-

import sys
from idarea.host import getUuids
from idarea.lib import uuid_will_use,loadProc
import idarea.static
from idarea.wsgi import run_wsgi

def start():
    
    hosts = getUuids()
    try_times = False
    for uuid,ip,port,home in hosts:
        if not uuid_will_use(uuid, ip, port, home):
            continue
        try_times = True
        
    if not try_times:
        print 'no uuid can be use,exit'
        sys.exit(0) 
    
    loadProc(uuid, ip, port, home)

    run_wsgi(idarea.static.PROC_PASTE_CONF, 
             idarea.static.PROC_PASTE_APP_SECTION, 
             idarea.static.PROC_HOST,
             idarea.static.PROC_PORT)
    
if __name__ == '__main__':
    start()
    
