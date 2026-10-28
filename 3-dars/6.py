from abc import ABC,abstractmethod

class Nashr(ABC):

    def __init__(self,ism,narx):
        self.ism=ism
        self.__narx=narx

    def narxni_korish(self):
        return self.__narx

    def narxni_ozgartir(self,yangi_narx):
        if yangi_narx>=0:
            self.__narx=yangi_narx
        else:
            print("Xatolik! Narx 0 dan kichik bolmaydi!")

    @abstractmethod
    def malumot_ber(self):
        pass

class Kitob(Nashr):

    def __init__(self, ism, narx,muallif):
        super().__init__(ism, narx)
        self.muallif=muallif

    def malumot_ber(self):
        return f"Kitob nomi: {self.ism},muallifi: {self.muallif}, narxi: {self.narxni_korish()} so'm"

class Jurnal(Nashr):
    def __init__(self, ism, narx,soni):
        super().__init__(ism, narx)
        self.soni=soni

    def malumot_ber(self):
        return f"Jurnal: {self.ism}, soni: {self.soni}, narxi: {self.narxni_korish()} so'm"

class Kutubxona:
    def __init__(self,nom):
        self.nom=nom
        self.__nashrlar=[]

    def nashr_qosh(self,nashr):
        self.__nashrlar.append(nashr)
        print(f"{nashr.ism} kutubxonaga qoshildi!")

    def barcha_nashrlar(self):
        print(f"{self.nom}dagi barcha nashrlar")
        for nashr in self.__nashrlar:
            print(nashr.malumot_ber())


kitob1 = Kitob("O'tkan kunlar", 150000, "Abdulla Qodiriy")
kitob2 = Kitob("Sariq devni minib", 120000, "Xudoyberdi To'xtaboyev")
jurnal1 = Jurnal("Gulxan", 25000, 5)

kitob1.narxni_ozgartir(140000)

kutubxona = Kutubxona("Milliy Kutubxona")
kutubxona.nashr_qosh(kitob1)
kutubxona.nashr_qosh(kitob2)
kutubxona.nashr_qosh(jurnal1)

kutubxona.barcha_nashrlar()

