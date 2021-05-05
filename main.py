#gerekli kütüphaneler
import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound
import random
#benim data dosyalarım
import malzemeler
import ozellikler
import malzemeDict
import yemekDict
import yemekler

def speak(val):
    tts = gTTS(text=val,lang="tr",slow=False)
    file = "asnwer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

def mic(val):
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        if(val != ""):
            speak(val)
        audio = rec.listen(mic)
        print(">>>")
        try:
            
            said = rec.recognize_google(audio, language="tr-TR")
            if(said != ""):
                said = said.lower()
            return said
        except Exception as e:
            print("Error occured -> " + str(e))

#gerekli yenilemeler
yemekDict.refresh()
malzemeDict.refresh()
yemekList = yemekDict.yemek.keys()
yemekList = list(yemekList)

def oner():
    randomYemek = random.randint(0, len(yemekList)-1)
    istenilen = yemekList[randomYemek]
    del randomYemek
    yemek = yemekDict.yemek[istenilen]
    isim = yemek["isim"]
    using = yemek["malzemeler"]
    process = yemek["süreç"]
    ozellik = ozellikler.ozellik

    #Cümle kurma
    cumle = "size "
    for i in range(0,int(len(using)/2)):
        atilacak = random.randint(0, len(using)-1)
        using.pop(atilacak)
    for x in using:
        malzeme = malzemeDict.malzeme[x]
        cumle += malzeme["tad"] + " " + malzeme["tur"]+" " + x + malzeme["ek"]
        if(using.index(x) == (len(using)-2)):
            cumle += " ve "
        elif(using.index(x) == len(using)-1):
            pass
        else:
            cumle += ", "

    randomOzellik = random.randint(0, len(ozellik)-1)
    cumle += " ile " + process + " " + ozellik[randomOzellik] +" "+ isim + yemek["ek"] +" " + "öneriyorum "

    #final
    return cumle

while True:
    speak("hoş geldiniz, buyrun menümüze bir göz atın ağzınızı sulandıracak bir çok yemeğimiz var.")
    oneri = oner()
    speak("ben şahsen "+oneri)
    speak("menümüz burada")
    sira = 1
    for yemek in yemekList:
        if(sira%4 == 0):
            print(sira+") "+yemek)
        else:   
            print(sira,") "+yemek,end="    ")
        sira+=1
    print("")
    said = ""
    said = mic("siparişlerinizi alayım eğer aklınızda bir şey yoksa size en muhteşem yemeklerimizden birini önerebilirim")
    print(said)
    if("yok" in said):
        oneri = oner()
        said = mic("ozaman "+ oneri + "ne dersiniz")
        if("olur" in said or "tamam" in said or "peki" in said or "güzel" in said):
            speak("ustaaaa duydun gönder gelsin")
            speak("efendim yemekleriniz birazdan getirilecektir şimdiden afiyet olsun")
            break
    elif("var" in said):
        said = mic("ne veriyim abime")
        print("devam edecek...")
        break
