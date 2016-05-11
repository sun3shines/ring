# -*- coding: utf-8 -*-

from idarea.ring.static import _PARTITION_POWER

PARTITION_SHIFT = 32 - _PARTITION_POWER

PROC_HOST = '127.0.0.1'
PROC_PORT = 9030

PROC_PASTE_CONF = '/usr/lib/python2.6/site-packages/idarea/proxy/proxy.conf'
PROC_PASTE_APP_SECTION = 'proxy'

CURRENT_RING_SET_SEQ = -1