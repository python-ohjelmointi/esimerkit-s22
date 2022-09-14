'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''

# "kiintoarvo", tätä ei tulla muuttamaan:
vuosi = int(input('Vuosi: '))

# "askeltaja" pitää kirjaa kokeiltavista vuosista:
seuraava = vuosi + 1

while not (seuraava % 4 == 0 and (seuraava % 100 != 0 or seuraava % 400 == 0)):
    seuraava += 1

print(f'Vuotta {vuosi} seuraava karkausvuosi on {seuraava}')
