import numpy as np
import sympy as sp
from sympy import *
import time as tm

print("===================================")
print("######## PROGRAM KALKULUS #########")
print("===================================\n")

def Hitung_limit():
    x, y = sp.symbols('x,y')
    print("Menghitung limit siap!")
    fungsi = input("masukan fungsi: ")
    nilaix = input("nilai x mendekati: ")
    f = sp.limit(fungsi, x, nilaix, dir='+-')
    print("hasilnya adalah: ", f, "\n")
    
def Hitung_turunan():
    x, y = sp.symbols('x,y')
    print("Menghitung turunan siap!")
    fungsi = input("masukan fungsi: ")
    f = sp.diff(fungsi, x)  # Memperbaiki argumen untuk diff()
    print("hasilnya adalah: ", f, "\n")
    
def Hitung_integral():
    x, y = sp.symbols('x,y')
    print("Menghitung integral siap!")
    fungsi = input("masukan fungsi: ")
    f = sp.integrate(fungsi, x)  # Memperbaiki argumen untuk integrate()
    print("hasilnya adalah: ", f, "+ C\n")

def hitung_mundur():
    for i in range(3, 0, -1):
        print(i, "...")
        tm.sleep(1)
    print("Terimakasih telah menggunakan program ini")
    
while True:
    userInput = int(input("Silahkan pilih rumus: \n\n1. Limit\n2. Turunan\n3. Integral\n4. Exit\n\nPilih nomor berapa: "))
    if userInput == 1:
        Hitung_limit()
    elif userInput == 2:
        Hitung_turunan()
    elif userInput == 3:
        Hitung_integral()
    elif userInput == 4:
        hitung_mundur()
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")