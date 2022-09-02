'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''

from math import ceil


opiskelijoita = int(input('Montako opiskelijaa? '))
ryhman_koko = int(input('Mikä on ryhmän koko? '))

# vaihtoehtoisia tapoja: https://stackoverflow.com/a/43292557
maara = ceil(opiskelijoita / ryhman_koko)

print(f'Ryhmien määrä: {maara}')
