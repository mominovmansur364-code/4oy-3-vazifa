class Telefon:
    def __init__(self,quvvat=0):
        self.__quvvat=quvvat

    def quvvatni_korish(self):
        return self.__quvvat

    def zaryadla(self,foiz):
        if self.__quvvat+foiz>100:
            print("Xatolik! Quvvat 100 dan oshmasligi kerak!")
        else:
            self.__quvvat+=foiz
            print("Muvaffaqiyatli!")

    def ishlat(self,foiz):
        if self.__quvvat>=foiz:
            self.__quvvat-=foiz
            print("Muvaffaqiyatli!")
        else:
            print("Quvvat 0 dan tushib ketmasligi kerak!")

telefon = Telefon(40)
telefon.zaryadla(60)
print(telefon.quvvatni_korish())
telefon.ishlat(15)
print(telefon.quvvatni_korish())