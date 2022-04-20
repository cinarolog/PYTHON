# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 03:51:50 2022

@author: cinar
"""

# 1-  "Samsung S5,Samsung S6,Samsung S7,Samsung S8" elemanlarına sahip bir liste oluşturunuz.

s=["Samsung S5","Samsung S6","Samsung S7","Samsung S8"]
type(s)

# 2-  Liste Kaç elemanlıdır ?
len(s)

# 3-  Listenin ilk ve son elemanı nedir ?
s[0]
s[3]

# 4-  "Samsung S5" değerini "Samsung S9" ile değiştirin.

s[0]="Samsung S9"
s
# 5-  "Samsung S6" listenin bir elemanı mıdır ?

if "Samsung S6" in s:
    print(True)

# 6-  Listenin -3 indeksindeki değer nedir ?

s[-3]

# 7-  Listenin ilk 2 elemanını alın.

s[0:2]

# 8-  Listenin son 2 elemanı yerine "Samsung S9" ve "Samsung S10" değerlerini ekleyin.
s[-2:] = ["Samsung S9","Samsung S10"]


# 9-  Listenin üzerine "IPhone X" ve "IPhone XR" değerlerini ekleyin.

s=s+ ["IPhone X" , "IPhone XR"]
s

# 10- Listenin son elemanını silin.
del s[-1]
s
# 11- Liste elemanlarını tersten yazdırınız.

s[::-1]

# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # kullaniciA: Yiğit Bilgi 2010, (70,60,70)
      # kullaniciB: Sena Turan  1999, (80,80,70)
      # kullaniciC: Ahmet Turan 1998, (80,70,90)
ogrenciA = ["Yiğit","Bilgi",2010,[70,60,70]]
ogrenciB = ["Sena","Turan",1999,[80,80,70]]
ogrenciC = ["Ahmet","Turan",1998,[80,70,90]]

ogrenciler = [ogrenciA,ogrenciB,ogrenciC]

for ogrenci in ogrenciler:
      ad = ogrenci[0]
      soyad = ogrenci[1]
      yas = 2021-ogrenci[2]
      ortalama = (ogrenci[3][0] + ogrenci[3][1]+ ogrenci[3][2]) / 3
      print(f"{ad} {soyad} {yas} {ortalama}")

# 13- Liste elemanlarını ekrana yazdırınız.


for i in s:
    print(i)












