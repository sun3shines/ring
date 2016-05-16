# -*- coding: utf-8 -*-

import threading

class Mirror:
    
    def __init__(self):
        
        self.mirror_parts = []
        self.mirror_md5s = {}
        self.aux_parts = {}

        self.latest_part_index = 0
        
        self.lock = threading.Lock()
        
    def append_part(self,part,seq):
        
        part_key = str(part)
        
        val = {'part':int(part),'seq':seq}
        if self.lock.acquire():
            if self.aux_parts.has_key(part_key):
                pass
            else: 
                self.mirror_parts.append(val)
                self.mirror_md5s.update({part_key:{}})
                self.aux_parts.update({part_key:self.latest_part_index})
                self.latest_part_index = self.latest_part_index + 1
            self.lock.release()
            
    def append_md5(self,md5,hostUuid,part):
        
        part_key = str(part)
        if self.lock.acquire():
            md5_list = self.mirror_md5s.get(part_key) 
            if md5_list.has_key(md5):
                pass
            else:
                key = md5
                val = {'hostUuid':hostUuid}
                md5_list.update({key:val})
            self.lock.release()

            