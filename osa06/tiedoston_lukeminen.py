from pathlib import Path

# Tiedoston *absoluuttinen* polku voidaan selvittää
# Path-luokan ja __file__ -muuttujan avulla:
tiedosto = Path(__file__).parent / 'esimerkki.txt'

# Tiedoston sisältö voidaan lukea helposti *read_text*-metodilla:
sisalto = tiedosto.read_text(encoding='UTF-8')

# Tulostetaan (tässä vaiheessa sisältö on tavallinen merkkijono)
print(sisalto)
