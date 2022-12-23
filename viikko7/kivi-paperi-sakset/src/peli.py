from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class Peli:
    @staticmethod
    def luo_peli_ihmista_vastaan():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def luo_peli_tekoalya_vastaan():
        return KPSTekoaly()

    @staticmethod
    def luo_peli_parannettua_tekoalya_vastaan():
        return KPSParempiTekoaly()