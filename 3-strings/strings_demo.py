# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 03:03:56 2022

@author: cinar
"""

website = "www.github.com/cinarolog"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- 'kursAdi' karakter dizisinde kaç karakter bulunmaktadır ?

len(kursAdi)

# 2- 'website' içinden www karakterlerini alın.

website[0:3]

# 3- 'website' içinden log karakterlerini alın.

len(website)
website[21:24]

# 4- 'kursAdi' içinden ilk 15 ve son 15 karakterlerini alın.

kursAdi[0:15]
kursAdi[-15:]

# 5- 'kursAdi' ifadesindeki karakterleri tersten yazdırın.

kursAdi[::-1]


# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.

s="Hello World"
s = s[0:6] + 'w' + s[-4:]
print(s)

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

print(3*"abc")


name, surname, age, job = 'Muhammet','Çınar', 22, 'Student' 

# 9- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Sadık Turan, Yaşım 37 ve mesleğim öğretmen.' 

sonuc = "Benim adım " + name + " " + surname + ",Yaşım " + str(age) + " ve mesleğim " + job + "."
sonuc = "Benim adım {0} {1},Yaşım {2} ve mesleğim {3}".format(name,surname,age,job)
sonuc = f"Benim adım {name} {surname},Yaşım {age} ve mesleğim {job}."

print(sonuc)
