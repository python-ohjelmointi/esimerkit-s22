'''
Testit voidaan suorittaa komennolla:
python3 -m doctest -v eniten_kirjainta.py
'''


def eniten_kirjainta(teksti: str) -> str:
    '''
    >>> eniten_kirjainta('esimerkkimerkkijonokki')
    'k'
    >>> eniten_kirjainta('abcbdbe')
    'b'
    >>> eniten_kirjainta('👍👎👍😂🙀')
    '👍'
    '''
    yleisin = teksti[0]  # sopivimman säilyttäjä

    # käydään läpi (iteroidaan) ja asetetaan yleisin, jos löydetään joku, joka
    # on yleisempi kuin nyt tiedossa oleva:
    for kirjain in teksti:
        if teksti.count(kirjain) > teksti.count(yleisin):
            yleisin = kirjain

    return yleisin


if __name__ == '__main__':
    print(eniten_kirjainta('abcbdbe'))
    print(eniten_kirjainta('esimerkkimerkkijonokki'))
