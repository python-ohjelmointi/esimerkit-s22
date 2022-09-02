rooli = 'anonymous'
on_ratkaissut = False

on_henkilokuntaa = (rooli == 'admin') or (
    rooli == 'teacher') or (rooli == 'assistant')

if on_henkilokuntaa or on_ratkaissut:
    print('Saat katsoa malliratkaisun')
else:
    print('Saat katsoa malliratkaisun kun olet ratkaissut tehtävän itse')
