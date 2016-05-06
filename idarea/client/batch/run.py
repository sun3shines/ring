
from idarea.common.uuid import get_vs_uuid

def create_files():
    i = 0
    while i< 100:
        uuid = get_vs_uuid()
        path = 'files/file_'+str(uuid)
        file(path,'w').write(uuid)
        i = i+1
    pass

if __name__ == '__main__':
    create_files()


