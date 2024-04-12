from Morpion import Morpion
from StrategieAleatoire import StrategieAleatoire
from StrategieMinMax import StartegieMinMax
from ConfigurationMorpion import ConfigurationMorpion
from CoupMorpion import CoupMorpion



def test_coups_1():
    partie = Morpion()


    cg = ConfigurationMorpion()
    cg.jouer_coup(CoupMorpion(1, 0, 0))

    # cg.jouer_coup(CoupMorpion(2, 2, 2))
    # cg.jouer_coup(CoupMorpion(1, 2, 0))

    # cg.jouer_coup(CoupMorpion(2, 1, 1))
    # cg.jouer_coup(CoupMorpion(1, 2, 1))
    # cg.jouer_coup(CoupMorpion(2, 0, 2))
    # cg.jouer_coup(CoupMorpion(1, 2, 2))


    # cg.jouer_coup(CoupMorpion(2, 0, 1))


    partie.jouerPartie(cg, StartegieMinMax, 10)

def test_coups_2():
    """rotation a 45° fait apparaitre un probleme"""

    partie = Morpion()

    cg = ConfigurationMorpion()
    cg.jouer_coup(CoupMorpion(1, 0, 2))
    cg.jouer_coup(CoupMorpion(2, 2, 2))

    cg.jouer_coup(CoupMorpion(1, 2, 0))
    cg.jouer_coup(CoupMorpion(2, 1, 1))

    cg.jouer_coup(CoupMorpion(1, 1, 0))
    cg.jouer_coup(CoupMorpion(2, 1, 2))

    partie.jouerPartie(cg, StartegieMinMax, 10)


def test_coups_3():
    partie = Morpion()

    cg = ConfigurationMorpion()
    cg.jouer_coup(CoupMorpion(1, 2, 0))
    cg.jouer_coup(CoupMorpion(2, 0, 0))
    cg.jouer_coup(CoupMorpion(1, 1, 1))
    cg.jouer_coup(CoupMorpion(2, 0, 2))
    cg.jouer_coup(CoupMorpion(1, 0, 1))
    partie.jouerPartie(cg, StartegieMinMax, 10)


test_coups_1()