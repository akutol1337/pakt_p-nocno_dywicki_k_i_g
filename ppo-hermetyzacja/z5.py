class Pracownik:
    def __init__(self, imie, pensja):
        self.__imie = imie      
        self.__pensja = pensja  

    def get_imie(self):
        return self.__imie

    def set_pensja(self, nowa_pensja):
        if nowa_pensja > 0:
            self.__pensja = nowa_pensja

    def get_pensja(self):
        return self.__pensja