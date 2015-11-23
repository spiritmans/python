#!/usr/bin/env python
#-*- coding:utf8 -*-
import sys
import os
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
                    print '''There are six mode for you:
1.search
2.add
3.delete
4.modify
5.insert
0.exit'''
                break
            else:
                print "Too many wrong input,exit!!"
                sys.exit()
    else:
        print "There is no %s"%name
        continue
    break
######################################
while True:
    select = raw_input('Please input your choice:1/2/3/4/5/0/ ').strip()
    if len(select) == 0:continue
    if select == '0':
        sys.exit()
    elif select == '1':
        while True:
            match = 0
            info = file('info.txt')
            sch = raw_input("Please input sth that you want to search(The exit/quit for exit):")
            if sch == 'exit' or sch == 'quit':break
            while True:
                line = info.readline()
                if len(line) == 0:break
                if sch in line:
                    print line,
                    info.close()
                    match = 1
                else:
                    pass
            if match == 0:
                print "There is no informations for %s" %sch
    elif select == '2':
        while True:
            print '''Add format:
            num     name    dep     tel'''
            add = raw_input("Please input sth that you want to add(The exit/quit for exit):")
            if len(add) == 0:continue
            if add == 'exit' or add == 'quit':break
            info == file('info.txt','a')
            info.write('%s\n' %(add))
            info.close()
    elif select == '3':
        while True:
            os.system('cat info.txt')
            delete = raw_input('Please input the name whom you want to delete(The exit/quit for exit):').strip()
            if delete == 'exit' or delete == 'quit':break
            if len(delete) == 0:continue
            info = file('info.txt')
            list = info.readlines()
            if 
                new = ""
                for line in list:
                    if delete not in line:
                        new = new + line
                info.close()
                info = file('info.txt','w')
                info.write(new)
                info.close()
            else:
                print "There is no %s"%delete
    elif select == '4':
        while True:
            os.system('cat info.txt')
            name = raw_input("Please input the name whom you want to change(The exit/quit for exit):").strip()
            if len(name) == 0:continue
            fi name == 'exit' or name == 'quit':break
            mod = raw_input("Please input your choice:num/name/dep/tel/exit/").strip()
            info = file('info.txt')
            list = info.readlines()
            if mod =='exit':break
            if len(mod) == 0:continue
            if mod == 'num':
                num = raw_input("Please input your num:")
                new = ""
                for line in list:
                    x = line.split()
                    if name == x[1]:
                        x[0] = num
                        new = new + '\t'.join(x) + '\n'
                    else:
                        new = new + line
                print new
            info.close()
            info = file('info.txt','w')
            info.write(new)
            info.close()


            elif option == 'name':
            elif option == 'dep':
            elif option == 'tel':
            print new
            info.close()
            info = file('info.txt','w')
            info.write(new)
            info.close()




















            

#    elif select == '5':
        
    
    