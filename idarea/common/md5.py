
import hashlib

def md5sum(path):
    m = hashlib.md5()  
    with file(path) as f: 
        bytes = f.read(1024)  
        while(bytes != b''):  
            m.update(bytes)  
            bytes = f.read(1024)   
        f.close()  
          
        md5value = m.hexdigest() 
        return md5value

if __name__ == '__main__': 

    print md5sum('/root/install.log')
