print("Comprendre les modules dans Python \n")

"""
1er cas: import librairie: Importer une librairie et pour l'executer un module vous devez ecrire librairie.module(variable)
2eme cas: from librairie import module: Vous importer un module precis et pour l'executer on ecrit juste module(variable)
3eme cas: from librairie import *: importer tous les modules de la librairie, pour l'executer on ecrit juste module(variable)

4eme cas: Vous pouvez egalement utiliser vos propres fichiers comme des librairies et des fonctions comme des modules
"""

# 1ER CAS
"""
import math

racine = math.sqrt(25)
print(racine)
"""

# 2EME CAS
"""
from math import sqrt

racine = sqrt(100)
print(racine)
"""

# 3EME CAS
"""
from math import *

racine = sqrt(81)
print(racine)
"""

# 4EME CAS

from module import * #On importe tous les modules de notre librairie module qu'on a crée
from includes.opera import *

dire("Mike", "Bonjour les gens") #On appel à notre fonction dire(nom, message)  qui se trouve dans module en l'attribuant des arguments
somme(25, 75) #On fait appel à notre fonction somme(a, b) qui se trouve dans notre dossier includes qu'on vient de créer

