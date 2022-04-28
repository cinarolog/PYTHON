# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:11:35 2022

@author: cinar
"""

#    Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

i=0
urunler=[]
adet=int(input("ürün sayisi : "))

while i<adet:
    urun=input("ad : ")
    fiyat=int(input("fiyat : "))
    
    urunler.append({
                    "ürün" : urun,
                    "fiyat" : fiyat})
    i+=1

urunler


for urun in urunler:
    print(f"ürün adı: {urun['ürün']} ürün fiyatı: {urun['fiyat']}")

 



