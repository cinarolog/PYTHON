# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 03:16:58 2022

@author: cinar
"""

ad = 'Muhammet'
soyad = 'Cinar'
yas = '22'

msj = 'Benim adım ' + ad + ' ve soyadım ' + soyad + '.yaşım ise ' + yas + '.'

print(msj)
print(msj[-10])

#%% slicing

karakterSayisi=len(msj)
print(msj[0])                  
print(msj[1])                   
print(msj[-1])               
print(msj[karakterSayisi - 1])  

print(msj[0:5])
print(msj[:10])
print(msj[10:])

print(msj[-10:-1])
print(msj[0:40:2])
print(msj[::1])
print(msj[::-1])


#%% . format , f strings

print('My name is {} {}'.format(ad,soyad))
print('My name is {1} {0}'.format(ad,soyad))
print('My name is {s} {n}'.format(n=ad,s=soyad))
print("My name is {} {}. I'm {} years old.".format(ad,soyad,yas))
print("My name is {0} {1}. I'm {2} years old.{2}".format(ad,soyad,yas))

number = 200 / 700
print('the result is {n:1.2}'.format(n=number))

print(f"My name is {ad} {soyad} and I'm {yas} years old.")






