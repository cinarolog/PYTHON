# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 01:59:24 2022

@author: cinar
"""

isimler = ["Ahmet","ali","Çınar","DeNiz"]
string = "Hello 123456 World."
yillar = [1983, 1999, 2008, 1956, 1986]
dereceler = [20,5,15,-2,0,-6]

# 1- "1-100" arasındaki sayılardan 12' e tam bölünebilen sayı listesi oluşturunuz.

sayilar=[i for i in range(1,100) if i%12==0]
sayilar

# 2- isimler listesindeki her ismi küçük harfe çevirip tersten yazdınız.

isimler_=[isim.lower()[::-1] for isim in isimler]
isimler_

# 3- verilen "string" içindeki rakamları içeren bir liste oluşturunuz.

strings=[c for c in string if c.isdigit()]
strings

# 4- "yillar" dizisindeki her doğum yılı için yaş bilgisini içeren liste oluşturunuz.

import datetime
simdi = datetime.datetime.now().year
sonuc = [simdi - yil for yil in yillar]
sonuc
# 5- "dereceler" listesinde bulunan hava sıcaklık bilgisine göre eksi değer için buzlanma tehlikesi yazdırınız.

sonuc = [i if i>=0 else "buzlanma tehlikesi" for i in dereceler]
print(sonuc)


