from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset = {}

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2
        return sum([self._ostokset[ostos].lukumaara() for ostos in self._ostokset])

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        return sum([self._ostokset[ostos].hinta() for ostos in self._ostokset])

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        nimi = lisattava.nimi()
        if nimi not in self._ostokset:
            self._ostokset[nimi] = Ostos(lisattava)
        else:
            self._ostokset[nimi].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        nimi = poistettava.nimi()
        self._ostokset[nimi].muuta_lukumaaraa(-1)
        if self._ostokset[nimi].lukumaara() == 0:
            del self._ostokset[nimi]

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self._ostokset = {}

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return list(self._ostokset.values())
