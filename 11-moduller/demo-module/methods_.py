# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:21:39 2022

@author: cinar
"""
import db

def urunEkle(urunAdi,fiyat):
    db.urunler.append({
        "id": len(db.urunler) + 1,
        "urunAdi": urunAdi,
        "fiyat": fiyat
    })

def urunGuncelle(id, urunAdi, fiyat):
    for urun in db.urunler:
        if(urun["id"] == id):
            urun["urunAdi"] = urunAdi
            urun["fiyat"]=fiyat
            break

def urunleriGetir():
    for urun in db.urunler:
        print(f"id {urun['id']} ürün adı: {urun['urunAdi']} fiyat: {urun['fiyat']}")