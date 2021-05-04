import malzemeler
malzeme = {"kıyma":malzemeler.kiyma, "domates":malzemeler.domates, "soğan":malzemeler.sogan,"biber":malzemeler.biber,"yumurta":malzemeler.yumurta}

def refresh():
    malzeme["patates"] = malzemeler.patates
    malzeme["maydanoz"] = malzemeler.maydanoz
