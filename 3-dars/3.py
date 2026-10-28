class Mahsulot:
    def __init__(self,nom,miqdor):
        self.nom=nom
        self.__miqdor=miqdor

    def miqdorni_korish(self):
        return f"{self.__miqdor} dona"

    def qabul_qil(self,son):
        if son>0:
            self.__miqdor+=son
            print("Muvaffaqiyatli!")
        else:
            print("Xatolik! Musbat son kiriting!")

    def sotish(self,son):
        if self.__miqdor>=son:
            self.__miqdor-=son
            print("Muvaffaqiyatli!")
        else:
            print("Mahsulot yetarli emas!")

mahsulot = Mahsulot("Daftar", 20)
mahsulot.sotish(6)
print(mahsulot.miqdorni_korish())
mahsulot.qabul_qil(4)
print(mahsulot.miqdorni_korish())