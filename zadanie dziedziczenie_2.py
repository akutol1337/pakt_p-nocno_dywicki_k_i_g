class Pracownik():
    def __init__(self):
        self.imie = input("Podaj imię pracownika: ")
        self.nazwisko = input("Podaj nazwisko pracownika: ")
        self.nip = input("Podaj NIP pracownika: ")
        self.data_urodzenia = input("Podaj datę urodzenia pracownika (format: dd-mm-yyyy): ")
        self.data_zatrudnienia = input("Podaj datę zatrudnienia pracownika (format: dd-mm-yyyy): ")
        self.pensja = float(input("Podaj pensję pracownika: "))
        self.dzial = input("Podaj dział, w którym pracuje pracownik: ")
        
    def show_info(self):
        print("Imię: " + self.imie + "\nNazwisko: " + self.nazwisko + "\nNIP: " + self.nip + "\nData urodzenia: " + self.data_urodzenia + "\nData zatrudnienia: " + self.data_zatrudnienia + "\nPensja: " + str(self.pensja) + "zł\nDział: " + self.dzial)
        
class Kierownik(Pracownik):
    def __init__(self):
        super().__init__()
        self.ilosc_podwladnych = int(input("Podaj ilość podwładnych kierownika: "))
        self.typ_kierownictwa = input("Podaj typ kierownictwa (np. liniowe, sztabowe, funkcjonalne): ")
        self.dodatek_funkcyjny = float(input("Podaj dodatek funkcyjny kierownika wyrażony w procentach: "))

    def show_info(self):
        print("Imię: " + self.imie + "\nNazwisko: " + self.nazwisko + "\nNIP: " + self.nip + "\nData urodzenia: " + self.data_urodzenia + "\nData zatrudnienia: " + self.data_zatrudnienia + "\nPensja: " + str(self.pensja) + "zł\nDział: " + self.dzial + "\nIlość podwładnych: " + str(self.ilosc_podwladnych) + "\nType kierownictwa: " + self.typ_kierownictwa + "\nDodatek funkcyjny: " + str(self.dodatek_funkcyjny))
    
    def add_worker(self):
        self.ilosc_podwladnych += 1
        
def Main():
    kierownik = Kierownik()
    kierownik.show_info()
    kierownik.add_worker()
    
Main()