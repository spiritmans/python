#!/usr/bin/env python

import sys
user = "liush"
num = 0

while True:
    if num < 3:
        name = raw_input("please inout your name:").strip()
        if len(name) == 0:
            print "You had not input something,try again!!!"
            continue
        elif name == user:
            print "Welcome to login!"
            break
        else:
            print "You had a wrong input!!"
            num += 1
            continue
        break
    else:
        print "You had too many wrong inout,exit!!!"
        sys.exit()
age = raw_input("How old are you:")
sex = raw_input("Please input your sex:")
dep = raw_input("Which dep:")
message = '''Information of staff:
    Name : %s
    Age  : %s
    Sex  : %s
    Dep  : %s
    ''' %(name, age, sex, dep)
print message

#while True:
#    name = raw_input("please inout your name:").strip()
#    if len(name) == 0:
#        print "You had not input something,try again!!!"
#        continue
#    if name == user:
#        print "Welcome to login!"
#        break
#    for i in range(1,3):
#        name = raw_input("Please input your name:").strip()
#        if name == user:
#            print "Welcome to login!"
#            pass
#        else:
#            print "You had a wrong input!!"
#            continue
#        break
#    else:
#        print "You had too many wrong input,exit!!!"
#        sys.exit()
#    break
#
#age = raw_input("How old are you:")
#sex = raw_input("Please input your sex:")
#dep = raw_input("Which dep:")
#message = '''Information of staff:
#    Name : %s
#    Age  : %s
#    Sex  : %s
#    Dep  : %s
#    ''' %(name, age, sex, dep)
#print message
