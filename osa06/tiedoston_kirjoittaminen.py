from pathlib import Path

# Tiedoston *absoluuttinen* polku voidaan määrittää
# Path-luokan ja __file__ -muuttujan avulla:
tallennettava = Path(__file__).parent / 'tallennettu.txt'

# Teksti, joka halutaan tallentaa:
lyriikka = 'Apotti apotti\nJou, tervetuloa tähän uuteen skeneen'

# write_text tallentaa sille annetun tekstin Path-oliota vastaavaan tiedostoon:
tulos = tallennettava.write_text(lyriikka, encoding='utf-8')

# Tulostetaan tiedoston polku ja merkkien määrä:
print(f'Tallennettiin tiedostoon {tallennettava} {tulos} merkkiä')
