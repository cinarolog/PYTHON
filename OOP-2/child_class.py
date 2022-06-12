# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 15:36:19 2022

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
    
    
#************************************************ 


class Student(Person):
    
    def __init__(self,name,lastname,age,number):
        
        Person.__init__(self,name,lastname,age)
        # super().__init__(name,lastname,age)
        self.number=number
        print("Student nesnesi türetildi...")
        
    def study(self):
        return f"{self.number} nolu öğrenci çalışıyor"
    
    def intro(self):
        return print(self.name,self.lastname,self.age,self.number)
    
        
        
        
        
        
 #************************************************       
        
class Teacher(Person):
    
    def __init__(self,name,lastname,age,departmant):
         
        Person.__init__(self,name,lastname,age)
        # super().__init__(name,lastname,age)
        self.departmant=departmant
        print("Teacher nesnesi türetildi...")
 
    def teach(self):
        return f"{self.departmant} Öğretmeni"
    
    def intro(self):
        return print(self.name,self.lastname,self.age,self.departmant)
    



       
#************************************************
p1=Person("Github>>","cinarolog",23)
        
p1.intro()

s1=Student("Muhammet","ÇINAR",23,34567)
s1.intro()
s1.number 
s1.study()

t1=Teacher("Selim","ÇINAR",30,"Türkçe")
t1.intro()
t1.departmant
t1.teach()




