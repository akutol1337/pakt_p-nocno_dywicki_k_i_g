class Uczen:
    def __init__(self, imię, lista_ocen):
        self.__imię = imię
        self.__lista_ocen = lista_ocen

    def dodaj_ocene(self, ocena):
        if ocena >=1 and ocena <= 6:
            self.__lista_ocen += ocena

    @property
    def średnia(self):
        suma = 0
        i=0
        for each in range(len(self.__lista_ocen)):
            suma += self.__lista_ocen[each]
            i+=1
        self.__średnia = suma/i
        return self.__średnia

uczeń = Uczen('Jan', [1,2,3,4,5,6])
print(uczeń.średnia)