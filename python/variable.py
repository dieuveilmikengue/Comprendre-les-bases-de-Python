
print('Bonjour tout le monde')


# COMPRENDRE LES VARIABLE DANS PYTHON
"""
VARIABLE: C'est unn element qui associe valeur à un libellé
Nommer une variable:
					Ne pas contenir de caractere speciaux
					Ne pas contenir d'espace
					Untiliser des underscores(_)
					Commencer par une lettre
Types des variable	:
					Entier numerique (int)
					Nombre flottant (float) ou nombre décimal
					Chaine de caractere (str)
					Bolean (bool)
					autres (listes, dictionnaires, tuples, etc.)

Les fonctions 		:
					print() 		=== Afficher dans la console
					input() 		=== Demander à l'utilisateur d'entrer une chaine de caractere
					type() 			=== retourner le type d'une variable
					int(), float(), str()	=== convertir une donnee
					str.format() 	=== formater une chaine les accolades sont placées respectivement par rapport aux variables
                    
Lors de l'affichage des variables on utilise:
											\t pour faire une tabulation
                                            \n pour revenir à la ligne
"""


agePersonne = 26 #variable de type entier(int)
prixHT = 5.14 #variable de type decimal(float)
nomPersonne = "Dillema" #Une chaine de caractere (str)
paye = True #Variable de type Bolean
prenomPersonne = input("Entrer votre prenom") #On demande à l'utilisateur d'entrer son prenom: variable de type (str)


#la fonction type demande le type de variable declaré
print("Le type de la variable agePersonne est:", type(agePersonne)) 
print("Le type de la variable nomPersonne est:", type(nomPersonne))
print("Le type de la variable prixHT est:", type(prixHT))
print("Le type de la variable paye est:", type(paye))
print("Le type de la variable paye est:", type(prenomPersonne))

# On affiche nos variables
print("Age = ", agePersonne)
print("Age = ", prenomPersonne)
print("Nom = ", nomPersonne)
print("PrixHT = ", prixHT)
print("Payé True or False = ", paye)


print("On crée une phrase avec nos variables")

print("L'age du client est : ", agePersonne, "ans. \nLe prix du produit: ", prixHT, "FCFA. \n Payé vraie ou faux: ", paye, ".")

# On va répeter la ligne du haut maintenat avec le .format
print("L'age du client est : ", agePersonne, "ans. \nLe prix du produit: ", prixHT, "FCFA. \n Payé vraie ou faux: ", paye, ".")

# On utilise la fonction .format(variable1, variable2,......)
texte = "L'age du client est {} et le prix est à {} FCFA "
print(texte.format(agePersonne, prixHT))

# La fontion input() qui permet de recuperer les valeurs du clavier
# Cette fonction renvoie une chaine de caractère (str) de base
montant = input("Entrez un montant")
print("Le Montant entré par l'utilisateur est: ", montant)

# On verifie le type de la variable montant
print("Le type de la vaiable montant est:", type(montant))

# Nous devons convertir le montant saisi par l'utilisateur en integer int() 
# pour ne pas avoir des erreurs dans nos operations.
montant = int(montant)

# Le nouvel type de la variable montant
print("Le nouveau type de la vaiable montant est:", type(montant))

# On calcule maintenant le Prix TTC

prixTTC = prixHT + montant

print("Le prix TTC est: ", prixTTC)


# Au reste travailler travailler et travailler encore
# BONNE CHANCE 
