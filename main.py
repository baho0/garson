import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound
import random

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

class malzemeler:
    #malzemeler
    kiyma = {"tad" : "leziz", "tür":"kuzu", "ek":"sı"} 
    domates = {"tad" : "leziz", "tür":"çanakkale", "ek" :"i"} 
    sogan = {"tad" : "taze", "tür":"arpacık", "ek" :"ı"} 
    biber = {"tad":"dalından yeni koparılmış", "tür":"sivri","ek":"i"}
    yumurta = {"tad":"nefis","tür":"gezen tavuk","ek":"sı"}
    #malzeme dict
    malzeme = {"kıyma":kiyma, "domates":domates, "soğan":sogan,"biber":biber,"yumurta":yumurta}
    #ek özellikler
    özellik = ["harika","şahane","muhteşem","paşalara layık"]
    #yemekler
    kiymaKavurma = {"malzemeler":["soğan","kıyma"], "süreç":"kavrulmuş", "ek":"yı", "isim":"kıyma kavurma"}
    menemen = {"malzemeler":["soğan","biber","domates","yumurta"],"süreç":"pişirilmiş", "ek":"i","isim":"menemen"}
    #yemek dict
    yemek = {"kıyma kavurma":kiymaKavurma,"menemen":menemen}


istenilen = input("yemek ismi[test için] >>> ")
yemek = malzemeler.yemek[istenilen]
isim = yemek["isim"]
using = yemek["malzemeler"]
process = yemek["süreç"]
ozellik = malzemeler().özellik

#Cümle kurma
cumle = "size "
for i in range(0,int(len(using)/2)):
    atilacak = random.randint(-1, len(using)-1)
    using.pop(atilacak)
for x in using:
    malzeme = malzemeler.malzeme[x]
    cumle += malzeme["tad"] + " " + malzeme["tür"]+" " + x + malzeme["ek"]
    if(using.index(x) == (len(using)-2)):
        cumle += " ve "
    elif(using.index(x) == len(using)-1):
        pass
    else:
        cumle += ", "

randomOzellik = random.randint(0, len(ozellik)-1)
cumle += " ile " + process + " " + ozellik[randomOzellik] +" "+ isim + yemek["ek"] +" " + "öneriyorum."

#final
speak(cumle)