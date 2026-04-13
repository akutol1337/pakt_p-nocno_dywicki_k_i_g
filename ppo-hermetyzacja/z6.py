class Samochod:
    def __init__(self, marka):
        self._marka = marka
        self._predkosc = 0            
        self.__stan_silnika = "wyłączony"  

    def wlacz_silnik(self):
        self.__stan_silnika = "włączony"

    def wylacz_silnik(self):
        if self._predkosc == 0:
            self.__stan_silnika = "wyłączony"

    def przyspiesz(self, ile):
        if self.__stan_silnika == "włączony":
            self._predkosc += ile

    def zwolnij(self, ile):
        self._predkosc -= ile
        if self._predkosc < 0:
            self._predkosc = 0

    def pokaz_informacje(self):
        print(f"Marka: {self._marka}")
        print(f"Prędkość: {self._predkosc} km/h")
        print(f"Stan silnika: {self.__stan_silnika}")