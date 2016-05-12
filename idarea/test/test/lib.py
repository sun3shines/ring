
import os
import shutil
from idarea.migrate.static import migrateObj
from idarea.common.utils import PART_SEQ

def get_part_seq(obj,latest_seq):
    
    path = '/'.join([migrateObj.MIGRATE_DATA_DIR,obj,PART_SEQ])
    if not os.path.exists(path):
        return latest_seq
    
    with open(path,'r') as f:
        seq = int(f.read())
    return seq


def transmit(part,seq):
    
    src = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part)])
    dst = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part)+'.push'])
    print 'transmit part: %s %s' % (dst,str(seq))
#    shutil.move(src, dst)

def upgrade(part,seq):
    
    print 'upgrade part: %s %s' % (str(part),str(seq))
#    path = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part),PART_SEQ])
#    with open(path,'w') as f:
#        f.write(str(seq))
    

