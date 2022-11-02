from statistics import mean


def keskimmaisten_keskiarvo(numerot: list) -> float:
    jarjestetty = sorted(numerot)
    keskimmaiset = jarjestetty[1:-1]

    return mean(keskimmaiset)
