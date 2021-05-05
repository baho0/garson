print("""
--------------------
|Yemek ekleme aracı|
--------------------
""")
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
text += ek + "\" , \"isim\" : \""+isim +"\"}"
myfile = open("yemekler.py","a+",encoding="utf-8")
myfile.write(text)
myfile.close()
myfile = open("yemekDict.py","a+",encoding="utf-8")
text = "\n    yemek[\"{}\"] = yemekler.{}".format(isim,isim)
myfile.write(text)
myfile.close()