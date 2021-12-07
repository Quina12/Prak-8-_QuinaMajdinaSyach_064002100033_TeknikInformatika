# -*- coding: utf-8 -*-
"""
Created on Thu Dec 2 18:56:38 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

print("\nPROGRAM MENGHITUNG JUMLAH RANGE")
def jumlah_range ():
    jumlah = 0
    angka_pertama = int(input("Masukkan bilangan pertama: "))
    angka_kedua = int(input("Masukkan bilangan kedua: "))
    for i in range(angka_pertama, angka_kedua + 1, 1):
        jumlah += i
    print("\nJadi, jumlah range adalah ", jumlah )
jumlah_range()