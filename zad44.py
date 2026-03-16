from abc import ABC, abstractmethod

class Zwierze(ABC):
    @abstractmethod
    def podajTemperature(self):
        pass

class Stalocieple(Zwierze):
    def __init__(self, nazwa, temperatura):
        self.nazwa = nazwa
        self.temperatura = temperatura
    
    def podajTemperature(self):
        return f"{self.nazwa} ma stałą temperaturę ciała: {self.temperatura}°C"

class Zmiennocieple(Zwierze):
    def __init__(self, nazwa, temperatura_minimalna, temperatura_maksymalna):
        self.nazwa = nazwa
        self.temperatura_minimalna = temperatura_minimalna
        self.temperatura_maksymalna = temperatura_maksymalna
    
    def podajTemperature(self):
        return (f"{self.nazwa} ma zmienną temperaturę ciała w zakresie: "
                f"{self.temperatura_minimalna}°C - {self.temperatura_maksymalna}°C")

pies = Stalocieple("Pies", 38.5)
żaba = Zmiennocieple("Żaba", 5, 25)

print(pies.podajTemperature())
print(żaba.podajTemperature())
