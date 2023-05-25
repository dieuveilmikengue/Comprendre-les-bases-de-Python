import json

print("Comprendre les Dictionnaires avec Python")


"""

dictionnaire:
            variable = {"clé": "valeur"}
            variable = {}  (vide)
            ne jamais utilisé une clé deux fois dans un seul dictionnaire.
            Les clés sont des chaines de caractères

fonctions:  
            variable.pop(valeur)    Supprimer une valeur dans le dictionnaire
            del variable[valeur]    Supprimer une valeur dans le dictionnaire
            dict1 = dict.copy()     Prendre une reference ou copier tout simplement
            variable.get("clé", "condition false")  On recupère la valeur de la clé et si la clé n'existe pas au lieu d'afficher une erreur affiche la condition false
"""


dict = {1:125, "present": "charle"}
print(dict[1]) #recupère la valeur de l'indice 1 dans le dico

# AJOUTER UNE VALEUR DANS LE DIC0, MODIFIER
dict["salutation"] = "Bonjour les gens" #on ajoute la clé salutation
print(dict)

dict[1] = "Bizarre" #On modifie la valeur de la clé 1 en bizarrz
print(dict)

print(dict.get("present", "l'element que vous cherchez n'existe pas"))

print("\n")

dict[("femme", "homme")] = ("gentille", "bad boys") #On ajoute là un tuple dans un dictionnaire
print(dict)

print(dict[("femme", "homme")]) #On recupère notre tuple dans le dictionnaire
print(dict[("femme", "homme")][0]) #On recupère la valeur de l'indice 0 du tuple qui se trouve dans le dictionnaire
print(dict[("femme", "homme")][1]) #On recupère la valeur de l'indice 1 du tuple qui se trouve dans le dictionnaire

print("\n")

dict1 = dict.copy() #La copie de dict
print(dict1)


# ON AFFICHE LES ELEMENTS, VERIFICATION

for element in dict: #Tant que y'a des element dans la variable dict
    print(element) #Affiches les

for element in dict.keys(): #Tant que y'a des element dans la variable dict
    print(element) #Affiches les clés

for element in dict.values(): #Tant que y'a des element dans la variable dict
    print(element) #Affiches les valeurs

for k, v in dict.items(): #Tant que y'a des element dans la variable dict
    print(f"{k}: {v}") #Affiches les valeurs

if "salutation" in dict: #On verifie si salut se trouve dans le dictionnaire dict
    print("C'est bien") #affiche c'est bien si true
else: #sinon
    print("Rien") #Affiche rien

# SUPPRESSION

elements = {"nom": "Mikengue", "prenom": "dieuveil", "sex": "masculin", "age": 26, "ville": "brazzaville", "pays": "congo"}
print(elements)

del elements["ville"] #On supprime la ville dans notre dictionnaire
print(elements)

elements.pop("pays") #On supprime le pays
print(elements)

"""
Pour eviter les erreurs lors de la supression des elements d'un dictionnaire
il est preferable d'utiliser les conditions

if "ville" in elements:
    del elements["ville"]
La si l'element est dans le dictionnaire il suprime mais si l'element n'est pas dans le dictionnaire
il ne fera rien et il ne va pas aussi afficher une erreur
"""


print("\n")

# UN ENSEMBLE AVEC DES DICTIONNAIRES A L'INTERIEURE
"""

e = {
        0: {
            "nom": "Mike",
            "prenom": "Dieuveil",
            "age": 26,
            "ville": "brazzaville"
        },
        1: {
            "nom": "ewe",
            "prenom": "stan",
            "age": 28,
            "ville": "oyo"
        },
        2: {
            "nom": "balems",
            "prenom": "mael",
            "age": 28,
            "ville": "jardin"
        }
}
"""

#CHARGER LES DONNEES DEPUIS UN FICHIER JSON
with open("fichier.json", "r") as file:
    e = json.load(file)

print(e)

print(e["0"]["nom"]) #On recupère la valeur de la clé nom dans le premier dictionnaire

# SAUVEGARDER DANS UN FICHIER
"""
On crée un fichier 'fichier.json' ou on va stocker notre notre ensemble e
"""

with open("fichier.json", "w+") as file:
    json.dump(e, file)
