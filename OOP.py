class Mašīna:
    def __init__(self,marka,dzinējs,cena):
        self.marka = marka
        self.dzinējs = dzinējs
        self.cena = cena

    def hello(self):
        return f"Mani sauc {self.marka} un es maksāju {self.cena} Euro"    


class Angļu_Mašīnas(Mašīna):
    pass




volvo = Mašīna("Volvo","2.5tdi",5000) 
bmw = Mašīna("BMW","3.0",7500)
ford = Mašīna("Ford","1.8",4500)

jaguar = Angļu_Mašīnas("Jaguar","3.0",6500)    



print(volvo.cena)
print(volvo.hello())
volvo.cena = 12000
volvo.atlaide = 1200
print(volvo.hello())
print(volvo.atlaide)
print(jaguar.hello())




