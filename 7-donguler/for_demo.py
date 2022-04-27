# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 14:36:44 2022

@author: cinar
"""

sayilar = [1,5,16,35,57,72,75,10]

# 1- sayilar listesindeki her bir elemanı yazdırın.
for sayi in sayilar:
    print(sayi)

# 2- Sayilar listesindeki hangi sayılar 5'in katıdır ?
for i in sayilar:
    if(i%5==0):
        print(i)

# 3- Sayilar listesinde sayıların toplamı kaçtır ?
i=0
total=0
for i in sayilar:
    total+=i
    
print(total)

# 4- Sayilar listesindeki çift sayıların karesini alınız.

for sayi in sayilar:
    if(sayi%2==0):
        print(sayi**2)


urunler = ['iphone 8','iphone 7','iphone X','iphone XR','samsung S10']

# 5- urunler listesindeki tüm ürünlerin 2.karakterlerini ekrana yazdırın.

for urun in urunler:
    print(urun[1])



# 6- urunler listesinde içinde 'iphone' geçen kaç ürün vardır? (index,find)

x= 0
for urun in urunler:
    index = urun.find('iphone')
    if (index>-1):
        x += 1
print(x)


