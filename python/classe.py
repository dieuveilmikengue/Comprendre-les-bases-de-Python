
"""
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

"""


class Humain:

    humain_cree = 0
    lieu_habitat = "Terre"

    def __init__(self, c_prenom, c_age) -> None:
        self.prenom = c_prenom #Attributs
        self.age = c_age #Attributs
        Humain.humain_cree += 1
        print("Creation d'un humain {}".format(Humain.humain_cree))

    def parler(self, message): #Methode standard
        self.message = message
        print("{}: {}".format(self.prenom, message))

    def changer_planete(self, nouvelle_planete): #Methode de class, cls methode
        Humain.lieu_habitat = nouvelle_planete

    changer_planete = classmethod(changer_planete)

    def definition(): #Methode statique
        print("L'etre Humain est considé comme le plus haut etre vivant")

    definition = staticmethod(definition)

    def _getage(self):
        return self.age
    
    def _setage(self, nouvel_age):
        if nouvel_age < 0:
            self.age = 0
        elif nouvel_age > 26:
            self.age = 26
        else:
            self.age = nouvel_age

    c_age = property(_getage, _setage)




print("Lancement du Programme")



"""
h1 = Humain("Mike", 26)
h2 = Humain("Diska", 21)

print("Prénom de h1: {}".format(h1.prenom))
h1.parler("Bonjour les codeurs")
print("Message: {}".format(h1.message))

print("Ancienne planete de {}: {}".format(h1.prenom, Humain.lieu_habitat))
h1.changer_planete("Mars")
print("Nouvelle planete de {}: {}".format(h1.prenom, h1.lieu_habitat))

print("L'age de h2: {}".format(h2.age))
h2.parler("Salut {}".format(h1.prenom))

Humain.definition()

"""

h1 = Humain("Mike", 26)

print(h1.c_age)

h1.c_age = -22

print(h1.c_age)