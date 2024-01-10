#!/usr/bin/env python3

"""
Module for testing Python garbage collection with customized callbacks.
https://medium.com/@josephosoo/garbage-collection-as-a-memory-management-technique-in-python-5f3ee57c7e07
https://rushter.com/blog/python-garbage-collector/
"""
import sys
import gc
import pandas as pd
# pylint: disable=R0801

gc.set_debug(gc.DEBUG_SAVEALL)
print(f"GC Threshold: {gc.get_threshold()}")

# GC callbacks for a view into the process
def info_callback(phase, info):
    """
    Leverage gc.callbacks to show collection start and stop along with info
    see: https://docs.python.org/3/library/gc.html#gc.callbacks
    """
    if phase == "start":
        print("Garbage collection started. Info: ", info, sep="\n", end="\n\n")

    elif phase == "stop":
        print("Garbage collection stopped. Info: ", info, sep="\n", end="\n\n")

###gc.callbacks.append(info_callback)

df_list = []

# Report Initial State
print(f"Initial GC Generations: {gc.get_count()}")
print(f"refcounts {sys.getrefcount(df_list)}")
print(len(gc.get_objects(generation=0)))
print(len(gc.get_objects(generation=1)))
print(len(gc.get_objects(generation=2)))

# Consume Memory
for i in range(100):
    df_list.append(pd.read_csv("test100.csv"))

print(f"After consuming GC Generations: {gc.get_count()}")
print(f"\nrefcounts {sys.getrefcount(df_list)}")
print(len(gc.get_objects(generation=0)))
print(len(gc.get_objects(generation=1)))
print(len(gc.get_objects(generation=2)))

# Consume and Abandon Memory
df_list = None

# Report State
print(f"\nAfter None  GC Generations: {gc.get_count()}")
print(f"refcounts {sys.getrefcount(df_list)}")
print(len(gc.get_objects(generation=0)))
print(len(gc.get_objects(generation=1)))
print(len(gc.get_objects(generation=2)))

# Collect Garbage and Report
collected = gc.collect()
print(f"\nGC collected: {collected}")
print(f"Cleaned GC Generations: {gc.get_count()}")
print(f"refcounts {sys.getrefcount(df_list)}")
print(len(gc.get_objects(generation=0)))
print(len(gc.get_objects(generation=1)))
print(len(gc.get_objects(generation=2)))
print("\n")
