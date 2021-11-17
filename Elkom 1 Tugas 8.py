# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 11:02:01 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

def memunculkan_karakter_index_ganjil(x):
    Karakter_indeks_ganjil = [x[i] 
    for i in range(len(x)) if i%2==1]
    print("Karakter index ganjil: ","".join(Karakter_indeks_ganjil))
    return(Karakter_indeks_ganjil)

print("\nPROGRAM MEMUNCULKAN KARAKTER INDEX GANJIL")
Kata = input("Masukan sebuah kata: ")
memunculkan_karakter_index_ganjil(Kata)