# -*- coding: utf-8 -*-

from idarea.ring.utils import get_all_ring_set

class migrate_global:
    def __init__(self):
        self.PROC_CMDLINE = 'python migrate_run.py'
        
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
        
        self.PAST_PARTS = []
        self.TRANSMIT_PARTS = []
        self.UPGRADED_PARTS = []
        self.LATEST_PARTS = []
        
migrateObj = migrate_global()