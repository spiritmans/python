#!/usr/bin/python

name=raw_input("what's your name:")
age=raw_input("how old are you:")
sex=raw_input("please input your sex:")
dep=raw_input("which dep:")

message='''Information of compeny staff:
    Name :%s
    Age  :%s
    Sex  :%s
    Dep  :%s
    ''' %(name, age, sex, dep)
    
print message