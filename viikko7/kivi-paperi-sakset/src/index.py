from peli import Peli
""" Pois ok?
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
"""

def main():
    #kaksinpeli = Peli()

    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            kaksinpeli = Peli.luo_peli_ihmista_vastaan()
            #kaksinpeli = KPSPelaajaVsPelaaja()
            kaksinpeli.pelaa()
        elif vastaus.endswith("b"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            yksinpeli = Peli.luo_peli_tekoalya_vastaan()
            #yksinpeli = KPSTekoaly()
            yksinpeli.pelaa()
        elif vastaus.endswith("c"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            haastava_yksinpeli = Peli.luo_peli_parannettua_tekoalya_vastaan()
            #haastava_yksinpeli = KPSParempiTekoaly()
            haastava_yksinpeli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
