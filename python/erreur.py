print("La gestion des erreurs avec Python")

"""
Voila, ici le but est de gerer les informations envoyer par l'utilisateur en precisant les exceptions.
Commencer par tester votre formulaire, decouvrez les erreurs et utiliser ses erreurs pour gerer les exceptions
A noter qu'il ya beaucoup des erreurs, vous allez les rencontrer par rapport a vos programmes

assert: permet de creer vos propres exceptions
"""

# ON DEMANDE D'ECIRE UN NOMBRE AU HASARD
"""
choixUser = input("Choisissez une valeur au hasard \n>") #On demande à l'utilisateur de choisir un nombre

try:
    choixUser = int(choixUser) #On essaye de convertir la valeur entrer par l'utilisateur
except ValueError: #On verifie si l'utilisateur envoie une chaine de caractère au lieu d'un nombre
    print("Vous devez entrer un nombre et nom une lettre") #On affiche.........
else: #Sinon 
    print("Tu as choisi {}".format(choixUser)) #On continue notre programme
finally:
    print("Fin du programme !") #finalement on affiche ca peut importe les données de l'utilisateur
"""



# On prends un autre exemple avec la division
"""
valeur = 100
calcule  = input("Ecris une valeur que 100 peut diviser \n>")

try:
    calcule = int(calcule)
    print(valeur, " / " ,calcule, " = " ,valeur/calcule)
except ZeroDivisionError:
    print("Vous ne pouvez pas diviser 100 par zero (0)")
except ValueError:
    print("Vous ne pouvez pas diviser 100 par une lettre ou une phrase entrer plutot une valeur")
"""

# ON VA UTILISER ASSERT
"""
try:
    choixUser = input("Choisissez une valeur au hasard \n>") #On demande à l'utilisateur de choisir un nombre
    choixUser = int(choixUser) #On essaye de convertir la valeur entrer par l'utilisateur
    assert 0 <= choixUser <= 50 #Cette condition doit etre remplie sinon exception
    print("Vous avez choisi {}".format(choixUser))
except AssertionError: #On verifie si l'utilisateur envoie une chaine de caractère au lieu d'un nombre
    print("La valeur doit etre de 0 à 50") #On affiche.........
except ValueError: #On verifie si l'utilisateur envoie une chaine de caractère au lieu d'un nombre
    print("Pas des chaines de caractères, entrer plutot un nombre de 0 à 50") #On affiche.........
"""