# -*- coding: utf-8 -*-

import sys
from idarea.common.utils import migrate_uuid_will_use,loadMigrateProc
import idarea.migrate.static
from idarea.migrate.static import PORT_ADDITION
from idarea.common.wsgi import run_wsgi

from idarea.ring.variable import NODE_UUIDS as MIGRAGE_HOST_LIST
from idarea.migrate.identify import get_not_latest_parts

def start():

    import pdb;pdb.set_trace()
    pass
    try_times = False
    for uuid,ip,port,home in MIGRAGE_HOST_LIST:
        
        if not migrate_uuid_will_use(uuid, ip, int(port)+PORT_ADDITION, home):
            continue
        try_times = True
        break
    
    if not try_times:
        print 'no uuid can be use,exit'
        sys.exit(0) 
    
    loadMigrateProc(uuid, ip, port, home)
    print 'load migrate proc finished'
    print idarea.migrate.static.MIGRATE_HOST,idarea.migrate.static.MIGRATE_PORT,idarea.migrate.static.MIGRATE_UUID

    print get_not_latest_parts()
        
    # run_wsgi(idarea.migrate.static.MIGRATE_PASTE_CONF, 
    #          idarea.migrate.static.MIGRATE_PASTE_APP_SECTION, 
    #          idarea.migrate.static.MIGRATE_HOST,
    #          idarea.migrate.static.MIGRATE_PORT)
   
if __name__ == '__main__':
    start() 
