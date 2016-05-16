# -*- coding: utf-8 -*-

import json
from idarea.client.http.task import Task
import idarea.client.http.mission as mission

from idarea.common.urls.object import strObjectGet,strObjectPut,strObjectDel
from idarea.common.md5 import md5sum

class ObjectPut(Task):
    
    def __init__(self,part,seq,md5,length,fileinput):
        
        self.part = part
        self.seq = seq
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
                'part_seq':self.seq,
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

class ObjectDel(Task):
    
    def __init__(self,part,md5):
        self.part = part
        self.md5 = md5
    
    def getUrl(self):
        return strObjectDel
    
    def getBody(self):
        return json.dumps({'md5':self.md5,
                           'part':self.part})

def sendfile(host,port,part,seq,md5,length,fileinput):
    
    t = ObjectPut(part,seq,md5,length,fileinput) 
    t = mission.execute(t,host,port)
    print t.response

def recvfile(host,port,part,md5):
    t = ObjectGet(part,md5)
    return mission.download(t, host, port)

def delfile(host,port,part,md5):
    t = ObjectDel(part,md5)
    t = mission.execute(t, host, port)
    print t.response
 
if __name__ == '__main__':
    sendfile('127.0.0.1',9032,500,'eeeeeeeee',file('/root/install.log')) 
