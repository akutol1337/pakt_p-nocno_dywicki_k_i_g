class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

    @property
    def cena(self):
        return self._cena

    @cena.setter
    def cena(self, value):
        self._cena = value

mleko = Produkt('mleko', 2.50)
print(mleko.cena)
mleko.cena = 4.50
print(mleko.cena)