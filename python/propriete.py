print("Comprendre les Proprietés en Python")



class Humain:
    def __init__(self, nom, age) -> None:
        print("creation d'un humain")
        self.nom = nom
        self._age = age
    
    def _getage(self):
        try:
            return self._age
        except AttributeError:
            print("L'age n'existe pas")

    def _setage(self, nouvel_age):
        if nouvel_age < 0:
            self._age = 0
        else:
            self._age = nouvel_age

    def _delage(self, ):
         del self._age

    #property (getter, setter, deleter, helper)
    age = property(_getage, _setage, _delage, "Je suis l'age")


h1 = Humain("Mike", 26)

print(h1.age)

h1.age = 4

print(h1.age)

del h1.age
print(h1.age)

help(Humain.age)