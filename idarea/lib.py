# -*- coding: utf-8 -*-

import os.path
import psutil
import idarea.static 

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
    if not proc_exists(pid, idarea.static.PROC_CMDLINE):
        return True
    
    return False

def get_pid_cmdline(pid):
    
    # 采用psutil吧，是的。
    try:
        pr = psutil.Process(pid)
    except:
        return ''
    
    return ' '.join(pr.cmdline())
    
def proc_exists(pid,cmdline):
    
    if cmdline == get_pid_cmdline(pid):
        return True
    return False

def loadProc(uuid, ip, port, home):

    currentpid = get_proc_pid()
    
    data_dir = '/'.join([home,uuid])
    proc_pid = '/'.join(data_dir,'.pid')
    
    idarea.static.PROC_DATA_DIR = data_dir
    idarea.static.PROC_HOST = ip
    idarea.static.PROC_PORT = port
    idarea.static.PROC_UUID = uuid
    
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    
    with open(proc_pid,'w') as f:
        f.write(str(currentpid))
            
    
