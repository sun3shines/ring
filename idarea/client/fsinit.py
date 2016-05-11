
import os
def delete_objects(path):
    
    dirs = []
    with open(path,'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('#'):
                continue
            if not line.strip():
                continue
            line_list = line.strip().split(',')
            if 4 != len(line_list):
                continue
            
            dirs.append('/'.join([line_list[3],line_list[0]]))
            
    for nodedir in dirs:
        print nodedir
        cmd = 'rm -rf %s/*' % (nodedir)
        os.system(cmd)
 
if __name__ == '__main__':
    delete_objects('/usr/lib/python2.6/site-packages/idarea/ring/host.conf')
            
