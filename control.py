#!/usr/bin/env python

import sys
user="liush"
num = 0
while True:
    if num < 3:
        name = raw_input("Please input your name:").strip()
        if len(name) == 0:
            print "you had not input something,try again!"
            continue
        elif name == user:
            print "Welcome to login."#pass
        else:
            print "You had a wrong inout!!"
            num += 1
            continue
        break
    else:
        sys.exit()
        