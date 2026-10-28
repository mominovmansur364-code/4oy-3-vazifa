from abc import ABC,abstractmethod

class Mahsulot(ABC):
    def __init__(self,nomi,narx):
        self.nomi=nomi
        self.__narx=narx

    def narxni_korish(self):
        return self.__narx

    def narxni_ozgartir(self,yangi_narx):
        if yangi_narx>0:
            self.__narx=yangi_narx
            print("Narx muvaffaqiyatli yangilandi!")
        else:
            print("Narx manfiy bolmaydi!")

    @abstractmethod
    def tavsif_ber(self):
        pass

class Telefon(Mahsulot):
    def __init__(self, nomi, narx,xotira):
        super().__init__(nomi, narx)
        self.xotira=xotira

    def tavsif_ber(self):
        return f"Mahsulot nomi: {self.nomi}, xotirasi: {self.xotira} GB, narxi: {self.narxni_korish()} so'm"

class Noutbuk(Mahsulot):
    def __init__(self, nomi, narx,ram):
        super().__init__(nomi, narx)
        self.ram=ram

    def tavsif_ber(self):
        return f"Mahsulot nomi: {self.nomi}, ram xotirasi: {self.ram} GB, narxi: {self.narxni_korish()} so'm"



class Dokon:
    def __init__(self,nom):
        self.nom=nom
        self.__mahsulotlar=[]

    def mahsulot_qosh(self, mahsulot):
       self.__mahsulotlar.append(mahsulot)
       print(f"{self.nom} mahsulotlarga qo'shildi")

    def barcha_mahsulotlar(self):
        print(f"{self.nom}dagi barcha mahsulotlar")
        for mahsulot in self.__mahsulotlar:
            print(mahsulot.tavsif_ber())

telefon1=Telefon("Iphone",7000000,256)
telefon2=Telefon("Samsung",5500000,128)
noutbuk1=Noutbuk("Victus",10000000,8)

telefon1.narxni_ozgartir(6900000)

dokon=Dokon("Maishiy texnikalar")
dokon.mahsulot_qosh(telefon1)
dokon.mahsulot_qosh(telefon2)
dokon.mahsulot_qosh(noutbuk1)

dokon.barcha_mahsulotlar()