#!/usr/bin/env python

import fileinput

for line in fileinput.input('user.txt',inplace=1):
    line = line.replace('004','005')
    print line,
    