from datetime import datetime

kk = datetime.now().month

if 11 >= kk >= 9:
    vuodenaika = 'syksy'
elif 8 >= kk >= 6:
    vuodenaika = 'kesä'
elif 5 >= kk >= 3:
    vuodenaika = 'kevät'
else:
    vuodenaika = 'talvi'


print(f'Nykyinen kuukausi: {kk}, vuodenaika: {vuodenaika}')
