# -*- coding: utf-8 -*-

import sys
import time
import traceback
from idarea.common.utils import migrate_uuid_will_use,loadMigrateProc
import idarea.migrate.static
from idarea.migrate.static import migrateObj
from idarea.common.wsgi import run_wsgi

from idarea.ring.variable import NODE_UUIDS as MIGRAGE_HOST_LIST
from idarea.migrate.queue.thread import doProcessInitParts,doProcessPastParts,\
    doTransmitParts,doUpgradeParts,doLatestParts,doTransmitMD5s
from idarea.ring.static import MIGRATE_STARTUP_LIST
from idarea.ring.host import get_startup_list

def start():

    startup_list = get_startup_list(MIGRATE_STARTUP_LIST)
    
    try_times = False
    for uuid,ip,port,home in MIGRAGE_HOST_LIST:
        
        if not migrate_uuid_will_use(uuid, ip, int(port)+migrateObj.PORT_ADDITION, home):
            continue
            
        if uuid not in startup_list:
            print 'host uuid not in startup list'
            continue
        
        try_times = True
        break
    
    if not try_times:
        print 'no uuid can be use,exit'
        sys.exit(0) 
            
    loadMigrateProc(uuid, ip, port, home)
    print 'load migrate proc finished'
    print migrateObj.MIGRATE_HOST,migrateObj.MIGRATE_PORT,migrateObj.MIGRATE_UUID

    migrateObj.interruptEvent.clear()

    doProcessInitParts().start()
    doProcessPastParts().start()
    doTransmitParts().start()
    doUpgradeParts().start()
    doLatestParts().start()
    doTransmitMD5s().start()
    
    try:
        run_wsgi(migrateObj.MIGRATE_PASTE_CONF, 
                 migrateObj.MIGRATE_PASTE_APP_SECTION, 
                 migrateObj.MIGRATE_HOST,
                 migrateObj.MIGRATE_PORT)
    except:
        # 已经抛出异常了，但是并非是 KeyboardInterrupt,而是raise出来的
        print traceback.format_exc()
        migrateObj.interruptEvent.set()
    print 'main thread exit'  
 
if __name__ == '__main__':
    start() 
