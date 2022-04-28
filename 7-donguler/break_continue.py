# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:42:16 2022

@author: cinar
"""

isim = "cinarolog"

for harf in isim:
    if (harf == "r"):
        break
    print(harf)

i = 0
while (i < 5):
    i += 1
    if (i == 3):
        continue
    print(i)

print('MuhammetÇınar/gihub/cinarolog')

# 1-100 arasÄ±ndaki çift sayilar toplam.

i = 0
toplam = 0

while (i <= 100):
    i += 1
    if (i % 2 == 1):
        continue
    toplam += i

print(f"toplam: {toplam}")

print("\U0001f600")
