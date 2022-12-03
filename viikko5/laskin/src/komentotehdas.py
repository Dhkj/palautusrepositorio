class Komentotehdas:
    def __init__(self, io):
        self.io = io

    def hae(self, komento):
        if komento == "summa":
            return Summa(self.io)
        elif komento == "tulo":
            return Tulo(self.io)
        elif komento == "nelio":
            return Nelio(self.io)
        elif komento == "lopeta":
            return Lopeta(self.io)

        return Tuntematon(self.io)


class Summa:
    def __init__(self, sovelluslogiikka, funktio):
        self.sovelluslogiikka = sovelluslogiikka
        self.funktio = funktio

    def suorita(self):
        arvo = int(self.funktio)

        self.sovelluslogiikka.plus(arvo)

        #self.io.kirjoita(f"Vastaus: {luku1 + luku2}")









"""
class Summa:
    def __init__(self, io):
        self.io = io

    def suorita(self):
        luku1 = int(self.io.lue("Luku 1:"))
        luku2 = int(self.io.lue("Luku 2:"))

        self.io.kirjoita(f"Vastaus: {luku1 + luku2}")

class Nelio:
    def __init__(self, io):
        self.io = io

    def suorita(self):
        luku = int(self.io.lue("Luku 1:"))

        self.io.kirjoita(f"Vastaus: {luku * luku}")

class Tuntematon:
    def __init__(self, io):
        self.io = io

    def suorita(self):
        self.io.kirjoita("Sallitut komennot: summa, tulo, nelio, lopeta")

class Lopeta:
    def __init__(self, io):
        self.io = io

    def suorita(self):
        self.io.kirjoita("Kiitos ja näkemiin!")
        sys.exit(0)
"""