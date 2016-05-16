# -*- coding: utf-8 -*-

from __future__ import with_statement

import traceback
from eventlet import Timeout
from idarea.common.webobx import Request, Response
from idarea.proxy.route import process_request
    
class ServerController(object):

    def __init__(self, conf):
        pass
 
    def __call__(self, env, start_response):
        request = Request(env)
        
        try:
            resp = process_request(request) 
        except (Exception, Timeout):
            print 'ERROR __call__ error with %s %s ' % (request.method,request.path)
            print traceback.format_exc()
            resp = Response() 
                
        return resp(env, start_response)

def app_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    return ServerController(conf)

