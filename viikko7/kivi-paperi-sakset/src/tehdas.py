from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_tekoaly import KPSTekoaly


class Tehdas:
    @staticmethod
    def luo_kps_pelaaja_vs_pelaaja():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def luo_kps_pelaaja_vs_tekoaly():
        return KPSTekoaly()

    @staticmethod
    def luo_kps_pelaaja_vs_parempi_tekoaly(muisti):
        return KPSParempiTekoaly(muisti)
