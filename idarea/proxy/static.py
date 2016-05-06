# -*- coding: utf-8 -*-

from idarea.proxy.ring.partition import _PARTITION_POWER,_part2node,_node2uuid

PARTITION_SHIFT = 32 - _PARTITION_POWER
PART2NODE = _part2node()
NODE2UUID = _node2uuid()
HOST_PATH = ''

PROC_HOST = '127.0.0.1'
PROC_PORT = 9030

PROC_PASTE_CONF = '/usr/lib/python2.6/site-packages/idarea/proxy/proxy.conf'
PROC_PASTE_APP_SECTION = 'proxy'
