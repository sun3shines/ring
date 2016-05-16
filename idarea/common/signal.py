# -*- coding: utf-8 -*-

import os
import time

from idarea.migrate.static import migrateObj
from idarea.common.utils import SLEEP_INTERVAL
from idarea.common.utils import QUEUE_TIMEOUT_INTERVAL

def signal_handler():
    if migrateObj.interruptEvent.isSet():  
        print 'thread finished'  
        raise KeyboardInterrupt
       
def signal_sleep(seconds):
    
    total = 0
    while total < seconds:
        signal_handler()
        time.sleep(SLEEP_INTERVAL)
        total = total + SLEEP_INTERVAL
        
def getQueuItem(queue):
    
    while True:
        try:
            item = queue.get(timeout=QUEUE_TIMEOUT_INTERVAL)
        except:
            signal_handler()
        else:
            break    
    return item

