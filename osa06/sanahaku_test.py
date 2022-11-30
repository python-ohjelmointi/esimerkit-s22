# pylint: disable=use-implicit-booleaness-not-comparison,singleton-comparison

'''
Tässä Python-tiedostossa olevat *yksikkötestit* voidaan ajaa Pytest-työkalulla:
$ pip install pytest
$ pytest
'''

from sanahaku import lue_sanat, etsi_sanat, sana_vastaa_hakusanaa


def test_lue_sanat_palauttaa_listan_sanoja():
    sanat = lue_sanat('sanat.txt')

    assert sanat[0] == 'a'
    assert sanat[-1] == 'zyzzyvas'


def test_lue_sanat_ymmartaa_skandit():
    sanat = lue_sanat('testisanat.txt')

    assert sanat[0] == 'päällikkö'


def test_etsi_sanat_loytaa_yhden_sanan():
    hakusana = 'jupiter'
    sanat = ['a', 'jupiter', 'zyzzyvas']

    tulos = etsi_sanat(sanat, hakusana)

    assert isinstance(sanat, list)
    assert len(tulos) == 1
    assert tulos[0] == 'jupiter'


def test_etsi_sanat_palauttaa_listan_jos_hakusanaa_ei_loydy():
    hakusana = 'päällikkö 🤘'
    sanat = ['a', 'jupiter', 'zyzzyvas']

    tulos = etsi_sanat(sanat, hakusana)

    assert tulos == []


def test_etsi_sanat_ottaa_pisteen_huomioon():
    sanat = ['cat', 'car', 'carrot', 'banana', 'sane', 'care', 'late']

    # testataan yhdellä pisteellä
    tulos = etsi_sanat(sanat, 'ca.')
    assert tulos == ['cat', 'car']

    # testataan kahdella pisteellä
    tulos = etsi_sanat(sanat, '.a.e')
    assert tulos == ['sane', 'care', 'late']


def test_sana_jossa_asteriski_alussa():
    tulos = sana_vastaa_hakusanaa('aeroplane', '*ane')

    assert tulos == True


def test_sana_jossa_asteriski_lopussa():
    tulos = sana_vastaa_hakusanaa('aeroplane', 'aero*')

    assert tulos == True
