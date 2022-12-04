class Sovelluslogiikka:
    def __init__(self, tulos=[0]):
        self.tulos = tulos
        #self.tulos.append(0)

    def miinus(self, arvo):
        self.tulos.append(self.tulos[len(self.tulos) - 1] - arvo)

        #self.tulos.append(self.tulos.pop() - arvo)
        #self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos.append(self.tulos[len(self.tulos) - 1] + arvo)
        #self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos.append(0)
        #self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos.append(arvo)
        #self.tulos = arvo
    """
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo
    """