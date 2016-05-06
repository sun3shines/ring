# -*- coding: utf-8 -*-

import json
from idarea.client.http.task import Task
from idarea.common.urls.proxy import strProxyGet,strProxyPut    
import idarea.client.http.mission as mission
from idarea.common.md5 import md5sum

class FilePut(Task):
    
    def __init__(self,src,md5):
        
        self.src = src
        self.md5 = md5
        
    def getUrl(self):
        return strProxyPut
    
    def getBody(self):
        return file(self.src)
    
    def getHeaders(self):
        return {'md5':self.md5}
        
class FileGet(Task):
    
    def __init__(self,md5):
        self.md5 = md5
    
    def getUrl(self):
        return strProxyGet
    
    def getBody(self):
        return json.dumps({'md5':self.md5})

def putfile(src):
    t = FilePut(src,md5sum(src)) 
    t = mission.execute(t)
    print t.status
    print t.data

def getfile(src):
    t = FileGet(md5sum(src))
    for data in mission.download(t):
        print data
        print len(data)
 
if __name__ == '__main__':
    src = '/root/install.log'
#    putfile(src)
    getfile(src)
 
