"""
Vaje voronoi

Potrebujete matplotlib:
pip install matplotlib
"""

from typing import List, Tuple, Dict, Callable, Union
import random
import time

from matplotlib import pyplot


def voronoi_brute_force(semena: Dict[Tuple[int, int, int], List[int]], velikost: int, razdalija: Callable) -> List[List[Tuple[int, int, int]]]:
    """
    Vrne matriko, ki predstavlja voronoieve diagrame v 2D ravnini.
    Pregleda vsako tocko in najde kateremu semenu je najbizja in jo pobarva v to barvo.

    Args:
        semena (Dict[Tuple[int, int, int], List[int]]): Semena za narisat.
        velikost (int): Predstavlja velikost kvadratne matrike N.
        razdalija (Callable): Funkcija, ki prejme dve točki in vrne razdalijo med njima.

    Returns:
        List[List[Tuple[int, int, int]]]: Kvadratno matriko kjer vsak element predstavlja en piksel in je v obliki RGB vrednosti.
    """
    print("Brute force: Generiram ... ")
    matrika = list()
    for x in range(velikost):
        vrsta = list()
        for y in range(velikost):
            najmanjsa = velikost
            najmanjsa_barva = (0, 0, 0)
            for barva, koordinate in semena.items():
                raz = razdalija([x, y], koordinate)
                if raz < najmanjsa:
                    najmanjsa = raz
                    najmanjsa_barva = barva
            vrsta.append(najmanjsa_barva)
        matrika.append(vrsta)
    return matrika


def voronoi_jump_flood(semena: Dict[Tuple[int, int, int], List[int]], velikost: int, razdalija: Callable) -> List[List[Tuple[int, int, int]]]:
    """
    Vrne matriko, ki predstavlja voronoieve diagrame v 2D ravnini, kjer je vsak element v matriki pobarvan v barvo celice kateri točka pripada.
    Semena so v obliki {barva : točka, ...};

    Args:
        semena (Dict[Tuple[int, int, int], List[int]]): Semena za narisat.
        velikost (int): Predstavlja velikost kvadratne matrike N.
        razdalija (Callable): Funkcija, ki prejme dve točki in vrne razdalijo med njima.

    Returns:
        List[List[Tuple[int, int, int]]]: Kvadratno matriko kjer vsak element predstavlja en piksel in je v obliki RGB vrednosti.
    """
    def smo_v_matriki(tocka: List[int]) -> bool:
        """
        Vrne true če se točka nahaja v matriki.

        Args:
            tocka (List[int]): Točka kjer preverjamo.

        Returns:
            bool: Če se nahaja ali ne.
        """
        return 0 <= tocka[0] < len(matrika) and 0 <= tocka[1] < len(matrika)
    print("Jump flood: Gneriram ... ")
    matrika = [[(0, 0, 0)] * velikost for _ in range(velikost)]
    for barva, tocke in semena.items():
        matrika[tocke[0]][tocke[1]] = barva
    #k predstavlja korak, za koliko mest gremo stran od nasega semena
    k = len(matrika) // 2
    # osnovna semena vstavimo v naso tabelo
    tabela_semen = list(semena.values())
    while k >= 1:
        nova_tabela = tabela_semen
        for tocka in tabela_semen:
            x, y = tocka
            #dolocimo vseh osem smeri v katerih bomo gledali
            for smer in [[1, 1], [1, 0], [0, 1], [-1, -1], [-1, 0], [0, -1], [1, -1], [-1, 1]]:
                #premik povezamo za nas korak
                premik_x, premik_y =  [k * smer[i] + tocka[i] for i in range(2)]
                #pogledamo, ali smo se vedno v matriki da ni slucajno indexerror
                if not smo_v_matriki([premik_x, premik_y]):
                    continue
                #ce je tocka katero gledamo drugacna od trenutne
                if matrika[x][y] != matrika[premik_x][premik_y]:
                    #ce je tocka se nepobarvana jo takoj lahko pobarvamo z barvo trenutne tocke
                    if matrika[premik_x][premik_y] == (0, 0, 0):
                        matrika[premik_x][premik_y] = matrika[x][y]
                        #dodamo v tabelo, saj je to tut zdaj seme za naslednje iteracije
                        nova_tabela.append([premik_x, premik_y])
                    else:
                        #Pogledamo ce je ta tocka blizje nasi izvirni ali tisti, s kero barvo je trenutno oznacena
                        if razdalija(semena[matrika[x][y]], [premik_x, premik_y]) < razdalija([premik_x, premik_y], semena[matrika[premik_x][premik_y]]):
                            matrika[premik_x][premik_y] = matrika[x][y]
        #tabela zamenjamo z novo, ki poleg starih semen vsebuje tudi tiste, ki smo jih prvic pobarvali
        tabela_semen = nova_tabela
        #korak razdvojimo
        k //= 2
    return matrika


def generator_semen(velikost_platna: int, st_semen: int) -> Dict[Tuple[int, int, int], List[int]]:
    """
    Generira nakljucna semena v obliki 
        {barva_celice : točka_v_matriki}, kjer je barva celice RGB vrednost npr. (30, 245, 134); točka_v_matriki pa seznam [x, y]

    Args:
        velikost_platna (int): Velikost N platna, če bo N=100, bo matrika pikslov velikosti 100x100
        st_semen (int): Število semen za generirat

    Returns:
        Dict[Tuple[int, int, int], List[int]]: {barva1: točka1, barva2: točka2, ...}
    """
    semena = dict()
    for _ in range(st_semen):
        barva = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        semena[barva] = [random.randint(1, velikost_platna - 1) for _ in range(2)]
    return semena
    

def narisi(semena: Dict[Tuple[int, int, int], List[int]], matrika: List[List[Tuple[int, int, int]]]) -> None:
    """
    Funkcija nariše podano matriko, ter doda semena kot rdeče točke. 
    Matrika je 2 dimenzionalna in vsak element predstavlja RGB barvo tistega "piksla", torej (0, 0, 0) za črno.

    Semena podamo kot slovar, kjer je ključ RGB tuple; npr. (23, 22, 234), vrednost pa pozicija v matriki; [x, y]
    Matriko podamo kot Seznam Seznamov, vsak element predstavlja RGB vrednost tistega "piksla"

    Args:
        semena (Dict[Tuple[int, int, int], List[int]]): Semena za narisat.
        matrika (List[List[Tuple[int, int, int]]]): Matrika pobarvanih pikslov.
    """
    # Narišemo matriko kjer vrednosti predstavljajo RGB barve
    pyplot.imshow(matrika)
    tocke = semena.values()
    #narisemo se osnovna semena in kje "izvirajo"
    pyplot.scatter([x[1] for x in tocke], [y[0] for y in tocke], color="red")
    pyplot.show()


def k_ta_razdalja(tocka1: List[int], tocka2: List[int], k: Union[float, int] = 2) -> float:
    """
    Vrne k-to razdalijo med dvema točkama.

    Args:
        tocka1 (List[int]): Prva točka dimenzije 2.
        tocka2 (List[int]: Druga točka dimenzije 2.
        k (Union[float, int], optional): Potenca k-te razdalije. Defaults to 2.

    Returns:
        float: Razdalija med dvema točkama.
    """
    return (abs((tocka2[0] - tocka1[0]))**k + abs((tocka2[1] - tocka1[1]))**k) ** (1/k)

def euclidova_razdalija(tocka1: List[int], tocka2: List[int]) -> float:
    """
    Vrne euklidovo razdalijo med dvema točkama.

    Args:
        tocka1 (List[int]): Prva točka dimenzije 2.
        tocka2 (List[int]: Druga točka dimenzije 2.

    Returns:
        float: Razdalija med dvema točkama.
    """
    return k_ta_razdalja(tocka1, tocka2)

def manhattan_razdalja(tocka1, tocka2) -> float:
    """
    Vrne manhatansko razdalijo med dvema točkama.

    Args:
        tocka1 (List[int]): Prva točka dimenzije 2.
        tocka2 (List[int]: Druga točka dimenzije 2.

    Returns:
        float: Razdalija med dvema točkama.
    """
    return abs(tocka2[0] - tocka1[0]) + abs(tocka2[1] - tocka1[1])


if __name__ == "__main__":
    # Primer
    velikost_platna = 200
    st_semen = 20
    semena = generator_semen(velikost_platna, st_semen)
    matrika = voronoi_jump_flood(semena=semena, velikost=velikost_platna, razdalija=euclidova_razdalija)
    narisi(semena, matrika)
