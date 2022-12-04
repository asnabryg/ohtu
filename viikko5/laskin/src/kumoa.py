
class Kumoa:
    def __init__(self, sovelluslogiikka, edellinen_komento):
        self._sovelluslogiikka = sovelluslogiikka
        self.edellinen_komento = edellinen_komento

    def suorita(self):
        komento = self.edellinen_komento()
        komento.kumoa()
