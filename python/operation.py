"""
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

"""

# Ici on va travailler avec les nombres:
nombre1 = 12
nombre2 = 15
nombre3 = 3

texte1 = "Hello"
texte2 = "Word !"

# On va incrementer la variable nombre1 qui est 12 de 7, diminuer nombre2 de 9 et multiplier nombre par 5
nombre1 += 7
nombre2 -= 9
nombre3 *= 5

# La nouvelle valeur de nombre1
print("La nouvelle valeur de nombre1 est :", nombre1)
print("La nouvelle valeur de nombre1 est :", nombre2)
print("La nouvelle valeur de nombre1 est :", nombre3)


# On zffectue quelques operations tout en recuperant nos resultats en entier (int)
# NB: l'opération va se faire avec les nouvelles valeurs des variables

print(nombre1, " + ", nombre2, " = ", nombre1 + nombre2)
print(nombre1, " / ", nombre2, " = ", int(nombre1 / nombre2)) #A la base la valeur sortante sera en float mais on prefère recuperer cela en int pour simplifier les choses
print(nombre1, " - ", nombre2, " = ", nombre1 - nombre2)
print(nombre1, " * ", nombre2, " = ", nombre1 * nombre2)
print(nombre1, " % ", nombre2, " = ", nombre1 % nombre2) #le resultat est 1. Ceci s'explique du fait que 19 / 6 = 3, 3 * 3 = 18 et 19 - 18 = 1, c'est ce 1 que nous avons comme reponse finale 

# Opérations sur les chaines de caractères ou concatenation 

texte = texte1+" "+texte2 # le symbole + represente la concatenation entre les chaines de caractères
print(texte)

# C'EST LA FIN DU COURS SUR LES PERATIONS

