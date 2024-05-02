from Allumettes import Allumettes
from StrategieMinMax import StartegieMinMax
from ConfigurationAllumettes import ConfigurationAllumettes
from CoupAllumettes import CoupAllumettes






def test_coups_1():
    partie = Allumettes()


    cg = ConfigurationAllumettes([1, 2, 1], 3)
    #cg.jouer_coup(CoupMorpion(1, 0, 0))

    # cg.jouer_coup(CoupMorpion(2, 2, 2))
    # cg.jouer_coup(CoupMorpion(1, 2, 0))

    # cg.jouer_coup(CoupMorpion(2, 1, 1))
    # cg.jouer_coup(CoupMorpion(1, 2, 1))
    # cg.jouer_coup(CoupMorpion(2, 0, 2))
    # cg.jouer_coup(CoupMorpion(1, 2, 2))


    # cg.jouer_coup(CoupMorpion(2, 0, 1))


    partie.jouerPartie(cg, StartegieMinMax, 100)

def test_coups_2():
    """rotation a 45° fait apparaitre un probleme"""

    partie = Allumettes()

    cg = ConfigurationAllumettes([1, 3, 5], 3)
   

    partie.jouerPartie(cg, StartegieMinMax, 100)


# def test_coups_3():
#     partie = Allumettes()

#     cg = ConfigurationMorpion()
#     cg.jouer_coup(CoupMorpion(1, 2, 0))
#     cg.jouer_coup(CoupMorpion(2, 0, 0))
#     cg.jouer_coup(CoupMorpion(1, 1, 1))
#     cg.jouer_coup(CoupMorpion(2, 0, 2))
#     cg.jouer_coup(CoupMorpion(1, 0, 1))
#     partie.jouerPartie(cg, StartegieMinMax, 100)


test_coups_1()