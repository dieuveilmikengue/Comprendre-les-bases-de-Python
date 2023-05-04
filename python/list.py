elements = ["arc", "bouclier", "marteau", "epee", "couteau", "fourchette"]
chiffres = [5, 17, 2, 31, -4, 10, 6, -17]
chiffres2 = [5, 17, 2, 31, -4, 10, 6, -17]
melange = ["arc", "bouclier", "marteau", 31, -4, 10]

elements.remove("bouclier") #SUpprimmer l'element bouclier dans la liste
print(elements[:])

# L'indice des valeurs commence par 0
print("L'element arc se trouve en {}e position".format(elements.index("arc"))) #Retrouver l'element arc dans la liste et afficher son index

obj_del = elements.index("arc")     #retrouver l'element arc dans la liste
del elements[obj_del]               #SUpprimmer l'element arc de la liste
print(elements[:])      #On reaffiche la nouvelle liste

print(chiffres)  #On affiche notre liste des chiffres
print(melange)  #On affiche notre liste des chiffres

elements.sort()         #trier les element par ordre Alphabetique
chiffres.sort()        #trier les element par ordre croissant
print(elements)  ##On reaffiche notre liste
print(chiffres)  #On reaffiche notre liste des chiffres

chiffres.reverse()
elements.reverse()
melange.reverse()
print(chiffres) #renverser l'ordre d'affichage
print(elements)
print(melange)

print(min(elements)) #La valeur minimale d'une liste
print(min(chiffres))


print("Nombre d'epee: ", elements.count("epee")) #.count permet de compter le nombre de fois que l'element se repete dans la liste

# RECUPERER LES MOTS D'UNE PHRASE DANS UNE LISTE
chaine = "Bonjour tout le monde"
chaine = chaine.split(" ")
print(chaine)


# joindre les elements d'une liste pour creer une phrase
avec_join = ["Bonjour", "les", "gens"]
phrase = " ".join(avec_join)
print(phrase)

# CONCATENER DEUX LISTES
joindre = elements+chiffres
print(joindre)

joindre2 = chiffres+melange
print(joindre2)

# RECHERCHJER UN ELEMENT DANS UNE LISTE
trouveOU = [s for s in elements if "ou" in s]
print(trouveOU)

trouver_ee = list(filter(lambda x: 'ee' in x, elements))
print(trouver_ee)


#UNION, INTERSECTION, DIFFERENCE ET SYMETRIC DIFFERENCE
"""
Union: La réunion de deux ensembles A et B, se note A | B et désigne l'ensemble des éléments qui appartiennent (à la fois) à A et à B. 
C'est l'ensemble des éléments qui appartiennent à A ou à B ou les deux.

Intersection: L'intersection entre A et B est l'ensmble des elements qui appartiennent à A et B, se note A & B

Diefference: En arithmétique, la différence est le résultat de la soustraction entre deux nombres, se note A - B.

Symetric diference: La différence symétrique des ensembles A et B sont ces éléments dans A ou B, mais pas dans A et B, se note A ^ B.

"""

# union
print(set(chiffres) | set(melange)) #On recupère l'union dans un ensemble
print(list(set(chiffres) | set(melange))) #On utilise list pour afficher dans une liste


# intersection
print(set(chiffres) & set(melange)) #On recupère l'intersection dans un ensemble
print(list(set(chiffres) & set(melange))) #On utilise list pour afficher dans une liste
  
# difference
print(set(chiffres) - set(melange)) #On recupère la difference dans un ensemble
print(list(set(chiffres) - set(melange))) #On utilise list pour afficher dans une liste
  
# symmetric difference
print(set(chiffres) ^ set(melange)) #On recupère la symetric difference dans un ensemble
print(list(set(chiffres) ^ set(melange))) #On utilise list pour afficher dans une liste
