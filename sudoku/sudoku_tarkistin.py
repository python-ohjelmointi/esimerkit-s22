'''
Tehtävä on lainattu Helsingin yliopiston Ohjelmoinnin perusteet -kurssilta
ohjelmointi-22.mooc.fi, ja se on lisensoitu Creative Commons BY-NC-SA 4.0 -lisenssillä.

Täydennä funktiot omista mooc.fi tehtävien vastauksistasi!
'''

# pylint: disable=unused-argument,fixme


def rivi_oikein(sudoku: list, rivi_nro: int) -> bool:
    # FIXME: Täydennä funktiot omista mooc.fi tehtävien vastauksistasi!
    return True


def sarake_oikein(sudoku: list, sarake_nro: int) -> bool:
    # FIXME: Täydennä funktiot omista mooc.fi tehtävien vastauksistasi!
    return True


def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int) -> bool:
    # FIXME: Täydennä funktiot omista mooc.fi tehtävien vastauksistasi!
    return True


def sudoku_oikein(sudoku: list) -> bool:
    # FIXME: Täydennä funktiot omista mooc.fi tehtävien vastauksistasi!
    return True


def sudoku_valmis(sudoku: list) -> bool:
    '''
    Tarkastaa, että annettu sudoku on kokonaan täytetty ja että se täyttää
    kaikki numeroita koskevat säännöt.
    '''
    for rivi in sudoku:
        if 0 in rivi:
            return False
    return sudoku_oikein(sudoku)


def tulosta(sudoku: list):
    '''
    Tulostaa annetun sudokun siten, että rivit ja sarakkeet on numeroitu.
    Eri "neliöt" sudokussa erotellaan putkilla (|) ja viivoilla (-):

        0 1 2   3 4 5   6 7 8

    0   2 6 7 | 8 3 9 | 5   4
    1   9 8 3 | 5 1   | 6
    2   4 5 1 | 6     | 8 3 9
        ------ ------- ------
    3   5 1 9 |   4 6 | 3 2 8
    4   8   2 | 1   5 | 7   6
    5   6 7 4 | 3 2   |     5
        ------ ------- ------
    6         | 4 5 7 | 2 6 3
    7   3 2   |   8   |   5 7
    8   7 4 5 |     3 | 9   1
    '''
    sisennys = '   '
    ylin = f'{sisennys} 0 1 2   3 4 5   6 7 8'
    vali = f'{sisennys} ------ ------- ------'

    print(ylin)
    print()

    for rivi_nro in range(9):
        if rivi_nro in (3, 6):
            print(vali)

        print(rivi_nro, end=sisennys)

        for sarake_nro in range(9):
            if sarake_nro in (3, 6):
                print('| ', end='')

            numero = sudoku[rivi_nro][sarake_nro]
            print(numero if numero > 0 else ' ', end=' ')

        print()
