print("""
--------------------
|Yemek ekleme aracı|
--------------------
""")
yemekDicts = {"sıcak":"sicakYemek","hafif":"hafifYemek"}
isim = input("yemeğin ismi >>> ")
text = "\n"+ isim + " = {\"malzemeler\" : "
malzemeler = []
while True:
    malzeme = input("malzeme ismi girin >>> ")
    if(malzeme != "q"):
        malzemeler.append(malzeme) 
    else:
        break
text += str(malzemeler).replace("\'","\"") + ", \"süreç\" : \""
surec = input("süreç girin >>> ")
text += surec +"\" , \"ek\" : \""
ek = input("ek girin >>> ")
ozellik = input("özellik girin >>> ")
text += ek + "\" , \"isim\" : \""+isim +"\",\"özellik\":\""+ozellik+"\"}"
myfile = open("yemekler.py","a+",encoding="utf-8")
myfile.write(text)
myfile.close()
myfile = open("yemekDict.py","a+",encoding="utf-8")
text = "\n    yemek[\"{}\"] = yemekler.{}".format(isim,isim)
myfile.write(text)
text = "\n    "+yemekDicts[ozellik]+"[\"{}\"] = yemekler.{}".format(isim,isim)
myfile.write(text)
myfile.close()