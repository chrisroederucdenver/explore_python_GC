#!/usr/bin/env python3

import gc

gc.set_debug(gc.DEBUG_SAVEALL)

print(f"BEFORE: {gc.get_count()}")
lst = []
lst.append(lst)
list_id = id(lst)

print(f"DURING: {gc.get_count()}")

del lst
print(f"DEL: {gc.get_count()}")
gc.collect()
print(f"after COLLECT: {gc.get_count()}")

print(gc.get_count())
for item in gc.garbage:
    print(item)
    assert list_id == id(item)

