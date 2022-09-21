'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''

teksti = ''

while True:
    sana = input('Anna sana: ')

    # "guard clause"
    if sana == 'loppu' or teksti.endswith(sana):
        break

    teksti += ' ' + sana

print()
print(teksti.strip())
