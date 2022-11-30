'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''

from pathlib import Path


def hae_sanat(hakusana: str) -> list:
    sanat: list = lue_sanat('sanat.txt')

    loydetyt: list = etsi_sanat(sanat, hakusana)

    return loydetyt


def lue_sanat(tiedoston_nimi: str) -> list:
    '''
    Lukee tiedoston ja pilkkoo sen sisältämät sanat listaksi.
    '''
    # Toinen vaihtoehto: tiedosto = Path(tiedoston_nimi)
    tiedosto = Path(__file__).parent / tiedoston_nimi

    sisalto: str = tiedosto.read_text(encoding='utf-8')
    return sisalto.splitlines()


def etsi_sanat(sanat: list, hakusana: str) -> list:
    '''
    Palauttaa uuden listan, jossa on annetulta listata kaikki ne sanat,
    jotka vastaavat annettua hakusanaa.
    '''
    loydetyt = []

    for sana in sanat:
        if sana_vastaa_hakusanaa(sana, hakusana):
            loydetyt.append(sana)

    return loydetyt


def sana_vastaa_hakusanaa(sana: str, hakusana: str) -> bool:
    '''
    Palauttaa True, mikäli annettu sana vastaa annettua hakusanaa.
    Hakusanassa saattaa olla pisteitä tai asteriskeja tehtävänannon
    kuvauksen mukaisesti.
    '''
    if hakusana.startswith('*'):
        loppuosa = hakusana[1:]
        return sana.endswith(loppuosa)

    if hakusana.endswith('*'):
        alkuosa = hakusana[:-1]
        return sana.startswith(alkuosa)

    if len(sana) != len(hakusana):
        return False

    for i, kirjain in enumerate(hakusana):
        if kirjain != '.' and kirjain != sana[i]:
            return False

    # toistossa ei löytynyt yhtään eroavaa kirjainta, joten sana vastaa haettua:
    return True


def main():
    hakusana = input('Anna hakusana: ')
    osumat = hae_sanat(hakusana)

    for sana in osumat:
        print(sana)


if __name__ == '__main__':
    main()
