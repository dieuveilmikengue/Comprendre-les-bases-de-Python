"""
Une methode de chaine de caractere travaille sur une copie, et pas sur la chaine elle meme.

str.upper(), str.lower(), str.capitalize(), str.title()
str.center(largeur, caractere de remplissage)

str.find(chaine, debut, fin) trouver l'indice du mot dans chaine en respectant la casse
str.index(chaine, debut, fin) trouver l'indice du mot dans chaine en respectant la casse
str.strip() Enleve les espaces avant et apres
str.replace
str.len
"""

texte = "Bonjour tout le monde"

print(texte.find("tout"))

try:
    print(texte.index("tout"))
except ValueError:
    print("La lettre ou le mot n'existe pas dans le texte")

print(texte.strip(" "))

print(texte.replace("jour", "pour"))
print(texte.replace("B", "L"))
print(len(texte)) #Recuperer la longueur de la chaine
print(texte[:5]) #Recuperer une partie(5) de la chaine en commmencant par 0 

help(str)

# help(str) pour voir d'autres elements