# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 02:41:19 2022

@author: cinar
"""

# Bir aracın yakıt tipine göre (benzin,dizel) belirtilen bir mesafede 
# ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.

benzin = 6.69
dizelFiyat = 5.86
toplamYakitUcreti = 0

ortalamaYakitTuketimi = float(input(' ortalama yakıt tüketimi: '))
gidilecekYol = float(input('gidilecek yol  '))
yakitTipi = input('yakıt tipi ')

toplamYakitTuketimi = gidilecekYol * (ortalamaYakitTuketimi / 100)

if(yakitTipi == "benzin"):
    toplamYakitUcreti = benzin * toplamYakitTuketimi
elif (yakitTipi == "dizel"):
    toplamYakitUcreti = dizelFiyat * toplamYakitTuketimi
else:
    print('yanlış yakıt tipi girdiniz.')

if (toplamYakitUcreti != 0):
    print(toplamYakitUcreti)
    
    
    