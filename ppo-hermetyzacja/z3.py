class Uczen:
    def __init__(self, imie):
        self.__imie = imie          
        self.__oceny = []           

    def dodaj_ocene(self, ocena):
        if 1 <= ocena <= 6:
            self.__oceny.append(ocena)

    @property
    def srednia(self):
        if not self.__oceny:
            return 0
        return sum(self.__oceny) / len(self.__oceny)