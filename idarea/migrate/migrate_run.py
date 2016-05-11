# -*- coding: utf-8 -*-

import sys
from idarea.common.utils import migrate_uuid_will_use,loadMigrateProc
import idarea.migrate.static
from idarea.migrate.static import migrateObj
from idarea.common.wsgi import run_wsgi

from idarea.ring.variable import NODE_UUIDS as MIGRAGE_HOST_LIST
from idarea.migrate.identify import process_init_parts,process_past_parts

def start():

    pass
    try_times = False
    for uuid,ip,port,home in MIGRAGE_HOST_LIST:
        
        if not migrate_uuid_will_use(uuid, ip, int(port)+migrateObj.PORT_ADDITION, home):
            continue
        try_times = True
        break
    
    if not try_times:
        print 'no uuid can be use,exit'
        sys.exit(0) 
    
    loadMigrateProc(uuid, ip, port, home)
    print 'load migrate proc finished'
    print migrateObj.MIGRATE_HOST,migrateObj.MIGRATE_PORT,migrateObj.MIGRATE_UUID
    import pdb;pdb.set_trace()

    process_init_parts()
    process_past_parts()
    
    import pdb;pdb.set_trace()
    pass    
    # run_wsgi(migrateObj.MIGRATE_PASTE_CONF, 
    #          migrateObj.MIGRATE_PASTE_APP_SECTION, 
    #          migrateObj.MIGRATE_HOST,
    #          migrateObj.MIGRATE_PORT)
   
if __name__ == '__main__':
    start() 
