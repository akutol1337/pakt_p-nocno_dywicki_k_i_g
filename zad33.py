from abc import ABC, abstractmethod

class Pojazd(ABC):
    @abstractmethod
    def start(self):
        pass

class Samochód(Pojazd):
    def start(self):
        print("Samochód uruchomiony")

class Motocykl(Pojazd):
    def start(self):
        print("Motocykl uruchomiony")

auto = Samochód()
motocykl = Motocykl()

auto.start()      
motocykl.start()  
