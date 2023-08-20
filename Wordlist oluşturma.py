#! usr/bin/env/python
# -*- coding: utf-8 -*-

import os

os.system("apt install figlet")
os.system("apt install crunch")
os.system("clear")
os.system("figlet WORDLİST TOOL")

print("""
Wordlist Oluşturma Tooluna Hoş Geldiniz!

""")

minkarakter = input("Minimum Karakter Sayısını Girin: ")

maxkarakter = input("Maximum Karakter Sayısını Girin: ")

karakter = input("Wordilstin Oluşturacağı Karakterleri Girin : ")

kayityeri = input ("Wordlistin Kaydedileceği Yerin Dizin Yolunu Girin :")

os.system("crunch " + minkarakter + " " + maxkarakter + " " + karakter + " -o " + kayityeri)

print("İşlem Başarıyla Tamamlanmıştır ") 
