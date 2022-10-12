'''
Doctest-testejä voidaan kirjoittaa kommentteihin, jotka suoritetaan Pythonin
doctest-moduulilla:

Lukuvälejä voidaan muodostaa seuraavasti:

>>> range(10)
range(0, 10)

Lukuväleistä voidaan muodostaa listoja list-"funktiolla":

>>> list(range(1, 10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]

Lukuväleille voidaan määritellä ala- ja ylärajat sekä askel, ja askellus voi olla negatiivinen:
>>> list(range(10, 0, -2))
[10, 8, 6, 4, 2]

Merkkijonot ovat myös iteroitavia:

>>> for k in 'abc':
...    print(k)
a
b
c

Range-oliot ovat erittäin tehokkaita, koska ne eivät muodosta koko joukkoa kerralla,
vaan yhden arvon kerrallaan:

>>> r = range(100_000_000_000_000)
>>> len(r)
100000000000000
'''
