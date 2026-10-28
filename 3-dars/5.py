from abc import ABC,abstractmethod

class Tolov(ABC):
    @abstractmethod
    def tolash(self,summa):
        pass

class NaqdTolov(Tolov):
    def tolash(self, summa):
        print(f"{summa} so'm naqd pul orqali to'landi")

class KartaTolov(Tolov):
    def tolash(self, summa):
        print(f"{summa} so'm karta orqali to'landi")

naqd=NaqdTolov()
karta=KartaTolov()

naqd.tolash(50000)
karta.tolash(50000)