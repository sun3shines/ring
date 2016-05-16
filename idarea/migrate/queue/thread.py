# -*- coding: utf-8 -*-

import threading
from idarea.migrate.queue.identify import process_init_parts,process_past_parts,\
    transmit_parts,upgrade_parts,latest_parts,transmit_md5s

class doProcessInitParts(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        process_init_parts()            
        
class doProcessPastParts(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        process_past_parts()            
        
class doTransmitParts(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        transmit_parts() 
        
class doUpgradeParts(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        upgrade_parts()
        
class doLatestParts(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        latest_parts()
        
class doTransmitMD5s(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        transmit_md5s()
                           