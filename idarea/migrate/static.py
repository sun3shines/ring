# -*- coding: utf-8 -*-

from idarea.ring.utils import get_all_ring_set
import Queue
import threading
from idarea.common.cache.locklist import Mylist
from idarea.mirror.mirror import Mirror

class migrate_global:
    def __init__(self):
        self.PROC_CMDLINE = 'python migrate_run.py migrate.conf'
        
        self.MIGRATE_DATA_DIR = ''
        self.MIGRATE_HOST = ''
        self.MIGRATE_PORT = ''
        self.MIGRATE_UUID = ''
        
        self.MIGRATE_PASTE_CONF = '/usr/lib/python2.6/site-packages/idarea/migrate/migrate.conf'
        self.MIGRATE_PASTE_APP_SECTION = 'migrate'
        
        self.PULL_SUFFIX = '.pull'
        self.PUSH_SUFFIX = '.push'
        
        self.PORT_ADDITION = 100
        self.ALL_RING_SET = get_all_ring_set()
        
        self.PAST_QUEUE = Queue.Queue()
        self.TRANSMIT_QUEUE = Queue.Queue()
        self.UPGRADED_QUEUE = Queue.Queue()
        self.LATEST_QUEUE = Queue.Queue()
        
        self.PROCESS_PART_OBJS = Mylist()
        
        self.interruptEvent = threading.Event()
       
        self.mirror = Mirror()
        
migrateObj = migrate_global()
