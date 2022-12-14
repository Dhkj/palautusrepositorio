from kauppa import Kauppa
from kirjanpito import Kirjanpito

from varasto import Varasto
from pankki import Pankki
from ostoskori import Ostoskori
from viitegeneraattori import Viitegeneraattori

from kirjanpito import the_kirjanpito_olio

def main():
    """
    viitegeneraattori = Viitegeneraattori()
    kirjanpito = Kirjanpito()
    varasto = Varasto(kirjanpito)
    pankki = Pankki(kirjanpito)
    """
    kauppa = Kauppa()
    """
    kauppa = Kauppa(
        Varasto.get_instance(),
        Pankki.get_instance(),
        Viitegeneraattori.get_instance()
    )
    """
    """
    kauppa = Kauppa(varasto, pankki, viitegeneraattori)
    """
    # kauppa hoitaa yhden asiakkaan kerrallaan seuraavaan tapaan:
    kauppa.aloita_asiointi()
    kauppa.lisaa_koriin(1)
    kauppa.lisaa_koriin(3)
    kauppa.lisaa_koriin(3)
    kauppa.poista_korista(1)
    kauppa.tilimaksu("Pekka Mikkola", "1234-12345")

    # seuraava asiakas
    kauppa.aloita_asiointi()

    for _ in range(0, 24):
        kauppa.lisaa_koriin(5)

    kauppa.tilimaksu("Arto Vihavainen", "3425-1652")

    # kirjanpito
    """
    for tapahtuma in Kirjanpito.get_instance().tapahtumat:
        print(tapahtuma)
    """
    """
    for tapahtuma in kirjanpito.tapahtumat:
        print(tapahtuma)
    """
    for tapahtuma in the_kirjanpito_olio.tapahtumat:
        print(tapahtuma)

if __name__ == "__main__":
    main()
