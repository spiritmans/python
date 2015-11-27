#!/usr/bin/env python
# -*- conding:utf8 -*-
import types
import sys
product = ['Iphone','TV','cloth','book','bike']
cost = [4899, 3299, 329, 54, 1029]

while True:
    gz = raw_input('Please input your salary:').strip()
    salary = int(gz)
    if type(salary) is int:
        break
    else:
        continue
###############################################
cart_list = []
while True:
    cost_list = []
    #打印商品列表
    for a in product:
        p = a
        c = cost[product.index(a)]
        cost_list.append(c)
     	print p, c
    #筛选可以购买和不能购买列表
    no_list = []
    store_list = []
    for b in cost_list:
        if salary >= b:
            x = product[cost.index(b)]
            store_list.append(x)
        else:
            x = product[cost.index(b)]
            no_list.append(x)
    if len(store_list) == 0:		#当可购买列表为0时，退出
        print 'You have no enough money to buy %s'%no_list
        print 'You can not to buy anything,exit!'
        sys.exit()
    elif len(no_list) != 0:		#当不可购买列表不为0时，打印不可购买列表
        print 'You have no enough money to buy %s'%no_list
        pass
    #打印可购买列表
    print 'You can choose the product that you want to buy from %s'%store_list
    #开始选择购买产品
    choice = raw_input('Please input your choice:').strip()
    if choice == 'exit':break
    if choice in store_list:
        cart_list.append(choice)
        price = cost[product.index(choice)]
        salary = salary - int(price)
        print 'You will to buy %s(%d)'%(choice,price)
        print 'Your cart list: %s'%cart_list
        print 'Your salary had left %s'%salary
        print '#####################################'
        continue
    else:
        print 'Wrong input,there is no %s'%choice
