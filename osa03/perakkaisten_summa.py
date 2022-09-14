mihin_asti = 18

# oikea vastaus on 21
summa = 0

# pidetään tässä aina "seuraavaa", kasvatetaan aina, kunnes summa ylittää mihin_asti
seuraava = 1

# rimpsu on laskukaava, esim. '1 + 2 + 3'
rimpsu = ''

# lasketaan yhteen seuraavia, kunnes saavutetaan yläraja:
while summa < mihin_asti:
    summa += seuraava
    rimpsu += f'{seuraava} + '
    seuraava += 1

rimpsu = rimpsu[:-3]

print(f'Laskettiin {rimpsu} = {summa}')
