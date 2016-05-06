# -*- coding: utf-8 -*-

from idarea.ring import _PARTITION_POWER,_part2node,_node2uuid

PARTITION_SHIFT = 32 - _PARTITION_POWER
PART2NODE = _part2node()
NODE2UUID = _node2uuid()
HOST_PATH = ''

PROC_CMDLINE = 'python proc.py'

PROC_DATA_DIR = ''
PROC_HOST = ''
PROC_PORT = ''
PROC_UUID = ''

PROC_PASTE_CONF = 'paste.conf'
PROC_PASTE_APP_SECTION = 'ringproc'