# -*- coding: utf-8 -*-

from httplib import HTTPConnection
import urllib
import json

from idarea.client.http.static import SERVER_HTTP_HOST,SERVER_HTTP_PORT,SERVER_HTTP_TIMEOUT

class Mission:
    
    def __init__(self,host,port,timeout):
        
        self.host= host
        self.port = int(port)
        self.conn = None
        self.connection_flag = False
        self.readsize = 4096
 
        self.timeout = 1000
        
    def __enter__(self):
        self.connect()
        return self 
  
    def getHttpsConn(self):
        
        return HTTPConnection(self.host,self.port,True,self.timeout)  

    def connect(self):
        
        if not self.connection_flag:
            self.conn = self.getHttpsConn()
            self.connection_flag = True
    
    def close(self):
        
        if self.connection_flag:
            self.conn.close()
            self.connection_flag = False
            
    def __exit__(self,type,value,trace):
        self.close()
         
    def http(self,t):

        self.connect()
        
        url = t.getUrl()
        ps = t.getParams() 
        if ps:
            url = url + '?' + urllib.urlencode(ps)
        headers = t.getHeaders()
        try:
            self.conn.request(t.getMethod(),url,t.getBody(),headers)
        except:
            t.response = {'status':'-1','msg':'connected refused'}
            return t

        resp = self.conn.getresponse()
        t.status = resp.status
        t.data = resp.read()
        t.headers = {}
        for item in resp.getheaders():
            t.headers[item[0]] = item[1]
            
        if 2==t.status/100:
            if t.data:
                try:
                    msg = json.loads(t.data)
                    if type([]) == type(msg):
                        t.response = {'status':'0','msg':msg}
                    elif type({}) == type(msg) and msg.has_key('status'):
                        t.response = json.loads(t.data)
                    else:
                        t.response = {'status':'0','msg':t.data} 
                except:
                    t.response = {'status':'0','msg':t.data} 
            else:
                t.response = {'status':'0','msg':t.data}
        else:
            try:
                msg = json.loads(t.data)
                t.response = msg
            except:
                t.response = {'status':'-1','msg':t.data}
                       
        self.close()
 
        return t


    def download(self,t):
        try:
            self.connect()
  
            url = t.getUrl()
            ps = t.getParams()
            if ps:
                url = url + '?' + urllib.urlencode(ps)

            headers = t.getHeaders()
           
            self.conn.request(t.getMethod(),url,t.getBody(),headers)

            resp = self.conn.getresponse()
            while True:
                data = resp.read(self.readsize)
                if data:
                    yield data 
                else:
                    break
        finally:
            self.close()

def getMission(host,port):

    return Mission(host,port,SERVER_HTTP_TIMEOUT)

def execute(t,host=SERVER_HTTP_HOST,port=SERVER_HTTP_PORT):
    
    with getMission(host,port) as m:
        m.http(t)
    
    return t 

def download(t,host=SERVER_HTTP_HOST,port=SERVER_HTTP_PORT):
    m = getMission(host,port)
    return m.download(t)

