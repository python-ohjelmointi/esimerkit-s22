# tuple eli monikko voidaan muodostaa seuraavasti:
nimet = 'Kasper', 'Teemu', 'Heikki', 'Jukka'
print(nimet)

# pituus yms. operaatiot toimivat aivan kuten listoilla:
print(len(nimet))

for n in nimet[:2]:
    print(f'* {n}')

koordinaatti = 4, 7  # sama kuin (4, 7)
print(koordinaatti)

i = 4
j = 7

# muuttujien vaihtaminen päittäin:
i, j = j, i
print(i, j)

piste = 10, 15  # x ja y

# "unpack" operaatio purkaa kokoelman yksittäisiin muuttujiin:
# (https://medium.com/geekculture/python-packing-and-unpacking-ff0ae8ca6702)
x, y = piste

print('x', x)
print('y', y)
print(type(piste))

# tähti eli * kokoaa loput arvot uuteen listaan
a, b, c, d, *loput = 'XYZWÅÄÖ💣'
print('a', a)
print('b', b)
print(loput)
