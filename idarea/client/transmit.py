# -*- coding: utf-8 -*-

import os
import json
from idarea.client.http.task import Task
from idarea.common.urls.migrate import strPartTransmit    
import idarea.client.http.mission as mission


class PartTransmit(Task):
    
    def __init__(self,part,seq,md5_list):
        
        self.part = part
        self.seq = seq
        self.md5_list = md5_list
        
    def getUrl(self):
        return strPartTransmit
    
    def getBody(self):
        return json.dumps({'part':str(self.part),
                           'seq':str(self.seq),
                           'md5list':self.md5_list})
    
def http_transmit_part(part,seq,md5_list,host,port):
    t = PartTransmit(part,seq,md5_list)
    t = mission.execute(t,host=host,port=port)
    print t.response

if __name__ == '__main__':

    pass
#    http_transmit_part(5555,1,{},'127.0.0.1',9134)
