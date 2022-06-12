# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 15:55:51 2022

@author: cinar
"""


class User:
    
    active_users=0
    
    @classmethod
    def display_active_users(cls):
        return f" şu anda {cls.active_users} user var"
    
    
    def __init__(self,name,lastname):
        
        self.name=name 
        self.lastname=lastname
        User.active_users +=1 
    
    def fullname(self):
        return print(self.name,self.lastname)
    
   
#*****************************************************************  
 
class Moderator(User):
    
    active_moderators=0
    
    @classmethod
    def display_active_moderators(cls):
        return f" şu anda {cls.active_moderators} moderator var"
    
    def __init__(self,name,lastname,community):
        super().__init__(name,lastname)
        self.community=community
        
        Moderator.active_moderators +=1
        
    def remove_post(self):
        return f"{self.fullname()} {self.community} grubundan bir post sildi"
        
        
        
        
#******************************************************************

print(Moderator.display_active_moderators())
print(User.display_active_users())
u1=User("Ali","Çaldıran")
m1=Moderator("Merve", "Çaldıran", "DataScience")
m1.fullname()
print(User.display_active_users())
print(Moderator.display_active_moderators())

m1.remove_post()













