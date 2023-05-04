

print("Créer et manipuler les fichiers avec python")
"""


            r (Lecture seule)
            w (Ecrire avec remplacement)
            a (Ecrire avec ajout en fin du fichier)
            x (Lecture et ecriture)
            r+ (Lecture/écriture dans un meme fichier)
"""

doc = open("includes/texte.txt", "r")
# print(doc.read())  lire le document

line = doc.readline(2)  #recuper les 2 premiers caracteres du fichier
print(line) #qui est 17

line = int(line) #On converti la variable en entier (int)

addition = 23 + line #Operation
print(addition)

line = doc.readlines() #recuperer les lignes restantes
print(line)



# doc.close() fermer le fichier

print("\n")

# AUTRES FACON D'AFFICHER LE DOCUMENT
with open("includes/texte.txt", "r") as feuille:
    content = feuille.read()
    print(content)

# On verifie si le fichier est ouvert ou fermé
if feuille.closed:
    print("Fichier fermé")
else:
    print("Fichier toujours ouvert")

"""
A partir du moment ou vous quitter le with le fichier se ferme automatiquement
"""
