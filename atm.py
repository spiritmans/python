#!/usr/bin/env python
# -*- coding:utf8 -*-
import sys
import types

user = 'liush'
password = '123456'
num = 0
while True:
    name = raw_input('Please input your name:').strip()
    if name != user:
        print 'Wrong name,try again:'
        continue
    else:
        while True:
            if num < 3:  
                pw = raw_input('Please input your password:').strip()
                if pw != password:
                    print 'Wrong password, please enter again!'
                    num += 1
                    continue
                else:
                    print 'Welcome to login:  %s'%name
                    pass
                break
            else:
                print 'Too many wrong input,exit!!!'
                sys.exit()
    break        