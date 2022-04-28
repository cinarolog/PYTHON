# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:11:22 2022

@author: cinar
"""

sayilar = [4,6,9,10,35,57,89,125,244]

# 1: sayilar listesini while ile ekrana yazdırın.

i=0
while i < len(sayilar):
    print(sayilar[i])
    i+=1


# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları 
# ekrana yazdırın.

x=int(input("basla :"))
y=int(input("bitir :"))

while x<y :
    if(x%2==1):
        print(x)
    x+=1    
        
    
# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.


i=100
while i>0:
    print(i)
    i-=1


# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

i=0
sayilar2=[]

while i<5:
    sayi=int(input("sayi gir :"))
    sayilar2.append(sayi)
    sayilar2.sort()
    i+=1
 
sayilar2









