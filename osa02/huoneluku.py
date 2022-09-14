
# Esimerkki: käydään läpi peräkkäisiä lukuja:

huoneita = 1  # alustus

print('<select name="huoneita">')

while huoneita <= 10:  # toistoehto
    print(f'  <option value="{huoneita}">{huoneita}</option>')

    # kasvatus
    huoneita += 1

print('</select>')


numero = 1

while numero <= 10:
    print(numero)

    numero += 1

# Lopussa muuttujan arvo on aina *ensimmäinen* jolla ehto oli EPÄTOSI
print(f'Lopussa numero on {numero}')
