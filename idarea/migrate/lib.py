
import os
import shutil
from idarea.migrate.static import migrateObj

def get_part_seq(obj,latest_seq):
    
    path = '/'.join([migrateObj.MIGRATE_DATA_DIR,obj,'seq'])
    if not os.path.exists(path):
        return latest_seq
    
    with open(path,'r') as f:
        seq = int(f.read())
    return seq


def transmit(part):
    
    src = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part)])
    dst = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part)+'.push'])
    print 'transmit part: %s' % (dst)
#    shutil.move(src, dst)

def upgrade(part,seq):
    
    print 'upgrade part: %s %s' % (str(part),str(seq))
#    path = '/'.join([migrateObj.MIGRATE_DATA_DIR,str(part),'seq'])
#    with open(path,'w') as f:
#        f.write(str(seq))
    

