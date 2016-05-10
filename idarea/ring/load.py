# -*- coding: utf-8 -*-

from idarea.ring.utils import get_previous_set

def get_lates_set():
    return get_previous_set()[0]

def load_ring():
    return get_lates_set()
