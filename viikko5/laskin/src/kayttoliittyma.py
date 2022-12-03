from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka, self._lue_syote),
            Komento.KUMOA: Kumoa(sovelluslogiikka, self._lue_syote)
        }

    # ...
    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovelluslogiikka.tulos)
        #self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)









    #

    def _lue_syote(self):
        #return self._syote_kentta.get()

        arvo = 0

        try:
            arvo = int(self._syote_kentta.get())
        except Exception:
            pass

        return arvo

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovelluslogiikka.tulos)








#
class Summa:
    def __init__(self, sovelluslogiikka, funktio):
        self.sovelluslogiikka = sovelluslogiikka
        self.funktio = funktio

    def suorita(self):
        """
        arvo = 0 #?

        arvo = self.funktio() #int()
        print(arvo)
        arvo = int(arvo) #int()
        """
        #self.sovelluslogiikka.plus(arvo)
        self.sovelluslogiikka.plus(self.funktio())



        """
        try:
            arvo = int(self._syote_kentta.get())
        except Exception:
            pass
        """

class Erotus:
    def __init__(self, sovelluslogiikka, funktio):
        self.sovelluslogiikka = sovelluslogiikka
        self.funktio = funktio

    def suorita(self):
        self.sovelluslogiikka.miinus(self.funktio())

class Nollaus:
    def __init__(self, sovelluslogiikka, funktio):
        self.sovelluslogiikka = sovelluslogiikka
        self.funktio = funktio

    def suorita(self):
        self.sovelluslogiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka, funktio):
        self.sovelluslogiikka = sovelluslogiikka
        self.funktio = funktio

    def suorita(self):
        pass



"""
class Erotus:
    def __init__(self, sovelluslogiikka, funktio):
        self.sovelluslogiikka = sovelluslogiikka
        self.funktio = funktio

    def suorita(self):
        arvo = int(self.funktio)

        self.sovelluslogiikka.miinus(arvo)
"""

"""
class Nollaus:
    def __init__(self, sovelluslogiikka, funktio):
        self.sovelluslogiikka = sovelluslogiikka
        self.funktio = funktio

    def suorita(self):
        self.sovelluslogiikka.nollaa()

        
        arvo = int(self.funktio)

        self.sovelluslogiikka.plus(arvo)
        
"""
"""
class Kumoa:
    def __init__(self, sovelluslogiikka, funktio):
        self.sovelluslogiikka = sovelluslogiikka
        self.funktio = funktio

    def suorita(self):
        pass
"""


"""

class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _suorita_komento(self, komento):
        arvo = 0

        try:
            arvo = int(self._syote_kentta.get())
        except Exception:
            pass

        if komento == Komento.SUMMA:
            self._sovellus.plus(arvo)
        elif komento == Komento.EROTUS:
            self._sovellus.miinus(arvo)
        elif komento == Komento.NOLLAUS:
            self._sovellus.nollaa()
        elif komento == Komento.KUMOA:
            pass

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos)
    """