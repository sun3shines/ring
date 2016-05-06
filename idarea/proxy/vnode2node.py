# -*- coding: utf-8 -*-

from struct import unpack_from
from hashlib import md5
from bisect import bisect_left

def test():
    old_node_count = 100
    new_node_count = 101

    vnode_count = 1000

    old_vnode2node = []

    data_count = 10000000
    vnode_range_starts = []

    for vnode in xrange(vnode_count):

        old_vnode2node.append(vnode % old_node_count)
        vnode_range_starts.append(data_count/vnode_count * vnode)

    new_vnode2node = list(old_vnode2node)

    vnodes_to_reassign = vnode_count / new_node_count
    while vnodes_to_reassign > 0:
        for node_to_take_from in xrange(old_node_count):
            for vnode_id,node_id in enumerate(new_vnode2node):
                if node_id == node_to_take_from:
                    new_vnode2node[vnode_id] = 101
                    vnodes_to_reassign -= 1
                    if vnodes_to_reassign <= 0:
                        break
            if vnodes_to_reassign <= 0:
                break

    moved_data_count = 0
    for data_id in xrange(data_count):
        hsh = unpack_from('>I',md5(str(data_id)).digest())[0]
#        vnode_id = hsh % vnode_count
        vnode_id = bisect_left(vnode_range_starts,hsh % data_count) % vnode_count
        old_node = old_vnode2node[vnode_id]
        new_node = new_vnode2node[vnode_id]

        if old_node != new_node:
            moved_data_count = moved_data_count + 1
    print moved_data_count
    print 100.0 * moved_data_count / data_count

if __name__ == '__main__':
    test()

