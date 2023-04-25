print("Comprendre les Conditions dans Python \n")

"""
Operateurs de comparaisons:
                            == (egal à)
                            < (inferieur à)
                            <= (inferieur ou egal à)
                            > (superieur à)
                            >= (superieur ou egal à)
                            != (different de)
                            


Conditions multiples:
                    and (ET)
                    or (OU)
                    in / not in (Dans / Pas Dans)
                    is not (different de)

Mot clés des conditions: if / ifelse / else

"""


identifiant = "Mike"
motDePasse = "Lebake1234"

userId = input("Entrez votre identifiant :")
userPassword = input("Entrez votre Mot de passe :")

print("\nInterface utilisateur \n")

if userId == identifiant and userPassword == motDePasse: #Si userId correspond à identifiant et userPassword à motDePasse
    print("Salut ", userId, "\n") #Affiche Salut l'userId qui est le nom de l'utilisateur
else: #Sinon
    print("L'identifiant ou le mot de passe saisi ne correspond à aucun compte") #Afficher ce qui est dans le print



lettre = input("Entrez une lettre")
alphabet = "abcdefghijklmnopqrstuvwxyz"
voyelle = "iuoaey"
consonnes = "bcdfghjklmnpqrstuvwxz"

if lettre in voyelle:
    print(lettre, " est une voyelle")
elif lettre in consonnes:
    print(lettre, " est une consonne")
else:
    print("La valeur entrer n'est ni une consonne n'ont plus une voyelle")


"""
On crée un Jeu de devinette qui va demander à l'utilisateur d'entrer une valeur quelconque entre 0 et 20, prennons 10 comme reponse juste
si la valeur entrée est inférieure à 5 et superieure à 15, on affiche: Vous etes un peu loin de la bonne reponse, reessayer encore !
si c'est superieur à 5 et inférieure à 10 ou supérieure à 10 et inférieure à 15: Pas mal vous n'etes pas loin de la bonne reponse.
si c'est 10: Bonne reponse ! Felicitaion vous avez un QI > 10000.
si c'est autres choses comme une erreur de sa part....: Oups vous avez surement entrer une valeur qu'il ne fallait pas, vous pouvez recommencer svp !
"""

print("Veillez entrer une valeur entre 0 et 20: ")
x = input(">") #On recupère la valeur saisie par l'utilisateur en str
x = int(x) #On converti la valeur en int

if (x <= 5 or x >= 15) and x != 10: 
    print("Vous etes un peu loin de la bonne reponse, reessayer encore !")
elif (x > 5 or x < 15) and x !=10:
    print("Pas mal vous n'etes pas loin de la bonne reponse, reesayer encore ")
elif x == 10:
    print("Bonne reponse ! Felicitaion vous avez un QI > 10000")
else:
    print("Oups vous avez surement entrer une valeur qu'il ne fallait pas, vous pouvez recommencer svp !")


# On va developper cela dans le chapitre suivant sur les boucles pour voir d'autres options

