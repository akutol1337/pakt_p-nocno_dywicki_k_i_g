class Pracownik:
    def __init__(self, imie, pensja):
        self.__imie = imie
        self.__pensja = pensja

    @property
    def imie(self):
        return self.__imie

    @property
    def pensja(self):
        return self.__pensja
    
    @pensja.setter
    def pensja(self, value):
        if value > 0:
            self.__pensja = value

pracownik = Pracownik('Jan', 3000)
print(pracownik.imie)
print(pracownik.pensja)
pracownik.pensja = 4000
print(pracownik.pensja)
pracownik.pensja = -200
print(pracownik.pensja)