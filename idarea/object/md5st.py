# -*- coding: utf-8 -*-

import os.path
import os
from idarea.object.static import PROC_DATA_DIR

class MSt:

    def __init__(self,part,md5,seq=0):
        self.prefix = PROC_DATA_DIR
        self.part = part
        self.seq = seq
        self.md5 = md5
        self.readsize = 4096 

    @property
    def path(self):
        return '/'.join([self.prefix,self.part,self.md5])

    @property
    def seq_path(self):
        return '/'.join([self.prefix,self.part,'seq'])
    
    @property
    def parent(self):
        return '/'.join([self.prefix,self.part])
    
    def get(self):
        
        try:
            self.handle = file(self.path,'r')
            while True:
                data = self.handle.read(self.readsize)
                if data:
                    yield data
                else:
                    break
        finally:
            self.handle.close()

    def put(self,fileinput):
        
        if not os.path.exists(self.parent):
            os.mkdir(self.parent)
            with open(self.seq_path,'w') as f:
                f.write(str(self.seq))
                
        with open(self.path,'w') as f:
            while True:
                data = fileinput.read(self.readsize)
                if data:
                    f.write(data)
                else:
                    break

#        input.close()

    @property
    def exists(self):
        
        if not os.path.exists(self.path):
            return False
        return True

# Mst 改造为app_iter 的方式，swift中，读取和写结束后，如何关闭？

if __name__ == '__main__':

    m = MSt(000,'c5371ed9133353622166fe6352b91a56') 
    if m.exists:
        print 'exists'
    else:
        print 'not exists'
        m.put(file('/root/install.log'))

    for data in m.get():
        print data
        print len(data)
