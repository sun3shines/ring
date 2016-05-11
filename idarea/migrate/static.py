# -*- coding: utf-8 -*-

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
        
migrateObj = migrate_global()