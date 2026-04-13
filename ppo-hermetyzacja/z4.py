class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self._cena = cena

    @property
    def cena(self):
        return self._cena

    @cena.setter
    def cena(self, nowa_cena):
        if nowa_cena >= 0:
            self._cena = nowa_cena