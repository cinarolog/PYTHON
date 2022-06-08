# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:52:41 2022

@author: cinar
"""

class Product():
    
    def __init__(self):
        self.name="cibombom"
        self.price=234
        print("nesne olusturuldu..")
        


p1=Product()
p1.name
p1.price

#%%


class Product():
    
    def __init__(self,name,price):
        self.name=name
        self.price=price
        print("nesne olusturuldu..")
        


p1=Product()
p1.name="cimbomm"
p1.price=234567

print(p1.name,p1.price)


p2=Product()
p2.name="asdf"
p2.price=2344543343



