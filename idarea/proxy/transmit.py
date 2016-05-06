# -*- coding: utf-8 -*-

import json
from idarea.client.http.task import Task
import idarea.client.http.mission as mission

from idarea.common.urls.object import strObjectGet,strObjectPut    
from idarea.common.md5 import md5sum

class ObjectPut(Task):
    
    def __init__(self,part,md5,length,fileinput):
        
        self.part = part
        self.md5 = md5
        self.length = length
        self.fileinput = fileinput
         
    def getUrl(self):
        return strObjectPut
    
    def getBody(self):
        return self.fileinput
    
    def getHeaders(self):
        return {'md5':self.md5,
                'part':self.part,
                'Content-Length':self.length}
        
class ObjectGet(Task):
    
    def __init__(self,part,md5):
        self.part = part
        self.md5 = md5
    
    def getUrl(self):
        return strObjectGet
    
    def getBody(self):
        return json.dumps({'md5':self.md5,
                           'part':self.part})

def sendfile(host,port,part,md5,length,fileinput):
    
    t = ObjectPut(part,md5,length,fileinput) 
    t = mission.execute(t,host,port)
    print t.status
    print t.data

def recvfile(host,port,part,md5):
    t = ObjectGet(part,md5)
    return mission.download(t, host, port)

if __name__ == '__main__':
    sendfile('127.0.0.1',9032,500,'eeeeeeeee',file('/root/install.log')) 
