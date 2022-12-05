#KAPASITEETTI = 5
#OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.tarkista_syotteen_oikeellisuus(kapasiteetti)
        self.tarkista_syotteen_oikeellisuus(kasvatuskoko)

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti #?
        self.alkioiden_lkm = 0 #?

    def tarkista_syotteen_oikeellisuus(self, positiivinen_kokonaisluku):
        if not isinstance(positiivinen_kokonaisluku, int) or positiivinen_kokonaisluku <= 0:
            raise Exception("Epäkelpo syöte.")

    def kuuluu(self, alkio):                  #ko_alkio_int_joukkoon(self, alkio):
        return not self.alkion_indeksi_int_joukossa(alkio) == -1
        """
        for i in self.lukujono:
            if i == alkio:
                return list.index(i)
                #return True
        
        #return False
        return -1
        """

    def alkion_indeksi_int_joukossa(self, alkio):
        for i in range(0, self.alkioiden_lkm):
            if self.lukujono[i] == alkio:
                return i

        return -1
        """
        for i in self.lukujono:
            if i == alkio:
                return list.index(i)
                #return True
        
        #return False
        return -1
        """

    def int_lukujonon_kapasiteetti_on_taynna(self):
        return self.alkioiden_lkm == self.kapasiteetti

    #kopioi_uusi_lukujono_ja_lisaa_kasvatuskokoa()


    def luo_uusi_lukujono_kasvatuskoon_lisaamalla_kapasiteetilla(self):
        uusi_lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko) #?

        self.kopioi_lukujono(self.lukujono, uusi_lukujono)

        return uusi_lukujono


    def kopioi_lukujono(self, alkuperainen_lukujono, uusi_lukujono):
        for i in range(0, len(alkuperainen_lukujono)):
            uusi_lukujono[i] = alkuperainen_lukujono[i]




    def lisaa(self, alkio):                           # _alkio_int_joukkoon(self, alkio): #(self, n):
        if self.alkioiden_lkm == 0:
            self.lukujono[0] = alkio
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True

        if not self.kuuluu(alkio):                      #ko_alkio_int_joukkoon(alkio):

            print("#")
            print(not self.kuuluu(alkio))
            print(alkio)
            print()

            if self.int_lukujonon_kapasiteetti_on_taynna():

                print("##")
                print(self.int_lukujonon_kapasiteetti_on_taynna())
                print()


                self.lukujono = self.luo_uusi_lukujono_kasvatuskoon_lisaamalla_kapasiteetilla()
                #self.kapasiteetti += self.kapasiteetti
                self.kapasiteetti += self.kasvatuskoko
            
            print("###")
            print(self.to_int_list())
            print(self.alkioiden_lkm)
            print()

            self.lukujono[self.alkioiden_lkm] = alkio       #INDEX ERROR?
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            return True

        return False




    def siirra_int_joukon_alkioita_oikealta_indeksiin(self, indeksi):
        for j in range(indeksi, self.alkioiden_lkm - 1): # - 1 ?
                self.lukujono[j] = self.lukujono[j + 1]

        self.lukujono[self.alkioiden_lkm - 1] = 0
        
        self.alkioiden_lkm = self.alkioiden_lkm - 1 # Tässä ok?

        """
                apu = self.ljono[j]
                self.ljono[j] = self.ljono[j + 1]
                self.ljono[j + 1] = apu
                """




    def poista(self, alkio):                  #    _alkio_int_joukosta(self, alkio):

        #alkion_indeksi = self.alkion_indeksi_int_joukkossa(self, alkio)

        if self.kuuluu(alkio):              #ko_alkio_int_joukkoon(alkio):
            alkion_indeksi = self.alkion_indeksi_int_joukossa(alkio)
            self.siirra_int_joukon_alkioita_oikealta_indeksiin(alkion_indeksi)

            #self.alkioiden_lkm = self.alkioiden_lkm - 1 # Kaikk, EDELLISESSÄ METODISSA OK?

            return True

        return False



    def mahtavuus(self):
        return self.alkioiden_lkm

    ##?
    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu





    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        yhdiste_joukko = IntJoukko()
        #x = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()

        for i in range(0, len(a_taulu)):
            yhdiste_joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdiste_joukko.lisaa(b_taulu[i])

        return yhdiste_joukko

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        leikkaus_joukko = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus_joukko.lisaa(b_taulu[j])

        return leikkaus_joukko

    @staticmethod
    def erotus(joukko_a, joukko_b):
        erotus_joukko = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()

        for i in range(0, len(a_taulu)):
            erotus_joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            erotus_joukko.poista(b_taulu[i])

        return erotus_joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos










        """
        kohta = -1
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.ljono[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.ljono[j]
                self.ljono[j] = self.ljono[j + 1]
                self.ljono[j + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False
        """









        """
        ei_ole = 0

        if self.alkioiden_lkm == 0:
            self.ljono[0] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        else:
            pass

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_taulukko(self.ljono, taulukko_old)
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)

            return True

        return False
        """

"""
class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        on = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                on = on + 1

        if on > 0:
            return True
        else:
            return False

    def lisaa(self, n):
        ei_ole = 0

        if self.alkioiden_lkm == 0:
            self.ljono[0] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        else:
            pass

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_taulukko(self.ljono, taulukko_old)
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)

            return True

        return False
#
    def poista(self, n):
        kohta = -1
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.ljono[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.ljono[j]
                self.ljono[j] = self.ljono[j + 1]
                self.ljono[j + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False


#
    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu
#
    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
"""