lista = [4, 8, 10, 0]
# -------0--1--2---3

print(lista[::-1])  # [4, 8, 10, 0] => [0, 10, 8, 4]

teksti = 'esimerkkimerkkijono'
print(teksti[::+1])  # "oikein päin" alusta loppuun, yksi askel kerrallaan
print(teksti[::-1])  # "väärin päin" lopusta alkuun, yksi askel kerrallaan
