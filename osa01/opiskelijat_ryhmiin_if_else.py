'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.

Vaihtoehtoinen ratkaisu hyödyntäen if-else-logiikkaa:
'''

opiskelijoita = int(input('Montako opiskelijaa? '))
ryhman_koko = int(input('Mikä on ryhmän koko? '))

jako_tasan = (opiskelijoita % ryhman_koko) == 0

if jako_tasan:
    # Jos jako menee tasan, ratkaisu on:
    maara = opiskelijoita // ryhman_koko
else:
    # Jos jako ei mene tasan, ryhmiä tulee yksi enemmän:
    maara = (opiskelijoita // ryhman_koko) + 1

print(f'Ryhmien määrä: {maara}')
