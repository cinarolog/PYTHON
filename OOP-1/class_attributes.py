# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 00:59:20 2022

@author: cinar
"""

class User():
    
    active_users=0
    
    def __init__(self,name,lastname,age):
        
        self.name=name
        self.age=age 
        self.lastname=lastname
        User.active_users +=1
        
        
    def fullname(self):
        return f"{self.name} {self.lastname}"
    
    def logout(self):
        User.active_users -=1
        return f"{self.fullname() } çıkış yaptı"



u1=User("Muhammet","Çınar",23)
u2=User("ali","Çınar",55)
print(User.active_users)
u1.logout()
u1.fullname()
u2.fullname()




















