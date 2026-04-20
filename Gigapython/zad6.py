class Samochod:
    def __init__(self, marka, predkosc, stan_silnika):
        self._marka = marka
        self._predkosc = predkosc
        self.__stan_silnika = stan_silnika

    def wlacz_silnik(self):
        self.__stan_silnika = 'włączony'
        print(self.__stan_silnika)

    def wylacz_silnik(self):
        self.__stan_silnika = 'wyłączony'
        print(self.__stan_silnika)

    def przyspiesz(self, ile):
        if self.__stan_silnika == 'włączony':
            self._predkosc += ile
        print(self._predkosc)

    def zwolnij(self, ile):
        if self._marka != 'Fiat':
            self._predkosc -= ile
        else:
            print('FIAT NIGDY NIE ZWALNIA')
            self._predkosc += 2*ile
        print(self._predkosc)

    def pokaz_informacje(self):
        if self._marka != 'Fiat':
            print(self._marka)
            print(self._predkosc)
            print(self.__stan_silnika)
        else:
            print('KTO NIE ZNA FIATA NIE MA GIATA!')

samochód = Samochod('Fiat', 2000, 'włączony')
samochód.wylacz_silnik()
samochód.wlacz_silnik()
samochód.przyspiesz(2000)
samochód.zwolnij(2000)
samochód.pokaz_informacje()