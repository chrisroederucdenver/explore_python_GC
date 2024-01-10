# A very simple set of python scripts to monkey around with garbage collection in Python.
The exploration started with Dave having memory trouble with various dataframe implementations and garbage collectors.  So far I've found that GC in Python is clearly different than in Java. At this point I'm looking at the different numbers you can pull from the system to see what's going on in the memory structures.

This is a work in progress!

-make_data.py makes a big 100k line CSV file to read into a Pandas dataframe to consume memory
-demo.py is some code I lifted from one of the links in test.py
-test.py is my code adapted from Dave Bunten's
