from abc import ABC, abstractmethod
class Instrument(ABC):
    @abstractmethod
    def graj(self):
        pass

class Gitara(Instrument):
    def graj(self):
        return "Gitara gra"
    
class Fortepian(Instrument):
    def graj(self):
        return "Fortepian gra"
    
g = Gitara()
f = Fortepian()

print(g.graj())
print(f.graj())
