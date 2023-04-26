print("Comprendre les Boucles dans Python \n")
print("C'est une methode qui nous permet de repeter une tache de facon automatique au lieu de recrire le meme code beaucoup de fois \n")



"""
Les fonctions de la boucles:
                            while (tant que .... on met la condition) 
                            for ()
                                continuer: (tant que la condition est respectée continue a faire tourner le truc)
                                break: (une fois la condition au dessus de break est vraie en arrete le truc)
"""

# On va repeter un phrase 10 fois (0 à 9)

compteur = 0 #on initialise le compteur à 0 (0 à 9)

while compteur < 10: #tant que le compteur sera inferieur à 10
    print(compteur, "Est ce que vous comprenez ?") #l'instruction: Affiche la valeur qui est dans le print
    compteur += 1 #En incrementant de 1 ou en ajoutant 1

#Hors de la boucle
print("On sort de la boucle une fois la condition est remplie \n")


# On va simuler une Machine par exemple

machineMarche = True #On itialise la Machine à True ce qui veut dire que la machine est en marche

while machineMarche: #Tant que la machine fonctionne (True)
    choixMenu = input("Ecrire : ")

    if choixMenu == "Suivant": #si le choix est Suivant alors la machine va continuer à tourner
        continue
    elif choixMenu == "Hello": #si le choix est Hello alors la machine va afficher Hello word et continuer à tourner
        print("Hello word")
    elif choixMenu == "Quitter": #Si le choix est de Quitter alors la machine s'arrete break
        break
    else:
        print("Commande introuvable") #Si l'utilisateur saisie fais ce qu'il ne faut la machine va afficher commande introuvable et continuer àvtourner

print('\nA bientot')

# On prends la boucle for
#On va parcourir les lettres d'une chaine de caractere

texte = "Salut les codeurs Python"

for letter in texte: #Ici la variable letter est une variable aleatoire qui permet de parcourir le texte
    print(letter) #On affiche les valeurs trouvées par la variable letter



"""
On crée un Jeu de devinette qui va demander à l'utilisateur d'entrer une valeur quelconque entre 0 et 20, prennons 10 comme reponse juste
si la valeur entrée est inférieure à 5 et superieure à 15, on affiche: Vous etes un peu loin de la bonne reponse, reessayer encore !
si c'est superieur à 5 et inférieure à 10 ou supérieure à 10 et inférieure à 15: Pas mal vous n'etes pas loin de la bonne reponse.
si c'est 10: Bonne reponse ! Felicitaion vous avez un QI > 10000.
si c'est autres choses: Oups vous avez surement entrer une valeur qu'il ne fallait pas, vous pouvez recommencer svp !
"""

application = True #L'application est initialisée à True
print("Veillez entrer une valeur entre 0 et 20: ")
i = -1 #on itialise à 0 le nombre des tentatives

while application: #Tant que l'application marche
    x = input(">") #La valeur qui sera saisie par l'utilisateur
    x = int(x) #La convertion en integer ou entier
    i += 1 #On incremente de 1 a chaque tentative manquée

    if (x <= 5 or x >= 15) and x != 10 and x != 99:
        print("Vous etes un peu loin de la bonne reponse, reessayer encore ! ou ecriver 99 pour quitter le jeu")
        continue
    elif (x > 5 or x < 15) and x !=10 and x != 99:
        print("Pas mal vous n'etes pas loin de la bonne reponse, reesayer encore ! ou ecriver 99 pour quitter le jeu")
        continue
    elif (x > 5 or x < 15) and x !=10 and x != 99:
        print("Pas mal vous n'etes pas loin de la bonne reponse, reesayer encore ! ou ecriver 99 pour quitter le jeu")
        continue
    elif x == 10:
        print("Bonne reponse ! Vous avez reussi après {} tentatives manquées, Felicitaion vous avez un QI > 10000".format(i))
        break
    elif x == 99: #L'utilisateur va cliquer sur 99 s'il veut quitter le jeu avanr d'avoir trouver la bonne reponse
        break
    else:
        print("Oups vous avez surement entrer une valeur qu'il ne fallait pas, vous pouvez recommencer svp ! ou ecriver Q pour quitter le jeu")
        continue

print("Merci d'avoir jouer a notre jeu !")

# On developpera cet exemple dans les fonctions