from abc import ABC, abstractmethod
class Pracownik(ABC):
    @abstractmethod
    def oblicz_pensje(self):
        pass

class Programista(Pracownik):
    def __init__(self, godziny, stawka):
        self.godziny = godziny
        self.stawka = stawka

    def oblicz_pensje(self):
        return self.godziny * self.stawka
    
class Kierownik(Pracownik):
    def __init__(self, pensja_podstawowa, premia):
        self.pensja_podstawowa = pensja_podstawowa
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja_podstawowa + self.premia
