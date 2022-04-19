# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 03:31:30 2022

@author: cinar
"""

web = "www.github.com/cinarolog"
msg = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

a=" hello world  "
a.strip()
print(a)

# 2- 'www.github.com/cinarolog' içindeki sadikturan bilgisi haricindeki her karakteri silin.

sonuc = "www.github.com/cinarolog".strip('w.moc')
print(sonuc)
# 3- 'msg' karakter dizisinin tüm karakterlerini küçük harf yapın.

print(msg.lower())

# 4- 'web' içinde kaç tane a karakteri vardır ? (count('a'))

print(web.count("a"))

# 5- 'web' "www" ile başlayıp com ile bitiyor mu?

web.startswith("www")

# 6- 'web' içinde '.com' ifadesi var mı?

web.find(".com")


# 7- 'msg' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

msg.isalpha()
msg.isdigit()
# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

# 9- 'msg' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

sonuc = msg.replace(' ','-')
sonuc
# 10-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin

sonuc = 'Hello World'.replace('World','There')
sonuc
# 11-'msg' karakter dizisini boşluk karakterlerinden ayırın.

msg = msg.lower().replace(':','')
msg = msg.split()

print(msg)
