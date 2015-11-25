#!/usr/bin/env python
#-*- coding:utf8 -*-
import sys
import os
user = 'liush'
password = '1234'
num = 0

while True:
    name = raw_input('\033[34mPlease input your name:\033[0m').strip()
    if name  == user:
        while True:
            if num < 3:
                pw = raw_input('\033[34mPlease input your password:\033[0m')
                if pw != password:
                    print "\033[31mWrong input,try again!\033[0m"
                    num += 1
                    continue
                else:
                    print "\033[32mWelcome to login. %s\033[0m"%name
                    while True:
                        print '''\033[35mThere are 5 mode for you:
                        1.search
                        2.add
                        3.delete
                        4.modify
                        0.exit\033[0m'''
                        select = raw_input('\033[33mPlease input your choice:1/2/3/4/0/ \033[0m').strip()
                        if len(select) == 0:continue
                        if select == '0':
                            sys.exit()
                        elif select == '1':
                            while True:
                                match = 0
                                info = file('info.txt')
                                sch = raw_input("\033[32mPlease input sth that you want to search(The exit/quit for return):\033[0m")
                                if sch == 'exit' or sch == 'quit':break
                                if len(sch) == 0:continue
                                while True:
                                    line = info.readline()
                                    if len(line) == 0:break
                                    if sch in line:
                                        print line,
                                        match = 1
                                    else:
                                        pass
                                if match == 0:
                                    print "\033[31mThere is no informations for %s\033[0m" %sch
                        elif select == '2':
                            while True:
                                print '''Add format:num     name    dep     tel'''
                                add = raw_input("\033[32mPlease input sth that you want to add(The exit/quit for return):\033[0m")
                                if len(add) == 0:continue
                                if add == 'exit' or add == 'quit':break
                                info = file('info.txt','a')
                                info.write('%s\n' %(add))
                                info.close()
                        elif select == '3':
                            while True:
                                os.system('cat info.txt')
                                name = raw_input('\033[32mPlease input name whom you want to delete(The exit/quit for exit):\033[0m').strip()
                                if name == 'exit' or name == 'quit':break
                                if len(name) == 0:continue
                                info = file('info.txt')
                                list = info.readlines()
                                m = 0
                                new = ""
                                for line in list:
                                    x = line.split()
                                    if name == x[1]:
                                        print x
                                        m = 1
                                        pass
                                    else:
                                        new = new + line
                                if m == 0:print "\033[31mWrong name,try aging!\033[0m"
                                info.close()
                                info = file('info.txt','w')
                                info.write(new)
                                info.close()
                        elif select == '4':
                            while True:
                                os.system('cat info.txt')
                                info = file('info.txt')
                                list = info.readlines()
                                name = raw_input("\033[32mPlease input the name whom you want to change(The exit/quit for exit):\033[0m").strip()
                                if len(name) == 0:continue
                                if name == 'exit' or name == 'quit':break
                                m = 0
                                for line in list:
                                    li = line.split()
                                    if name == li[1:
                                        print line,
                                        m = 1
                                        while True:
                                            mod = raw_input("\033[33mPlease input your choice:num/name/dep/tel/exit/\033[0m ").strip()
                        #                    info = file('info.txt')
                        #                    list = info.readlines()
                                            if mod =='exit':break
                                            if len(mod) == 0:continue
                                            if mod == 'num':
                                                num = raw_input("\033[34mPlease input your number:\033[0m")
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
                                            elif mod == 'name':
                                                name_ch = raw_input("\033[34mPlease input your name:\033[0m").strip()
                                                new = ""
                                                for line in list:
                                                    x = line.split()
                                                    if name == x[1]:
                                                        x[1] = name_ch
                                                        new = new + '\t'.join(x) + '\n'
                                                    else:
                                                        new = new + line
                                                print new
                                                info.close()
                                                info = file('info.txt','w')
                                                info.write(new)
                                                info.close()
                                            elif mod == 'dep':
                                                dep = raw_input("\033[34mPlease input your department:\033[0m")
                                                new = ""
                                                for line in list:
                                                    x = line.split()
                                                    if name == x[1]:
                                                        x[2] = dep
                                                        new = new + '\t'.join(x) + '\n'
                                                    else:
                                                        new = new + line
                                                print new
                                                info.close()
                                                info = file('info.txt','w')
                                                info.write(new)
                                                info.close()
                                            elif mod == 'tel':
                                                tel = raw_input("\033[34mPlease input your telnumber:\033[0m")
                                                new = ""
                                                for line in list:
                                                    x = line.split()
                                                    if name == x[1]:
                                                        x[3] = tel
                                                        new = new + '\t'.join(x) + '\n'
                                                    else:
                                                        new = new + line
                                                print new
                                                info.close()
                                                info = file('info.txt','w')
                                                info.write(new)
                                                info.close()
                                if m == 0:print "\033[31mThere is no %s\033[0m"%name
                break
            else:
                print "\033[31mToo many wrong input,exit!!\033[0m"
                sys.exit()
    else:
        print "\033[31mThere is no %s\033[0m"%name
        continue
    break
