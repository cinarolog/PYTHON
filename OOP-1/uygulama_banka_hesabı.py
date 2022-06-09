# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 21:47:44 2022

@author: cinar
"""


class BankAccount():
    
    def __init__(self,name):
        
        self.owner=name 
        self.balance=balance=0.0
   
        
    def deposit(self,amount):
       
        self.balance += amount
        return self.balance
    
    def getBalance(self):
        return self.balance
    
    def withdraw(self,amount):
        
        self.balance -= amount
        return  self.balance


b1=BankAccount("cinarolog")
b1.deposit(100)
b1.withdraw(22)
b1.getBalance()




