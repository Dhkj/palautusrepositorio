class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.tarkista_syotteen_oikeellisuus(kapasiteetti)
        self.tarkista_syotteen_oikeellisuus(kasvatuskoko)

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def tarkista_syotteen_oikeellisuus(self, positiivinen_kokonaisluku):
        if not isinstance(positiivinen_kokonaisluku, int) or positiivinen_kokonaisluku <= 0:
            raise Exception("Epäkelpo syöte.")

    def kuuluu(self, alkio):
        return not self.alkion_indeksi_int_joukossa(alkio) == -1

    def alkion_indeksi_int_joukossa(self, alkio):
        for i in range(0, self.alkioiden_lkm):
            if self.lukujono[i] == alkio:
                return i

        return -1

    def int_lukujonon_kapasiteetti_on_taynna(self):
        return self.alkioiden_lkm == self.kapasiteetti

    def luo_uusi_lukujono_kasvatuskoon_lisaamalla_kapasiteetilla(self):
        uusi_lukujono = [0] * (self.kapasiteetti + self.kasvatuskoko)

        self.kopioi_lukujono(self.lukujono, uusi_lukujono)

        return uusi_lukujono

    def kopioi_lukujono(self, alkuperainen_lukujono, uusi_lukujono):
        for i in range(0, len(alkuperainen_lukujono)):
            uusi_lukujono[i] = alkuperainen_lukujono[i]

    def lisaa(self, alkio):
        """
        if self.alkioiden_lkm == 0:
            self.lukujono[0] = alkio
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        """
        if not self.kuuluu(alkio):
            if self.int_lukujonon_kapasiteetti_on_taynna():
                self.lukujono = self.luo_uusi_lukujono_kasvatuskoon_lisaamalla_kapasiteetilla()
                self.kapasiteetti += self.kasvatuskoko
            
            self.lukujono[self.alkioiden_lkm] = alkio
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            return True

        return False

    def siirra_int_joukon_alkioita_oikealta_indeksiin(self, indeksi):
        for j in range(indeksi, self.alkioiden_lkm - 1):
                self.lukujono[j] = self.lukujono[j + 1]

        self.lukujono[self.alkioiden_lkm - 1] = 0        
        self.alkioiden_lkm = self.alkioiden_lkm - 1

    def poista(self, alkio):
        if self.kuuluu(alkio):
            alkion_indeksi = self.alkion_indeksi_int_joukossa(alkio)
            self.siirra_int_joukon_alkioita_oikealta_indeksiin(alkion_indeksi)
            return True

        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        yhdiste_joukko = IntJoukko()
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
        """
        string = "{"
        string += str(self.to_int_list())
        string += "}"

        return string
        """
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
        