from random import *

"""
randint(a, b): generer les entiers de [a à b]
randrange(a, b, n): generer les entiers de [a à b] avec un saut valeur de n
uniform(a, b): generer les nombres decimaux de a à b
choice(list): generer un choix dans list ou un tableau par exemple
shuffle(list): boulverser l'ordre d'une liste

"""

valeur1 = randint(0, 10) 
print(valeur1)

valeur2 = uniform(0, 10) 
print(valeur2)

c = randrange(0, 20, 2)
print(c)

for i in range(5):
    print(randrange(0, 20, 2))

valeur3 = ["Mike", "Lebake", "Dieuveil", "Diska"]
print(choice(valeur3))

valeur4 = [1, 2, 3, 4, "Mike", "Lebake", "Dieuveil", "Diska"]
shuffle(valeur4)
print(valeur4)

for x in range(6): # x va parcourir les 6 valeurs qui se trouve dans le range
    print(randint(1, 6)) #ET les afficher à noter que ces valeurts sont dans l'intervalle de 1 à 6

for x in range(6): # x va parcourir les 6 valeurs qui se trouve dans le range
    print(uniform(1, 6)) #ET les afficher à noter que ces valeurts sont dans l'intervalle de 1 à 6

for x in range(5): # x va parcourir les 5 valeurs qui se trouve dans le range
    print(choice(valeur3)) #En generer un element de la liste au hasard

for x in range(5): # x va parcourir les 5 valeurs qui se trouve dans le range
    shuffle(valeur4)
    print(valeur4) #En generer un element de la liste au hasard