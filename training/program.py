#!/usr/bin/env python2

from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def oprint(*args, **kwargs):
    print(*args, file=sys.stdout, **kwargs)

oprint("This line is regular output to STDOUT")
eprint("This line is an error to STDERR")
