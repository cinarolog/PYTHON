# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 01:15:08 2022

@author: cinar
"""


class Pet():
    
    cinsler=["kedi","köpek","kuş"]
     
    def __init__(self,isim,cins):
        
        if cins not in Pet.cinsler:
            raise ValueError(f"{cins} evcil hayvan değil")
        self.name=isim
        self.cins=cins 
        
boncuk=Pet("Boncuk","kedi")       
pasa=Pet("Paşa","köpek") 

mavis=Pet("Broo","aslan")



































