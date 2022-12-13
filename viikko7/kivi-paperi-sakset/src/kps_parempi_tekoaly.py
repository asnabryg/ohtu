from tekoaly_parannettu import TekoalyParannettu
from kivi_sakset_paperi import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):

    def __init__(self, muisti):
        self._tekoaly = TekoalyParannettu(muisti)

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
