print("Comprendre les tuples avec Python \n")

"""
La difference entre un tuple et une liste est qu'une liste est modifiable et un tuple ne peut pas etre modifi" une fois crée
sauf lors de l'affectation multiple

tuple:
    variable = ()  (vide)
    variable = (2, 4) (Plusieurs valeurs)
    variable = 5,   (Une seule valeur)
    variable = (5,) (Une seule valeur)

Affectation multiples:
                    (valeur1, valeur2,....valeurn) = (1, 2, 3,........n)
"""


valeur = 12,

print(type(valeur)) #On recupère le type de notre variable pour verifier que c'est un tuple
print(valeur)

valeur1 = (17, 2)
print(valeur1)
print(valeur1[1])

try: #VERIFIER AVEC LE TRY
    print(valeur1[2])
except:
    print("Pas possible")

t = 1, 4, 7, "bonjour", 6, "salut"
print(t)

tt = (24, "gentil", ("merci", 17)) #les tuples dans les tuples
print(tt)
print(tt[-1]) #on recupère la dernière valeur de tt qui n'est rein d'autre qu'un tuple
print(tt[-1][0]) #On recupère la première valeur du tuple qui se trouve à l'interieur de notre tuplr tt

tt0 = tt[-1] #On recupère le tuple qui se trouve en dernière position du tuple tt
print(tt0)

print(tt0[1]) #On affiche la deuxieme valeur de notre tuple tt0

# RASSEMBLER LES TUPLES

valeur3 = valeur + valeur1
print(valeur3)

valeur4 = valeur3 + t
print(valeur4)

# MULTIPLIER UN TUPLE

m = 3*valeur3 #On multiplie le tuple valeur3 par 3, les valeurs du tuple vont se repeter 3 fois
print(m)


# AFFECTATION MULTIPLE

(nombre1, nombre2) = (2, 5)

print(nombre1)
print(nombre2)


def get_position():
    posX = 25
    posY = 75
    return (posX, posY)

(coordX, coordY) = get_position()

coordX= 125
coordY= 22

print("Position du joueur: ( {}/{} )".format(coordX, coordY))


# PARCOURIR ET VERIFIER

for element in valeur4: #Tant que y'a des element dans la valeur4
    print(element) #Affiches les

if "salut" in valeur4: #On verifie si salut se trouve dans le tuple valeur4
    print("C'est bien") #affiche c'est bien si true
else: #sinon
    print("Rien") #Affiche rien