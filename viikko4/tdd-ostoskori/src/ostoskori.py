from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.kaikki_ostokset = {}

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2
        maara = 0
        for ostos in self.kaikki_ostokset:
            maara += self.kaikki_ostokset[ostos].lukumaara()
        return maara

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        hinta = 0
        for ostos in self.kaikki_ostokset:
            hinta += self.kaikki_ostokset[ostos].hinta()
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if lisattava.nimi() not in self.kaikki_ostokset:
            self.kaikki_ostokset[lisattava.nimi()] = Ostos(lisattava)
        else:
            self.kaikki_ostokset[lisattava.nimi()].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        self.kaikki_ostokset[poistettava.nimi()].muuta_lukumaaraa(-1)
        if self.kaikki_ostokset[poistettava.nimi()].lukumaara() == 0:
            del self.kaikki_ostokset[poistettava.nimi()]

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self.kaikki_ostokset = {}

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return list(self.kaikki_ostokset.values())
