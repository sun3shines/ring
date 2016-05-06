# -*- coding: utf-8 -*-

from idarea.proxy.ring import _PARTITION_POWER,_part2node,_node2uuid

PARTITION_SHIFT = 32 - _PARTITION_POWER
PART2NODE = _part2node()
NODE2UUID = _node2uuid()
HOST_PATH = ''

HOST_PROC_CONF = '/root/workspace1/merge/ring/idarea/proxy/host.conf'