# -*- coding: utf-8 -*-

from idarea.ring.utils import get_previous_set

def get_lates_set():
    ring_set,ring_seq = get_previous_set()
    return ring_set,ring_seq

def proxy_load_ring():
    ring_set,ring_seq = get_lates_set()
    return ring_set,ring_seq

def object_load_ring():
    ring_set,ring_seq = get_lates_set()
    return ring_set
