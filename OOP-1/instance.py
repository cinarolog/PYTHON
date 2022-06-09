# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 21:34:18 2022

@author: cinar
"""

class Person():
    
    #constructor
    def __init__(self,name,lastname,year):
        
        #object attributes
        self.name=name
        self.lastname=lastname      
        self.year=year
    
    #instance method
    def intro(self):
        return print(f"Benim adım {self.name} ve soy adım {self.lastname}")
        
    def yas_hesapla(self):
        return (2022 - int(self.year))
        
        
p1=Person("Muhammet" ,"Cinar",1999)  
p2=Person("X","y",2000)
p2.yas_hesapla() 
p1.yas_hesapla()     
p1.intro()
p2.intro()






