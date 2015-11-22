#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
user = 'liush'
password = '1234'
num = 0

while True:
    name = raw_input('Please input your name:').strip()
    if name == user:
        while True:
            if num < 3:
                pw = raw_input('Please input the password:')
                if pw == password:
                    print "Welcome to login. %s"%(name)                    
                    while True:
                        m = 0
                        sch = raw_input('Please input the name whom you want to search:').strip()
                        list = file('info.txt')
                        #循环打印所有包含查询字符的項目
                        while True:                     
                            line = list.readline()
                            if len(line) == 0:break         #line为空时，跳出循环
                            if sch in line:
                                print line,
                                m = 1
                            else:
                                pass  
                        if m == 0:print "There is no info for %s" %sch
                else:
                    num += 1
                    continue
            else:
                print "You had too many wrong input,exit!"
                sys.exit()
    else:
            continue
    break
