# pylint: disable=redefined-outer-name,unused-variable

# tämä muuttuja on ns. "globaali"
nimi = 'Pentti'


def vaihda_nimi():
    nimi = 'Antti'


print(nimi)  # Pentti
vaihda_nimi()
print(nimi)  # Antti vai Pentti?

# Vikalla rivillä tulostuu Pentti, koska vaihda_nimi funktion
# sisällä luodaan uusi paikallinen muuttuja `nimi`.
