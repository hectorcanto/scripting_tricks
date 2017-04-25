#!/usr/bin/env python
"""
This example illustrates the use of pickle to save some variable in disk to
avoid repeating a certain step that takes a lot of time.

This way, if the step was already done, you skip it, and load the results
directly from disk.

This is very useful when developing a process in two steps, so once you finish
the first step you can test the second without having to repeat the first once
every time.

Try the script twice, and you will see that the second time the first step
is skippend, and the varibale reloaded from memmory

Pickle is a library to serialize Python objects, meaning, convert them
into a binary or byte-like stream. In this case, we use it to save data to
disk, but can be used to send it to another process or another machine.

More info about _pickle_ in:
https://docs.python.org/2/library/pickle.html
https://docs.python.org/3/library/pickle.html
"""

import os
import pickle
from aux import do_hard_stuff, do_another_hard_thing

filename = "object.pickle"

# Step 1: the hard process
# Delete the pickle file if you want to run step 1 from scratch

if not os.path.exists(filename): # Run the step and save it to filename
    print "Running step 1"
    results = do_hard_stuff() # Replace
    with open(filename, "w") as write_buffer:
        # Do not use "buffer" as variable, is a reserved word
        pickle.dump(results, write_buffer)

else:  # Load the variable from disk
    print "Loading old results"
    with open(filename, "r") as read_buffer:
        results = pickle.load(read_buffer)

# Step 2: use step 1 results the way you want
print "Running step 2"
do_another_hard_thing(results)
