import yemekler
yemek = {"kıyma kavurma":yemekler.kiymaKavurma,"menemen":yemekler.menemen}
sicakYemek = {"kıyma kavurma":yemekler.kiymaKavurma,"menemen":yemekler.menemen}
hafifYemek = {}
def refresh():
    yemek["lahmacun"] = yemekler.lahmacun
    sicakYemek["lahmacun"] = yemekler.lahmacun