'''
Tämä tiedosto voidaan importoida ilman sivuvaikutuksia, koska
print- ja input-kutsut ovat if-ehtorakenteen sisällä, ja ne
suoritetaan vain kun tämä moduuli on ns. pääohjelma.
'''


def tee_tunnus(etunimi, sukunimi):
    tunnari = etunimi[:3] + sukunimi[:3]
    return tunnari.lower()


if __name__ == '__main__':
    print(tee_tunnus('Pytnikki', 'Honkanen'))

    etu = input('Syötä etunimi: ')
    suku = input('Syötä sukunimi: ')
    tunnus = tee_tunnus(etu, suku)

    print(f'Tunnus on {tunnus}')
