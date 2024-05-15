#!/usr/bin/env python

import sys

# input comes from standard input
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # emit each word with a count of 1
    for word in words:
        print('%s\t%s' % (word, 1))
