#__*__encoding:UTF-8__*__

'''
Created on 2015年11月18日

@author: Administrator
'''
import types

shop = {
        '1':{'byke':int(800)},
        '2':{'iphone':int(5000)},
        '3':{'milk':int(80)},
        '4':{'coffee':int(58)}
        }

while True:
    salary= raw_input('please input your salary:')
    
    try:
        salary= int(salary)
    except  ValueError as e:
        print e
    if type(salary) is not types.IntType:
        print 'input correct datatype'
        continue
    
    else:
        break

gouwuche = []

price_list=[] 

  
while True:
            for i in shop:
                product = shop[i].keys()[0]
                price = shop[i].values()[0]
                print i,product,price
                price_list.append(price)
            
            e= raw_input('please input the no of product you want to buy:') 
            if e in shop:
                product = shop[e].keys()[0]
                price = shop[e].values()[0]
                if salary >= min(price_list):
                    salary =  salary - price
                    if salary >= 0:
                        gouwuche.append(product)
                        print 'remine money is %s:'% salary 
                        print 'you have boungt these products:%s'% gouwuche
                        print '=' * 40
                    else:
                        salary = salary + shop[e].values()[0]
                        print "you haven't enough  money pay for the %s,try other product"% product
                        print 'remine money is %s:'% salary
                        print '=' * 40
                else:
                    print 'you have not enoghu money'
                    #打印购物车商品的名称和数量
                    gouwu = []
                    [gouwu.append(s) for s in gouwuche if s not in gouwu]
                    for shangpin in gouwu:
                        print shangpin,gouwuche.count(shangpin)
                    
                    print 'remaining money is : %s' %salary
                    break
            else:
                print  'plz input the nu of product'
