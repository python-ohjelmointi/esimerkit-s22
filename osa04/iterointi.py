# Iterointi tarkoittaa asioiden läpikäyntiä:
# esim. luvut 0-100, tai merkkijonot listalta

# listan läpikäynti yksi arvo kerrallaan:
lista = [0, 1, 2, 3, 4, 5]
for luku in lista:
    print(luku)

teksti = 'esimerkkimerkkijonokki'

# "vaihtoehtoinen tapa" while-luupilla
indeksi = 0
while indeksi < len(teksti):
    kirjain = teksti[indeksi]
    print(kirjain)
    indeksi += 1

# merkkijonon läpikäynti yksi merkki kerrallaan:
for kirjain in teksti:
    print(kirjain)

# esimerkki kirjainten laskemisesta:
eniten_maara = 0
eniten_kirjain = ''

for kirjain in teksti:
    maara = teksti.count(kirjain)

    if eniten_maara < maara:
        eniten_maara = maara
        eniten_kirjain = kirjain

print(
    f'Suurin yksittäisen kirjaimen määrä oli {eniten_maara}, kirjain oli {eniten_kirjain}')
