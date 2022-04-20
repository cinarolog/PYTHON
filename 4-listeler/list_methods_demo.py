# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:55:57 2022

@author: cinar
"""

isimler = ['Ada','Yigit','Hasan','Beril']
yaslar = [1998, 2000, 1999,1999, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.

isimler.append('Cenk')
isimler
# 2-  "Sena" deÄŸerini listenin baÅŸÄ±na ekleyiniz.

isimler.insert(0,"éSena")
isimler

# 3-  "YiÄŸit" ismini listeden siliniz.

isimler.remove("Yigit")
isimler

# 4-  "Cenk" isminin indeksi nedir ?

isimler.index("Cenk")

# 5-  "Beril" listenin bir elemanÄ± mÄ±dÄ±r ?

if "Beri4l" in isimler:
    print("Evet")
else :
    print("hayır")    

# 6-  Liste elemanlarÄ±nÄ± ters Ã§evirin.

isimler.reverse()
isimler
# 7-  Liste elemanlarÄ±nÄ± alfabetik olarak sÄ±ralayÄ±nÄ±z.

isimler.sort()
isimler
# 8-  yaslar listesini rakamsal bÃ¼yÃ¼klÃ¼ÄŸe gÃ¶re sÄ±ralayÄ±nÄ±z.

yaslar.sort()
yaslar
# 9-  s = "IPhone X,IPhone XR" karakter dizisini listeye Ã§eviriniz.
s = "IPhone X,IPhone XR"
sonuc = s.split(',')
print(sonuc)


s = "IPhone X,IPhone XR"
isimler.append(s)
isimler

# 10- yaslar dizisinin en bÃ¼yÃ¼k ve en kÃ¼Ã§Ã¼k elemanÄ± nedir ?

max(yaslar)
min(yaslar)
# 11- yaslar dizisinde kaÃ§ tane 1998 deÄŸeri vardÄ±r ?

yaslar.count(1999)


# 12- yaslar dizisinin tÃ¼m elemanlarÄ±nÄ± siliniz.

yaslar.clear()
yaslar

# 13- KullanÄ±cÄ±dan alacaÄŸÄ±nÄ±z 3 tane marka bilgisini bir listede saklayÄ±nÄ±z.

i=0
names=[]
for i in range(3):
    
    name=input("name1:")
    names.append(name)
    
names    
    
    











