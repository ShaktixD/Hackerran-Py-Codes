# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 2022

@author: shakti
"""
#OrderedDict in collections ==================================================
from collections import OrderedDict
from collections import Counter
basket = OrderedDict()
record = []
for i in range(int(input())):
    x = input().split()
    item_name,each_price = ' '.join(x[:-1]),int(x[-1])
    basket[item_name] = int(each_price)
    record.append(item_name)
coun_t = Counter(record)
for k,v in basket.items():
    print(k,v*coun_t[k])
    
#print(basket.items[i],format(coun_t[basket.items[i]]*basket[basket.items[i]],"0.2f"))    