class Pojazd:
    def __init__(self, prędkość):
        self._predkosc = prędkość

class Samochod(Pojazd):
    def __init__(self, prędkość):
        super().__init__(prędkość)

    def zwieksz_predkosc(self, ile):
        if self._predkosc + ile <= 200:
            self._predkosc += ile
        print(samochód._predkosc)

samochód = Samochod(100)
for i in range(7):
    samochód.zwieksz_predkosc(20)