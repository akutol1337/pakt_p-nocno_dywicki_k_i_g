class Osoba:
    def __init__(self, wiek):
        self._wiek = wiek  


class Pracownik(Osoba):
    def czy_emeryt(self):
        return self._wiek >= 65