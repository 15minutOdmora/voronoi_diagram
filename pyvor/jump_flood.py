from platform import python_branch
from matplotlib import pyplot
import math, random
import time

from numpy import mat


def k_ta_razdalja(prva, druga, k=2):
    """
    Vrne razdaljo prve tocke do druge
    """
    return (abs((druga[0] - prva[0]))**k + abs((druga[1] - prva[1]))**k) ** (1/k)

def manhattanRazdalja(prva, druga):
    """
    Vrne manhatansko razdaljo od prve do druge točke
    """
    return abs(druga[0] - prva[0]) + abs(druga[1] - prva[1])


def vornoi_jump_flood(semena, velikost):
    """
    Vrne matriko, ki predstavlja voronoieve diagrame v 2D ravnini, kjer je vsak element v matriki označen z številko kateri točki pripada
    Semena so v obliki {st_semena : [x, y], ...}
    """
    
    def smo_v_matriki(tocka):
        "Vrne true ali false, ce je tocka v dani matriki"
        return 0 <= tocka[0] < len(matrika) and 0 <= tocka[1] < len(matrika)

    matrika = [[(0, 0, 0)] * velikost for _ in range(velikost)]
    for barva, tocke in semena.items():
        matrika[tocke[0]][tocke[1]] = barva

    k = len(matrika) // 2
    tabela_semen = list(semena.values())
    while k >= 1:
        nova_tabela = tabela_semen
        for tocka in tabela_semen:
            x, y = tocka
            for smer in [[1, 1], [1, 0], [0, 1], [-1, -1], [-1, 0], [0, -1], [1, -1], [-1, 1]]:
                premik_x, premik_y =  [k * smer[i] + tocka[i] for i in range(2)]
                if not smo_v_matriki([premik_x, premik_y]):
                    continue
                if matrika[x][y] != matrika[premik_x][premik_y]:
                    if matrika[premik_x][premik_y] == (0, 0, 0):
                        matrika[premik_x][premik_y] = matrika[x][y]
                        nova_tabela.append([premik_x, premik_y])
                    else:
                        #Pogledamo ce je ta tocka blizje nasi izvirni ali tisti, s kero barvo je trenutno oznacena
                        if k_ta_razdalja(semena[matrika[x][y]], [premik_x, premik_y], 1/2) < k_ta_razdalja([premik_x, premik_y], semena[matrika[premik_x][premik_y]], 1/2):
                            matrika[premik_x][premik_y] = matrika[x][y]

        tabela_semen = nova_tabela
        k //=2
    return matrika

def generator_semen(velikost_platna, st_semen):
    """
    Generira nakljucna semena v obliki {st_semena : [x, y]}
    """
    semena = dict()
    for _ in range(st_semen):
        barva = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        semena[barva] = [random.randint(1, velikost_platna - 1) for _ in range(2)]
    return semena
    

def narisi(semena, matrika):
    """
    Narise voronoieve diagrame in semena na platno
    """
    pyplot.imshow(matrika)
    tocke = semena.values()
    pyplot.scatter([x[1] for x in tocke], [y[0] for y in tocke], color="red")
    pyplot.show()


velikost_platna = 1000
st_semen = 15
semena = generator_semen(velikost_platna, st_semen)

matrika = vornoi_jump_flood(semena, velikost_platna)

narisi(semena, matrika)


