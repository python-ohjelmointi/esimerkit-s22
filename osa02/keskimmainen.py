'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''

k1 = input('Anna 1. kirjain: ')
k2 = input('Anna 2. kirjain: ')
k3 = input('Anna 3. kirjain: ')

keskimmainen = None

if k1 >= k2 >= k3 or k1 <= k2 <= k3:
    keskimmainen = k2
elif k2 <= k1 <= k3 or k2 >= k1 >= k3:
    keskimmainen = k1
else:
    keskimmainen = k3

print(f'Keskimmäinen kirjain on {keskimmainen}')
