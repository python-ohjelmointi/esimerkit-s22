'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''


def lisaa_loppuun(numerot: list) -> None:
    num = len(numerot) + 1
    numerot.append(num)


def poista_viimeinen(numerot: list) -> None:
    numerot.pop()  # poistaa viimeisen


lista = []

while True:
    print(f'Lista on nyt {lista}')
    syote = input('(l)isää, (p)oista vai e(x)it: ')

    if syote == 'l':
        lisaa_loppuun(lista)
    elif syote == 'p':
        poista_viimeinen(lista)
    elif syote == 'x':
        print('Moi!')
        break
