
import os
from idarea.client.file import getfile,putfile

def gettest(filedir):
    for fn in os.listdir(filedir):
        src = '/'.join([filedir,fn])
        getfile(src)
        break

def puttest(filedir):
    for fn in os.listdir(filedir):
        src = '/'.join([filedir,fn])
        putfile(src)

if __name__ == '__main__':

#    puttest('/home/files')
    gettest('/home/files')


