# Comprendre les bases du Langage Python

## C'est quoi Python
Python est l’un des langages de programmation les plus couramment utilisés par les professionnels de la donnée. Mais ses applications ne se limitent pas seulement à la Data science : Python peut aussi être utilisé pour développer des logiciels, écrire des algorithmes ou encore gérer l’infrastructure web d’un réseau social (ex: Instagram). 

## Installation de la dernière version de Python

Télécharger la dernière version de Python le lien ci dessous:

https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe


## Les variables
VARIABLE: C'est unn element qui associe valeur à un libellé

    Nommer une variable:
                Ne pas contenir de caractere speciaux
                Ne pas contenir d'espace
                Untiliser des underscores(_)
                Commencer par une lettre
    Types des variable:
				Entier numerique (int)
				Nombre flottant (float) ou nombre décimal
				Chaine de caractere (str)
				Bolean (bool)
				autres (listes, dictionnaires, tuples, etc.)
    Les fonctions:
				print() === Afficher dans la console
				input() === Demander à l'utilisateur d'entrer une chaine de caractere
				type() 			=== retourner le type d'une variable
				int(), float(), str()	=== convertir une donnee
				str.format() 	=== formater une chaine les accolades sontplacées respectivement par rapport aux variables
                f"str{variable}..." === Afficher les variables dans la console
                    
    Lors de l'affichage des variables on utilise:
				\t pour faire une tabulation
                \n pour revenir à la ligne

## Les conditions
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

## Les opérations
    Operateurs en Python: 
                + (addition)
                - (soustraction)
                / (division)
                % (modulo) == reste d'une division
    Incrementation et decrementaion:
                variable = variable + X :Ajouter la valeur X dans la variable
                variable += X

                variable = variable - X :Diminuer la variable de X
                variable -= X

                variable = variable * X :Multiplier la variable par X
                variable *= X

## Les Boucles
    Les fonctions de la boucles:
                while (tant que .... on met la condition) 
                for ()
                    continuer: (tant que la condition est respectée continue a faire tourner le truc)
                    break: (une fois la condition au dessus de break est vraie en arrete le truc)

## Les fonctions
Une fonction désigne en programmation un « sous-programme » permettant d'effectuer des opérations répétitives. 
Au lieu d'écrire le code complet autant de fois que nécessaire, on crée une fonction pour l'appeler quand on aura 
besoin d'exécuter cette meme tache

    def nomDeLaFonction(arguments):
        instruction
    
    nomDeLaFonction(arguments)

    print(): dans la fonction permet à la fonction d'afficher l'instruction sur la console quand on l'appellera

    return: dans la fonction retourne l'intruction quant on appellera la fonction et on pourra utiliser print pour l'afficher sur la console

## Les listes
Une liste est une structure de données qui contient une série de valeurs. Python autorise la construction de liste contenant des valeurs de types différents (par exemple entier et chaîne de caractères), ce qui leur confère une grande flexibilité. Une liste est déclarée par une série de valeurs (n'oubliez pas les guillemets, simples ou doubles, s'il s'agit de chaînes de caractères) séparées par des virgules, et le tout encadré par des crochets.

## Les tuples
La difference entre un tuple et une liste est qu'une liste est modifiable et un tuple ne peut pas etre modifi" une fois crée
sauf lors de l'affectation multiple

    tuple:
        variable = ()  (vide)
        variable = (2, 4) (Plusieurs valeurs)
        variable = 5,   (Une seule valeur)
        variable = (5,) (Une seule valeur)

    Affectation multiples:
        (valeur1, valeur2,....valeurn) = (1, 2, 3,........n)

## Les dictionnaires
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


## Les chaines de caractères
Une methode de chaine de caractere travaille sur une copie, et pas sur la chaine elle meme.

    str.upper(), str.lower(), str.capitalize(), str.title()
    str.center(largeur, caractere de remplissage)

    str.find(chaine, debut, fin) trouver l'indice du mot dans chaine en respectant la casse
    str.index(chaine, debut, fin) trouver l'indice du mot dans chaine en respectant la casse
    str.strip() Enleve les espaces avant et apres
    str.replace
    str.len

## Le random
    randint(a, b): generer les entiers de [a à b]
    randrange(a, b, n): generer les entiers de [a à b] avec un saut valeur de n
    uniform(a, b): generer les nombres decimaux de a à b
    choice(list): generer un choix dans list ou un tableau par exemple
    shuffle(list): boulverser l'ordre d'une liste

## Gestion des erreurs
Voila, ici le but est de gerer les informations envoyer par l'utilisateur en precisant les exceptions.
Commencer par tester votre formulaire, decouvrez les erreurs et utiliser ses erreurs pour gerer les exceptions
A noter qu'il ya beaucoup des erreurs, vous allez les rencontrer par rapport a vos programmes

    assert: permet de creer vos propres exceptions

## Installation des modules
### 1er cas: 

    import librairie: Importer une librairie et pour l'executer un module vous devez ecrire librairie.module(variable)

### 2eme cas: 
    from librairie import module: Vous importer un module precis et pour l'executer on ecrit juste module(variable)
### 3eme cas: 
    from librairie import *: importer tous les modules de la librairie, pour l'executer on ecrit juste module(variable)

4eme cas: 
Vous pouvez egalement utiliser vos propres fichiers comme des librairies et des fonctions comme des modules


## Les fichiers
    r (Lecture seule)
    w (Ecrire avec remplacement)
    a (Ecrire avec ajout en fin du fichier)
    x (Lecture et ecriture)
    r+ (Lecture/écriture dans un meme fichier)

## Les class
Une Classe: définit des attributs et des méthodes. Par exemple, imaginons une classe Voiture qui servira à créer des objets qui sont des voitures. 
Cette classe va pouvoir définir un attribut couleur, un attribut vitesse, etc. Ces attributs correspondent à des propriétés qui peuvent exister pour 
une voiture. La classe Voiture pourra également définir une méthode rouler(). Une méthode correspond en quelque sorte à une action, ici l’action de 
rouler peut être réalisée pour une voiture.

    class NomDeNotreClass:
        def __init__(self, attribut1, attribut2):
            self.variable1 = attribut1
            self.variable2 = attribut2

            
    On sort de la class
    variable = NomDeNotreClass(attribut1, attribut2)

    print(variable.variable1) #Pour recuperer la variable1 de notre class nomDeNotreClass
    print(variable.variable2) #Pour recuperer la variable2 de notre class nomDeNotreClass

## Les propriétés
Les propriétés permettent de définir des comportements de 'getter' et 'setter' sur les méthodes d'une classe.
Cela nous permet également d'appeler une méthode sans avoir besoin d'utiliser les parenthèses.

## Héritage
L'héritage est un mécanisme qui nous permet de créer une nouvelle classe – connue sous le nom de classe enfant – qui est basée sur une classe existante – la classe mère, en ajoutant de nouveaux attributs et méthodes en plus de la classe existante. Lorsque vous procédez ainsi, la classe enfant hérite des attributs et méthodes de la classe parent.

## Gestion du temps
Quelques fonctions:

        .time() -----> Recuperer la temps et date ecoulée depuis l'expansion de l'informatique (le 1er Janvier 1970) en seconde
        .sleep(n) -----> mettre le programme en pause de n seconde
        .localtime() -----> Recuperer la date et l'heure actuelle
        .datetime.now()----->Recuperer la date et l'heure actuelle
        .date.today() ------> Recuperer la date actuelle
        .strftime() ----------> Prendre un format de date


L'heure et la date:

        %d : jour (du 1er au 31)
        %m : mois (1 à 12)
        %Y : année (2023)
        %y : année (23)
        %H : heures (00 à 23)
        %I : minutes (00 à 59)
        %S : secondes (00 à 59)
        %p : AM/PM
        %A : jour de la semaine
        %a : jour abrégé
        %B : mois
        %b : mois abregé
        %Z : fuseau horaire(timezone)