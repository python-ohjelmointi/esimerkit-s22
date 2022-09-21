# merkkijonossa toistuu sama osajono:
tunnari = 'nanananananananananananana batman'
print(tunnari)

# merkkijonoa voidaan toistaa * merkillä
tunnari = 'na' * 13 + ' batman'
print(tunnari)

print()  # tyhjä rivi

# toistetaan tähtimerkkiä otsikon pituuden verran:
otsikko = 'Merkkijonojen toistaminen'
print(otsikko)
print('*' * len(otsikko))

print()  # tyhjä rivi

# tulostetaan eri tasoisia esimerkkiotsikoita wiki markupissa:
# https://en.wikipedia.org/wiki/Help:Wikitext#Layout
taso = 1

while taso <= 20:
    merkit = '=' * taso
    print(f'{merkit} Heading {taso} {merkit}')

    taso += 1
