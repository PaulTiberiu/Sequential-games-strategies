from Morpion import Morpion
from StrategieAleatoire import StrategieAleatoire
from StrategieMinMax import StartegieMinMax
from ConfigurationMorpion import ConfigurationMorpion
from CoupMorpion import CoupMorpion

partie = Morpion()



cg = ConfigurationMorpion()


# cg.jouer_coup(CoupMorpion(1, 1, 1))
# cg.jouer_coup(CoupMorpion(2, 0, 0))
# cg.jouer_coup(CoupMorpion(1, 0, 2))
# cg.jouer_coup(CoupMorpion(2, 2, 0))


# cg.jouer_coup(CoupMorpion(1, 1, 0))
# cg.jouer_coup(CoupMorpion(2, 1, 2))


partie.jouerPartie(cg, StartegieMinMax, 3)

