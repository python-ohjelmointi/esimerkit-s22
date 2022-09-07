'''
Tämä esimerkki on lainattu mooc.fi:stä.
https://ohjelmointi-22.mooc.fi/osa-2/3-ehtojen-yhdist%C3%A4minen
CC-BY-NC-SA
'''

n1 = int(input("Anna luku 1: "))
n2 = int(input("Anna luku 2: "))
n3 = int(input("Anna luku 3: "))
n4 = int(input("Anna luku 4: "))
n5 = int(input("Anna luku 5: "))
n6 = int(input("Anna luku 6: "))
n7 = int(input("Anna luku 7: "))

# Vaihtoehto: hyödynnetään jotain valmista, joka ratkaisee ongelman
suurin = max(n1, n2, n3, n4, n5, n6, n7)

print(f" {suurin} on suurin luku.")
