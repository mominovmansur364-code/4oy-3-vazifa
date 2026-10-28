from abc import ABC,abstractmethod

class Transport(ABC):

    @abstractmethod
    def harakatlan(self):
        pass

class Mashina(Transport):
    def harakatlan(self):
        print(f"Mashina yo'lda harakatlanmoqda 🚓☁️")


class Velosiped(Transport):
    def harakatlan(self):
        print(f"Velosiped yo'lda harakatlanmoqda 🚲☁️")

mashina=Mashina()
velosiped=Velosiped()

mashina.harakatlan()
velosiped.harakatlan()