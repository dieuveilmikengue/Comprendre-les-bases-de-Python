print("Comprendre les fonctions en Python\n")

"""
Une fonction désigne en programmation un « sous-programme » permettant d'effectuer des opérations répétitives. 
Au lieu d'écrire le code complet autant de fois que nécessaire, on crée une fonction pour l'appeler quand on aura 
besoin d'exécuter cette meme tache

print(): dans la fonction permet à la fonction d'afficher l'instruction sur la console quand on l'appellera
return: dans la fonction retourne l'intruction quant on appellera la fonction et on pourra utiliser print pour l'afficher sur la console

"""


def direBonjour(): # On définit la fonction qui à pour nom :dire
    print("Bonjour les coudeurs !") # On précise ce que doit Afficher(le print()) la fonctioonn quand on l'appelera    

direBonjour() #On appelle la fonction :direBonjour

# On crée une boucle on appelant la fonction tant que notre valeur quont va iniatialiser séra inferieure à 10
chiffre = 0 
while chiffre < 10: #Tant chiffre sera inférieure ou à 10
    direBonjour() #Appelle la fonction bonjour à s'executer
    chiffre += 1 #en incrementant la valeur de  de la variable chiffre de 1


def message(nom, message): # On definit la fonction qui à pour nom message et on enregistre également les arguments(nom, message)
    print("{}: {}".format(nom, message)) # On précise ce que doit Afficher(le print()) la fonctioonn quand on l'appelera      

message("Mike", "Bonjour les codeurs") #On appelle la fonction message en enregistrant les argument (nom, message)


# Un autre exemple avec la fonction qui Affiches les valeurs saisies par l'utilisateur

nom = input("Entrez votre Pseudo: ")
messages = input("Message: ")

def direMessage(nom, messages): # On definit la fonction qui à pour nom :direMessage et on enregistre également les arguments(nom, message)
    print("{}: {}".format(nom, messages)) # On précise ce que doit Afficher(le print()) la fonctioonn quand on l'appelera      

direMessage(nom, messages) #On appelle la fonction message en enregistrant les argument (nom, messages)


nom = input("Entrez votre Pseudo: ")
messages = input("Message: ")

def direMessage(nom, messages): # On definit la fonction qui à pour nom :direMessage et on enregistre également les arguments(nom, message)
    return "{}: {}".format(nom, messages) # On précise ce que doit Retourner(return) la fonctioonn quand on l'appelera      

print(direMessage(nom, messages)) #Le print affiche la fonction

# On crée une fonction qui nous permettra de parcourir une liste en utilisant la boucle for
def parcours(*listes): #le symbole * signifie 'all' ou encore tou(te)s
    for element in listes: #Tant que notre listes contient de elements
        print(element) #Affiches les

parcours("fils", "fille", "garcon", "femme", "homme") #On apelle la fonction



# On crée une fonction qui va nous aider à faire des opérations en lui donnant juste les valeurs

nombre1 = input("Entrer le nombre 1: ") #On demande à l'utilisateur de saisir un nombre qui sera en string
nombre1 = int(nombre1) #On convrti la valeur saisie par l'utilisateur en integer
nombre2 = input("Entrer le nombre 2: ") #On demande à l'utilisateur de saisir un nombre qui sera en string
nombre2 = int(nombre2) #On convrti la valeur saisie par l'utilisateur en integer

def somme(nombre1, nombre2):
    resultat = nombre1 + nombre2
    return resultat #La fonction nous retourne le resultat mais ne va pas l'afficher

print(somme(nombre1, nombre2)) #On utilise le print pour afficher la fonction sur la console


"""
On crée une fonction de devinette qui va demander à l'utilisateur d'entrer une valeur quelconque entre 0 et 20, prennons 10 comme reponse juste
si la valeur entrée est inférieure à 5 et superieure à 15, on affiche: Vous etes un peu loin de la bonne reponse, reessayer encore !
si c'est superieur à 5 et inférieure à 10 ou supérieure à 10 et inférieure à 15: Pas mal vous n'etes pas loin de la bonne reponse.
si c'est 10: Bonne reponse ! Felicitaion vous avez un QI > 10000.

"""



def devinette():
    application = True #L'application est initialisée à True
    print("Veillez entrer une valeur entre 0 et 20: ")
    i = -1 #on itialise à 0 le nombre des tentatives

    while application: #Tant que l'application marche
        x = input(">") #La valeur qui sera saisie par l'utilisateur
        x = int(x) #La convertion en integer ou entier

        i += 1 #On incremente de 1 a chaque tentative manquée

        if (x <= 5 or x >= 15) and x != 10 and x != 99: #On doit preciser aussi 99 parce que cette notre valeur de sortie(quitter le jeu) sinon l'application va lui classer dans la condition de supérieure à 15
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
    print("Merci d'avoir joué à notre jeu !")


devinette()


# Une fonction lambda, cela nous prmet d'ecrire l'instruction en une seule ligne de code, c'est moins utilisé

prixTTC = lambda prixHT: prixHT + (prixHT * 20/100) #On met notre fonction dans une variable appelé prixTTC
somme = lambda a, b: a + b

print(prixTTC(100)) #On appel notre fonction puis on l'affiche
print(somme(5, 15))

"""
Avec ce script vous pouvez creer un jeu ou une application avec Kivy mais faudra encore travailler sur la gestion des erreurs
on le verra très prochainnement
Developper votre créativité et exercer vous

ON APPREND PAR LA PRATIQUE

"""