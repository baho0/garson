import malzemeler
malzeme = {"kıyma":malzemeler.kiyma, "domates":malzemeler.domates, "soğan":malzemeler.sogan,"biber":malzemeler.biber,"yumurta":malzemeler.yumurta,"hamur":malzemeler.hamur}

def refresh():
    malzeme["patates"] = malzemeler.patates
    malzeme["maydanoz"] = malzemeler.maydanoz
    malzeme["hamur"] = malzemeler.hamur
