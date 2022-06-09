# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 00:08:12 2022

@author: cinar
"""

class Comment():
    
    def __init__(self,username,text,likes,dislikes=0):
        
        self.username=username 
        self.text=text 
        self.likes=likes
        self.dislikes=dislikes 
 
        
 
        

c1=Comment("sdf","dsffbd",2334)   
c2=Comment("Sakdgdgaci08","dsffbd",245334)             
c3=Comment("Sakdfdgaci08","dsffefg3fbd",26678334)   

comments=[c1,c2,c3]

for i in comments:
    print(i.username,i.likes)



