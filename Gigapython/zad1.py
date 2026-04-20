class Osoba:
    def __init__(self, wiek):
        self._wiek = wiek

class Pracownik(Osoba):
    def __init__(self, wiek):
        super().__init__(wiek)
    
    def czy_emeryt(self):
        if self._wiek >= 65:
            print('emeryt')
            return True
        else:
            print('nie emeryt')
            return False
         
pracownik = Pracownik(65)
pracownik.czy_emeryt()