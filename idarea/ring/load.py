# -*- coding: utf-8 -*-

from idarea.ring.utils import get_previous_set

def get_lates_set():
    ring_set,ring_seq = get_previous_set()
    return ring_set,ring_seq

def load_ring():
    ring_set,ring_seq = get_lates_set()
    return ring_set,ring_seq

LOAD_RING_SET,CURRENT_RING_SEQ = load_ring()
LOAD_HOST_LIST = LOAD_RING_SET.pop('hostList')
