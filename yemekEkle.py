print("""
--------------------
|Yemek ekleme aracı|
--------------------
""")
isim = input("malzemenizin ismi >>> ")
tad = input("tad girin >>> ")
tur = input("tür girin >>> ")
ek = input("ek girin >>> ")
myfile = open("yemekler.py","a+")
text = "\n"+ isim+" = "+ "{ \"tad\" : "+"\""+tad+"\""+", "+"\""+"tür \""+":" +"\""+tur+"\""+", "+"\""+"ek"+"\""+":" +"\""+ek+"\""+"}"
myfile.write(text)