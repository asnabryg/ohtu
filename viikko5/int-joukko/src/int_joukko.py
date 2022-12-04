KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetin on oltava numero joka vähintään 1")
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kasvatuskoon on oltava numero joka vähintään 1")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lista = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, number):
        for n in self.lista:
            if n == number:
                return True
        return False

    def lisaa(self, number):
        if self.kuuluu(number):
            return False

        self.lista[self.alkioiden_lkm] = number
        self.alkioiden_lkm += 1

        if self.alkioiden_lkm % len(self.lista) == 0:
            taulukko_old = self.lista
            self.kopioi_lista(self.lista, taulukko_old)
            self.lista = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_lista(taulukko_old, self.lista)

        return True

    def poista(self, number):
        poistettu = False
        for i in range(0, len(self.lista) - 1):
            if not poistettu:
                if self.lista[i] == number:
                    self.lista[i] = self.lista[i + 1]
                    self.alkioiden_lkm -= 1
                    poistettu = True
            else:
                self.lista[i] = self.lista[i + 1]

        return poistettu

    def kopioi_lista(self, kopioitava_lista, kopio):
        for i in range(0, len(kopioitava_lista)):
            kopio[i] = kopioitava_lista[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        lista = [0] * self.alkioiden_lkm
        for i in range(0, len(lista)):
            lista[i] = self.lista[i]
        return lista

    @staticmethod
    def yhdiste(a, b):
        joukko = IntJoukko()
        for number in a.to_int_list():
            joukko.lisaa(number)
        for number in b.to_int_list():
            joukko.lisaa(number)
        return joukko

    @staticmethod
    def leikkaus(a, b):
        joukko = IntJoukko()
        for number1 in a.to_int_list():
            for number2 in b.to_int_list():
                if number1 == number2:
                    joukko.lisaa(number1)
        return joukko

    @staticmethod
    def erotus(a, b):
        joukko = IntJoukko()
        for number in a.to_int_list():
            joukko.lisaa(number)
        for number in b.to_int_list():
            joukko.poista(number)
        return joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        string = "{"
        for number in self.lista:
            if number > 0:
                string += str(number) + ", "
        string = string[:-2] + "}"
        return string
