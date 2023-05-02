
"""

class Animal:

    idAnimal = 0
    def __init__(self, nom) -> None:
        self.nom = nom
        Animal.idAnimal += 1

    def manger(self):
        print(self.nom, " mange")

class Reptile(Animal):
    def __init__(self, nom, regimeAlimentaire) -> None:
        Animal.__init__(self, nom)
        self.regime = regimeAlimentaire
        print("{} {} mange {} ".format(Animal.idAnimal, nom, self.regime))

    def manger(self):
        print("Le reptile mange")


lezard = Reptile("Lezard", "le chien")
momba = Reptile("Momba", "les gens")

if issubclass(Reptile, Animal):
    print("Reptile herite d'Animal")


"""

class Vehicule:
    def __init__(self, nom_vehicule, essence_vehicule) -> None:
        self.nom = nom_vehicule
        self.essence = essence_vehicule

    def deplacement(self):
        print("Le vehicule {} se deplace".format(self.nom))
        
    

class Voiture(Vehicule):
    def __init__(self, nom_voiture, essence_voiture, puissance_voiture) -> None:
        Vehicule.__init__(self, nom_voiture, essence_voiture)
        self.puissance = puissance_voiture

v1 = Vehicule("BMW", 58)
print(" Nom vehicule: {}, Quantité d'essence: {}".format(v1.nom, v1.essence))

voiture1 = Voiture("toyota", 85, 415)
print(" Nom vehicule: {}, Quantité d'essence: {}, Puissance: {}".format(voiture1.nom, voiture1.essence, voiture1.puissance))

