
# tarvitaan keino "dynamiisesti" muodostaa "numerosarjoja":
for luku in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(luku)

print('~' * 60)

alaraja = 1
ylaraja = 8
askel = 2

for luku in range(alaraja, ylaraja, askel):
    print(luku)

print('~' * 60)

# Määritellään todella iso lukuväli:
iso_vali = range(16 * 1_024 * 1_024 * 1_024)
print(iso_vali)
# tämä ei onnistuisi esim. listalla

for i in iso_vali:
    print(i)
    if i >= 10:
        break

print(range(10))
print(list(range(10)))
