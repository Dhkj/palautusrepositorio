import unittest
from int_joukko import IntJoukko


def main():
    """
    joukko = IntJoukko()

    joukko.lisaa(1)
    joukko.lisaa(2)
    joukko.lisaa(3)
    joukko.lisaa(2)
    joukko.lisaa(2)
    joukko.lisaa(2)

    joukko.poista(2)

    print(joukko.to_int_list())
    """

    lisattavat = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


    
    joukko_a = IntJoukko()
    joukko_b = IntJoukko(8)
    joukko_c = IntJoukko(10, 20)

    print(joukko_a.to_int_list())
    print()
    print(joukko_b.to_int_list())
    print()
    print(joukko_c.to_int_list())
    print()
    print()

    lisaa(joukko_a)
    lisaa(joukko_b)
    lisaa(joukko_b)

    print(joukko_a.to_int_list())
    print()
    print(joukko_b.to_int_list())
    print()
    print(joukko_c.to_int_list())
    print()
    print()
    """
    self.toimii_kasvatuksen_jalkeen(joukko_a)
    self.toimii_kasvatuksen_jalkeen(joukko_b)
    self.toimii_kasvatuksen_jalkeen(joukko_c)
    """

def lisaa(joukko):
    lisattavat = [1, 2, 4, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    for luku in lisattavat:
        print(luku)
        joukko.lisaa(luku)
        


if __name__ == "__main__":
    main()
