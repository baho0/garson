print("""
----------------------
|Malzeme ekleme aracı|
----------------------
""")
isim = input("malzemenizin ismi >>> ")
tad = input("tad girin >>> ")
tur = input("tür girin >>> ")
ek = input("ek girin >>> ")
myfile = open("malzemeler.py","a+",encoding="utf-8")
text = "\n"+isim+" = "+ "{ \"tad\" : "+"\""+tad+"\""+", "+"\""+"tur\""+":" +"\""+tur+"\""+", "+"\""+"ek"+"\""+":" +"\""+ek+"\""+"}"
myfile.write(text)
myfile.close()
myfile = open("malzemeDict.py","a+",encoding="utf-8")
text = "\n    malzeme[\""+isim+"\"]"+" = "+"malzemeler."+isim+"\n"
myfile.write(text)
myfile.close()