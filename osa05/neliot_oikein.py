'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''


def poimi_nelio(sudoku: list, rivi_nro: int, sarake_nro: int) -> list:
    '''
    >>> poimi_nelio([
    ...     [0, 0, 0, 0, 0],
    ...     [0, 1, 2, 3, 0],
    ...     [0, 4, 5, 6, 0],
    ...     [0, 6, 7, 8, 0],
    ...     [0, 0, 0, 0, 0]
    ... ], 1, 1)
    [1, 2, 3, 4, 5, 6, 6, 7, 8]
    '''
    numerot = []
    for rivi in sudoku[rivi_nro: rivi_nro + 3]:
        sarakkeet = rivi[sarake_nro: sarake_nro + 3]
        numerot += sarakkeet
    return numerot


def numerot_ok(numerot: list) -> bool:
    '''
    >>> numerot_ok([0, 0, 0, 0, 0, 0, 0, 0, 0,])
    True
    >>> numerot_ok([1, 2, 3, 4, 5, 6, 7, 8, 9])
    True
    >>> numerot_ok([0, 0, 0, 1, 1, 2, 0, 0, 0])
    False
    '''
    for luku in range(1, 10):
        if numerot.count(luku) > 1:
            return False
    return True


def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int) -> bool:
    numerot = poimi_nelio(sudoku, rivi_nro, sarake_nro)
    return numerot_ok(numerot)


if __name__ == '__main__':
    testisudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(nelio_oikein(testisudoku, 0, 0))  # False
    print(nelio_oikein(testisudoku, 1, 2))  # True
