'''
Ongelma tässä tiedostossa on se, että tee_tunnus-funktiota
ei voida importoida toisiin tiedostoihin ilman, että tämän
moduulin kysymyksiä ja printtejä suoritetaan!!!!1!!
'''


def tee_tunnus(etunimi, sukunimi):
    tunnari = etunimi[:3] + sukunimi[:3]
    return tunnari.lower()


print(tee_tunnus('Pytnikki', 'Honkanen'))

etu = input('Syötä etunimi: ')
suku = input('Syötä sukunimi: ')
tunnus = tee_tunnus(etu, suku)

print(f'Tunnus on {tunnus}')
