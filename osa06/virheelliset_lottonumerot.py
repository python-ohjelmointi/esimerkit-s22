from pathlib import Path

tiedosto = '''
viikko 1;5,7,11,13,23,24,30
viikko 2;9,13,14,24,34,35,37
viikko 100;1,5,13,22,24,25,26
viikko zzc;1,5,13,22,24,25,26
viikko 22;1,**,5,6,13,2b,34
viikko 13;4,6,17,19,24,33
viikko 41;5,12,3,35,12,14,36
'''.strip()


def tarkasta_lottorivi(lottorivi: str) -> bool:
    # lottorivi on esim. 'viikko 1;5,7,11,13,23,24,30'
    try:
        alkuosa, loppuosa = lottorivi.split(';')
        return rivin_alku_ok(alkuosa) and lottonumerot_ok(loppuosa)
    except ValueError:
        return False


def rivin_alku_ok(mjono: str) -> bool:
    _, viikko_str = mjono.split(' ')  # esim. 'viikko 1'
    viikkonumero = int(viikko_str)
    return 52 >= viikkonumero >= 1


def lottonumerot_ok(loppuosa: str) -> bool:
    osat = loppuosa.split(',')

    if len(osat) != 7:
        # ns. "guard clause"
        return False

    kasitellyt = []

    for osa in osat:
        numero = int(osa)
        if numero < 1 or numero > 39 or numero in kasitellyt:
            return False
        kasitellyt.append(numero)

    return True


def suodata_virheelliset():
    rivit = tiedosto.splitlines()

    validit_rivit: str = ''

    for rivi in rivit:
        if tarkasta_lottorivi(rivi):
            validit_rivit += rivi + '\n'

    print(validit_rivit)

    polku = Path('korjatut_numerot.csv')

    if polku.exists():
        vastaus = input(
            'Tiedosto on jo olemassa, haluatko ylikirjoittaa? k/e ')

        if vastaus == 'e':
            return

    polku.write_text(validit_rivit, encoding='utf-8')


if __name__ == '__main__':
    suodata_virheelliset()
