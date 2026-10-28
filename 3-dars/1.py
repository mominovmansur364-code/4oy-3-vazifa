class BankHisobi:
    def __init__(self,balans=0):
        self.__balans=balans

    def balansni_korish(self):
        return f"Balans: {self.__balans}"

    def pul_qosh(self,miqdor):
        if miqdor>0:
            self.__balans+=miqdor
            print("Muvaffaqiyatli balans to'ldirildi!")
        else:
            print("Xatolik! Balansga manfiy sonni qoshib bolmaydi!")

    def pul_yech(self,miqdor):
        if self.__balans>=miqdor:
            self.__balans-=miqdor
            print("Muvaffaqiyatli yechildi!")
        else:
            print("Balansingizda mablag' yetarli emas!")

hisob = BankHisobi(100000)
hisob.pul_qosh(25000)
print(hisob.balansni_korish())
hisob.pul_yech(30000)
print(hisob.balansni_korish())
