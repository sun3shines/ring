# -*- coding: utf-8 -*-

import os.path
import psutil
import idarea.object.static 

from idarea.migrate.static import migrateObj

MIGRATE_SUFFIX = 'migratepid'
OBJECT_SUFFIX = 'objectpid'


def get_proc_pid():
    return os.getpid()

def get_pid_cmdline(pid):
    
    # 采用psutil吧，是的。
    try:
        pr = psutil.Process(int(pid))
    except:
        return ''
    
    return ' '.join(pr.cmdline)
    
def proc_exists(pid,cmdline):
    
    if cmdline == get_pid_cmdline(pid):
        return True
    return False

def uuid_will_use(uuid,ip,port,home,suffix,cmdline):
    
    data_dir = '/'.join([home,uuid])
    proc_pid = '/'.join([data_dir,suffix])
    if not os.path.exists(data_dir):
        return True
    
    if not os.path.exists(proc_pid):
        return True

    pid = file(proc_pid).read().strip()
    if not proc_exists(pid, cmdline):
        return True
    
    return False

def object_uuid_will_use(uuid,ip,port,home):
    
    return uuid_will_use(uuid, ip, port, home,OBJECT_SUFFIX,
                         idarea.object.static.PROC_CMDLINE)

def migrate_uuid_will_use(uuid,ip,port,home):
    
    return uuid_will_use(uuid, ip, port, home, MIGRATE_SUFFIX,
                         migrateObj.PROC_CMDLINE)
    
def loadProc(uuid, ip, port, home,suffix):

    currentpid = get_proc_pid()
    
    data_dir = '/'.join([home,uuid])
    proc_pid = '/'.join([data_dir,suffix])
    
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    
    with open(proc_pid,'w') as f:
        f.write(str(currentpid))
            

def loadObjectProc(uuid, ip, port, home):
    
    data_dir = '/'.join([home,uuid])
    idarea.object.static.PROC_DATA_DIR = data_dir
    idarea.object.static.PROC_HOST = ip
    idarea.object.static.PROC_PORT = int(port)
    idarea.object.static.PROC_UUID = uuid
    
    loadProc(uuid, ip, port, home,OBJECT_SUFFIX)
    
def loadMigrateProc(uuid, ip, port, home):
    
    data_dir = '/'.join([home,uuid])
    migrateObj.MIGRATE_DATA_DIR = data_dir
    migrateObj.MIGRATE_HOST = ip
    migrateObj.MIGRATE_PORT = int(port) + migrateObj.PORT_ADDITION
    migrateObj.MIGRATE_UUID = uuid
    
    loadProc(uuid, ip, port, home,MIGRATE_SUFFIX)
    