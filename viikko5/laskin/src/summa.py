
class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote
        self.arvo = 0

    def suorita(self):
        self.arvo = int(self.lue_syote())
        print(self.arvo)
        self._sovelluslogiikka.plus(self.arvo)
    
    def kumoa(self):
        self._sovelluslogiikka.miinus(self.arvo)
