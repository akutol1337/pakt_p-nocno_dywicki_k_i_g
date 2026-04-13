class Pojazd:
    def __init__(self, predkosc):
        self._predkosc = predkosc  


class Samochod(Pojazd):
    def zwieksz_predkosc(self, ile):
        if self._predkosc + ile <= 200:
            self._predkosc += ile