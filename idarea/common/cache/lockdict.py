# -*- coding: utf-8 -*-

from idarea.common.cache.base import Base

class Mydict(Base):
    
    def put(self,key,val):
        return self.putd(key, val)
    
    def has_key(self,key):
        return self.dhas_val(key)