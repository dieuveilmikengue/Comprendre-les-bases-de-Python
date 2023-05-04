import time
import datetime
from datetime import date

print("Comprendre la gestion de la date et l'heure\n")


"""
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

"""

debut = time.time()
print("Premier texte")

"""
time.sleep(5) #Mettre en pause le programme pendant 5 secondes
"""
fin = time.time()
print("Second texte")

# On recupère le temps d'execution entre ces deux
print(f"premier texte - second texte: {fin - debut}s")

#l'heure locale
today = time.localtime()
print(today)

"""
La fonction mktime() permet de recuperer le nombre des seconde en partant d'une date...
"""
print(time.mktime(today))


tms1 = time.strftime("%A/%B/%Y")
tms2 = time.strftime("%d/%m/%Y")
tms3 = time.strftime("%Z")
print(tms1)
print(tms2)
print(tms3)

temps = datetime.time(23, 5, 30) # (heure, minute, secode)

#On recupère la date et l'heure actuelle avec la fonction datetime
print(datetime.datetime.now())
print(date.today())

date1 = datetime.datetime(1997, 1, 30, 23, 5, 55) # (annee, mois, jour, heure, minute, secode)
date2 = datetime.datetime(2023, 4, 30, 11, 55, 25)

# Calculer l'age
age = date.today().year - date1.year #On recupère juste les années pour faire l'operation
print(f"l'age est {age} ans")

print(date1 > date2) #On compare les deux date on virifiant si date1 est plus recente que date2

#On peut egalement faire
if date1 > date2:
    print("La date 1 est plus recente")
else:
    print("La date 2 est plus recente")

print(date2.year) #On recupère l'annee du date2