from varasto import Varasto
from pankki import Pankki
from ostoskori import Ostoskori
from viitegeneraattori import Viitegeneraattori

from varasto import the_varasto_olio
from pankki import the_pankki_olio
from viitegeneraattori import the_viitegeneraattori_olio

class Kauppa:
    """
    def __init__(self):
        self._varasto = Varasto.get_instance()
        self._pankki = Pankki.get_instance()
        self._viitegeneraattori = Viitegeneraattori.get_instance()
        self._kaupan_tili = "33333-44455"
    """
    """
    def __init__(self, varasto, pankki, viitegeneraattori):
        self._varasto = varasto
        self._pankki = pankki
        self._viitegeneraattori = viitegeneraattori
        self._kaupan_tili = "33333-44455"
    """
    def __init__(self, varasto=the_varasto_olio, pankki=the_pankki_olio, viitegeneraattori=the_viitegeneraattori_olio):
        self._varasto = varasto
        self._pankki = pankki
        self._viitegeneraattori = viitegeneraattori
        self._kaupan_tili = "33333-44455"

    def aloita_asiointi(self):
        self._ostoskori = Ostoskori()

    def poista_korista(self, id):
        tuote = self._varasto.hae_tuote(id)
        self._ostoskori.poista(tuote)
        self._varasto.palauta_varastoon(tuote)

    def lisaa_koriin(self, id):
        if self._varasto.saldo(id) > 0:
            tuote = self._varasto.hae_tuote(id)
            self._ostoskori.lisaa(tuote)
            self._varasto.ota_varastosta(tuote)

    def tilimaksu(self, nimi, tili_numero):
        viite = self._viitegeneraattori.uusi()
        summa = self._ostoskori.hinta()

        return self._pankki.tilisiirto(nimi, viite, tili_numero, self._kaupan_tili, summa)
