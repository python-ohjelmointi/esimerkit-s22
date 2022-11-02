'''
>>> from keskimmaisten_keskiarvo import keskimmaisten_keskiarvo
>>> keskimmaisten_keskiarvo([1, 2, 3, 100])
2.5

>>> keskimmaisten_keskiarvo([1, 1, 5, 1, 4, 1]) # minimi esiintyy monta kertaa
1.75

>>> keskimmaisten_keskiarvo([1, 1, 1, 4, 5]) == 2.0  # funktion pitää palauttaa arvo
True

>>> lista = [3, 2, 3, 1]
>>> keskimmaisten_keskiarvo(lista) # annettu lista ei saa muuttua
2.5
>>> lista # listan tulee olla edelleen [3, 2, 3, 1]
[3, 2, 3, 1]
'''

from statistics import mean


def keskimmaisten_keskiarvo(numerot: list) -> float:
    jarjestetty = sorted(numerot)
    keskimmaiset = jarjestetty[1:-1]

    return mean(keskimmaiset)
