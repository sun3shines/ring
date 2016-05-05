
import os
import os.path

from idarea.host import getUuids

def get_proc_pid():
    return os.getpid()

def uuid_will_use(uuid,ip,port,home):
    data_dir = '/'.join([home,uuid])
    proc_pid = '/'.join(data_dir,'.pid')
    if not os.path.exists(data_dir):
        return True
    
    if not os.path.exists(proc_pid):
        return True

    pid = file(proc_pid).read().strip()
    
def start():
    
    current_pid = get_proc_pid()
    
    hosts = getUuids()
    for uuid,ip,port,home in hosts:
        data_dir = '/'.join([home,uuid])
        proc_pid = '/'.join(data_dir,'.pid')
        if not os.path.exists(proc_pid):
            pass
         
         
    pass


if __name__ == '__main__':
    start()
    