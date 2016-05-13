import json
from idarea.common.http import jresponse
from idarea.object.md5st import MSt
from webob import Request, Response
from idarea.migrate.queue.lib import fs_make_part
from idarea.migrate.static import migrateObj
from idarea.ring.variable import CURRENT_RING_SEQ

def doPartTransmit(request):
    
    param = json.loads(request.body)
    part = int(param.get('part')) 
    seq = int(param.get('seq'))
    md5_list = param.get('md5list')
    fs_make_part(part, seq, md5_list)
    
    if seq < CURRENT_RING_SEQ:
        migrateObj.PAST_QUEUE.put((int(part),seq)) 
    else:
        migrateObj.LATEST_QUEUE.put(int(part))
        
    return jresponse('0','',request,200)

def doMergePartList(request):

    # 检查本地part列表中是否有part不存在 partlist中，
    # 若不存在，说明此part 已在源主机中传输完毕了，若文件全为md5.head
    # 则可以删除本地此part了。
    return jresponse('0','',request,200)
