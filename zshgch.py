#!/usr/bin/env python
#-*- coding:utf8 -*-
import sys
user = 'liush'
password = '1234'
num = 0

while True:
    name = raw_input('Please input your name:').strip()
    if name  == user:
        while True:
            if num < 3:
                pw = raw_input('Please input your password:')
                if pw != password:
                    print "Wrong input,try again!"
                    num += 1
                    continue
                else:
                    print "Welcome to login.  %s"%name
                break
            else:
                print "Too many wrong input,exit!!"
                sys.exit()
    else:
        print "There is no %s"%name
        continue
    break
####查询信息#####
while True:
    m = 0
    sch = raw_input('Please input the name whom you want to search:')
    list = file('info.txt')
    while True:
        line = list.readline()
        if len(line) == 0:break
        if sch in line:
            print line,
            m = 1
        else:
            pass
    if m == 0:
        print "There is no %s"%sch
            

    