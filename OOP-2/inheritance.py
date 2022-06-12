# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 15:20:40 2022

@author: cinar
"""

class Person:
    
    def __init__(self,name,lastname,age):
        self.age=age 
        self.name=name 
        self.lastname=lastname 
        print("Person nesnesi türetildi...")
        
        
    def intro(self):
        return print(self.name,self.lastname,self.age)


class Student(Person):
    pass
    # def __init__(self,number):
    #     self.number=number 
        
        
        
class Teacher(Person):
    
    # def __init__(self,departmant):
    #     self.departmant=departmant 
    pass   
        

p1=Person("Github>>","cinarolog",23)
        
p1.intro()

s1=Student("Muhammet","ÇINAR",23)
s1.intro()



