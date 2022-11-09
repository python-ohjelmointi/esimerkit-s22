'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''


def luku_tekstina(luku: int) -> str:
    '''
    luku_tekstina muodostaa merkkijonon yksittäisestä
    kokonaisluvusta:

    >>> luku_tekstina(0)
    'nolla'
    >>> luku_tekstina(10)
    'kymmenen'
    >>> luku_tekstina(45)
    'neljäkymmentäviisi'
    '''
    ykkoset = luku % 10
    kympit = luku // 10
    tekstina = ('nolla', 'yksi', 'kaksi', 'kolme', 'neljä', 'viisi',
                'kuusi', 'seitsemän', 'kahdeksan', 'yhdeksän')

    if luku < 10:
        return tekstina[ykkoset]
    if luku == 10:
        return 'kymmenen'
    if luku < 20:
        return f'{tekstina[ykkoset]}toista'
    if ykkoset == 0:
        return f'{tekstina[kympit]}kymmentä'

    return f'{tekstina[kympit]}kymmentä{tekstina[ykkoset]}'


def lukukirja() -> dict:
    luvut = {}
    for i in range(100):
        luvut[i] = luku_tekstina(i)
    return luvut


if __name__ == '__main__':
    sanakirja = lukukirja()  # lukukirja() palauttaa 'dict'-tyyppisen tuloksen

    print(sanakirja)
    print(sanakirja[45])
