# -*- coding: utf-8 -*-

from idarea.migrate.static import migrateObj
from idarea.migrate.lib import get_part_seq,transmit,upgrade

def transmit_parts():
    
    for part_info in migrateObj.TRANSMIT_PARTS:
        part = part_info[2]
        transmit(part)
        
def upgrade_parts():
    
    for part_info in migrateObj.UPGRADED_PARTS:
        part,upgrade_seq = part_info
        upgrade(part, upgrade_seq)
        