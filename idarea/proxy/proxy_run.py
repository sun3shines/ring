# -*- coding: utf-8 -*-

import idarea.proxy.static
from idarea.common.wsgi import run_wsgi

def start():

    print idarea.proxy.static.PROC_HOST,idarea.proxy.static.PROC_PORT
    
    run_wsgi(idarea.proxy.static.PROC_PASTE_CONF, 
             idarea.proxy.static.PROC_PASTE_APP_SECTION, 
             idarea.proxy.static.PROC_HOST,
             idarea.proxy.static.PROC_PORT)
    
if __name__ == '__main__':
    start()
    
