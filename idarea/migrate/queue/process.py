# -*- coding: utf-8 -*-

from idarea.migrate.static import migrateObj
from idarea.migrate.queue.lib import get_part_seq,transmit,upgrade

def transmit_parts():
    
    while True:
        part_info = migrateObj.TRANSMIT_QUEUE.get()
        part = part_info[2]
        seq = part_info[4]
        transmit(part,seq)
        
def upgrade_parts():
    
    while True:
        part_info = migrateObj.UPGRADED_QUEUE.get()
        part,upgrade_seq = part_info
        upgrade(part, upgrade_seq)
        migrateObj.LATEST_QUEUE.put(int(part))
        
def latest_parts():
    
    while True:
        part = migrateObj.LATEST_QUEUE.get()
        print 'latest part: %s' %(str(part))
    