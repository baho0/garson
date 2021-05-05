import os
print("""
-------------------------------
|                             |
|   Garson Yönetici Konsolu   |
|                             |
| 1) Malzeme ekle             |
| 2) Yemek ekle               |
-------------------------------
""")

while True:
    secim = input("Seçim >>> ")
    if(secim == "1"):
        os.system("malzemeEkle.py")
    elif(secim == "2"):
        os.system("yemekEkle.py")
    else:
        print("geçersiz işlem")