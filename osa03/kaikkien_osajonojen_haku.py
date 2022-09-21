'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''

sana = input('Sana: ')
merkki = input('Merkki: ')

i = 0
while i <= len(sana) - 3:
    osajono = sana[i:i+3]

    if osajono.startswith(merkki):
        print(osajono)

    i += 1
