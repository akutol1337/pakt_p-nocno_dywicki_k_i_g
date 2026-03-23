class Sprzedawca():
    def __init__(self):
        self.imię = input("Podaj imię sprzedawcy: ")
        self.nazwisko = input("Podaj nazwisko sprzedawcy: ")
        self.kod_sprzedawcy = input("Podaj kod sprzedawcy: ")
        self.do_kiedy_zatrudniony = input("Do kiedy ten sprzedawca jest zatrudniony? (dd-MM-YYYY): ")
        self.dzial = input("Podaj dział, w którym pracuje sprzedawca: ")
        self.wynagrodzenie = float(input("Podaj wynagrodzenie sprzedawcy: "))

    def show_info(self):
        print("Imię: " + self.imię + "\nNazwisko: " + self.nazwisko + "\nKod sprzedawcy: " + self.kod_sprzedawcy + "\nZatrudniony do: " + self.do_kiedy_zatrudniony + "\nDział: " + self.dzial + "\nWynagrodzenie: " + str(self.wynagrodzenie) + "zł")

class KierownikSprzedaży(Sprzedawca):
    def __init__(self):
        super().__init__()
        self.uprawnienia = input("Podaj uprawnienia kierownika sprzedaży: ")
        self.dodatek_funkcyjny = float(input("Podaj dodatek funkcyjny kierownika sprzedaży wyrażony w procentach: "))

    def show_info(self):
        print("Imię: " + self.imię + "\nNazwisko: " + self.nazwisko + "\nKod sprzedawcy: " + self.kod_sprzedawcy + "\nZatrudniony do: " + self.do_kiedy_zatrudniony + "\nDział: " + self.dzial + "\nWynagrodzenie: " + str(self.wynagrodzenie) + "zł" + "\nUprawnienia tego kierownika sprzedaży to: " + self.uprawnienia + "\nDodatek funkcyjny tego kierownika sprzedaży to: " + str(self.dodatek_funkcyjny))

    def oblicz_płace_z_uwzględnieniem_dodatku_funkcyjnego(self):
        self.płaca_z_uwzględnieniem_dodatku_funkcyjnego = self.wynagrodzenie * (1+(self.dodatek_funkcyjny)/100)
        print("Płaca z uwzględnieniem dodatku funkcyjnego tego kierownika sprzedaży wynosi: " + str(self.płaca_z_uwzględnieniem_dodatku_funkcyjnego))

def Main():
    kierownikSprzedaży = KierownikSprzedaży()
    kierownikSprzedaży.show_info()
    kierownikSprzedaży.oblicz_płace_z_uwzględnieniem_dodatku_funkcyjnego()
    sprzedawca = Sprzedawca()
    sprzedawca.show_info()

Main()