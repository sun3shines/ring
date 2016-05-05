
def getUuids():
    
    uuid_list = []
    with open('host.conf') as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            info = line.split(',')
            if len(info) != 4:
                continue
            uuid_list.append(tuple(info))
    return uuid_list


