
class Nollaus:
    def __init__(self, sovelluslogiikka, tulos):
        self._sovelluslogiikka = sovelluslogiikka
        self.tulos = tulos
        self.arvo = 0

    def suorita(self):
        self.arvo = int(self.tulos.get())
        self._sovelluslogiikka.nollaa()
    
    def kumoa(self):
        self._sovelluslogiikka.plus(self.arvo)
