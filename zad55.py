from abc import ABC, abstractmethod
class Transport(ABC):
    @abstractmethod
    def srednia_predkosc(self):
        pass
    def koszt_podrozy(self):
        pass

class Samolot(Transport):
    def __init__(self, czas, dystans, cena):
        self.czas = czas
        self.dystans = dystans
        self.cena = cena
    def srednia_predkosc(self):
        pass
    def koszt_podrozy(self):
        pass
        
class Pociag(Transport):
    def __init__(self, czas, dystans, cena):
        self.czas = czas
        self.dystans = dystans
        self.cena = cena
    def srednia_predkosc(self):
        pass
    def koszt_podrozy(self):
        pass
    
class Rower(Transport):
    def __init__(self, czas, dystans, cena):
        self.czas = czas
        self.dystans = dystans
        self.cena = cena
    def srednia_predkosc(self):
        pass
    def koszt_podrozy(self):
        pass
