'''
Tämä tiedosto sisältää Sudoku-pelin käyttöliittymän, mutta se ei sisällä lainkaan
pelin logiikkaa. Logiikka on toteutettu aikaisemmissa viikkoharjoituksissa, ja
lisäksi pelin tueksi on toteutettu uudet sudoku_valmis-, ja tulosta-funktiot.
Logiikka löytyy tiedostosta sudoku_tarkistin.py.
'''

from sudoku_tarkistin import tulosta, sudoku_oikein, sudoku_valmis


# Sudoku-logo on luotu https://patorjk.com/software/taag/ -palvelussa.
logo = r'''
   _____             __        __
  / ___/ __  __ ____/ /____   / /__ __  __
  \__ \ / / / // __  // __ \ / //_// / / /
 ___/ // /_/ // /_/ // /_/ // ,<  / /_/ /
/____/ \__,_/ \__,_/ \____//_/|_| \__,_/

'''


def kysy_numero(teksti: str) -> int:
    '''
    Pyytää käyttäjää syöttämään kokonaisluvun käyttäen annettua tekstiä.
    Toistaa kysymyksen kunnes saa kelvollisen kokonaisluvun, joka palautetaan.
    '''

    # Toistetaan, kunnes saadaan kelvollinen numero:
    while True:
        try:
            numero = int(input(teksti))
            return numero

        except ValueError as virhe:
            print('Virheellinen numero!')
            print('Voit lopettaa pelin painamalla Ctrl+C')
            print(virhe)


def pelaa_siirto(ruudukko: list) -> None:
    '''
    Kysyy pelaajalta siirron, ja koittaa tehdä sen annetussa ruudukossa.
    Jos siirto ei ole sallittu, se perutaan.
    '''
    rivi = kysy_numero('Syötä rivi (0-8): ')
    sarake = kysy_numero('Syötä sarake (0-8): ')
    numero = kysy_numero('Syötä numero (1-9): ')

    try:
        # Alkuperäinen numero talteen, jotta se voidaan tarvittaessa palauttaa
        alkuperainen = ruudukko[rivi][sarake]

        # Asetetaan käyttäjän antama numero annettuun kohtaan
        ruudukko[rivi][sarake] = numero

        if sudoku_oikein(ruudukko):
            print('OK!')
        else:
            # Perutaan siirto
            print('Ei sallittu numero!')
            ruudukko[rivi][sarake] = alkuperainen

    except IndexError:
        print('Virheellinen rivi tai sarake!')


def pelaa(ruudukko: list):
    print(logo)

    # Toistetaan siirtoja, kunnes peli on valmis:
    while not sudoku_valmis(ruudukko):
        tulosta(ruudukko)
        print()

        try:
            pelaa_siirto(ruudukko)

        except KeyboardInterrupt:
            # Ctrl+C -komento johtaa pelistä poistumiseen
            return False

        print()  # Tyhjä rivi jokaisen siirron jälkeen

    return True


def main():
    # pelin alkutila on lainattu mooc.fi:n esimerkistä
    ruudukko = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    valmis = pelaa(ruudukko)
    print()

    if valmis:
        print('Sait sudokun valmiiksi 🥳:\n')
        tulosta(ruudukko)

    else:
        print('Kiitos pelaamisesta 👋!')


if __name__ == '__main__':
    main()  # käynnistää pelin
