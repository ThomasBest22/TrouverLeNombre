#Coucou, je vais écrire ici mon "guess my number"

#hop les imports ici
import random
import sys #héhé
import time
import os
#voilà

#et ici les variables qui vont me servir, j'espère
while True:
    recommencer = True
    essais = 1
    your_guess=0.5
#voilà
    print("Coucou, \nDonne-moi deux nombres et tu vas devoir deviner celui que j'ai choisi entre les deux que t'as sélectionné\n")
    while recommencer == True:
        minimum = int(input("C'est quoi le minimum ?\n"))
        maximum = int(input("Et le maximum ?\n"))
        print("Donc ton minimum c'est " + str(minimum) + " et ton maximum " + str(maximum) + ".")
        if minimum>maximum:
            time.sleep(1)
            print("D'accord")
            time.sleep(1)
            print("Non attends")
            time.sleep(1)
            print("Allez, mets un maximum plus grand que ton minimum")
            time.sleep(1)
            continue
        oui_ou_non= input("C'est ça ? (réponds par oui ou non)\n")
        oui_ou_non_minuscule = oui_ou_non.lower()
        if oui_ou_non_minuscule == "oui":
            recommencer = False
        if oui_ou_non_minuscule == "non":
            recommencer = True
        if oui_ou_non_minuscule != "oui" and oui_ou_non_minuscule != "non":
            print("Ah oui donc méga lourd celui-là")
            time.sleep(1)
            print("Une petite vengeance ? Allez")
            time.sleep(1)
            sys.exit()
    le_nombre = str(random.randint(minimum,maximum))
    print("Je te rappelle juste que le nombre à deviner est entier donc pas de virgules, de points ou de trucs comme ça.")
    time.sleep(1)
    print("C'est le moment de deviner")
    time.sleep(1)
    print("Ton nombre est compris entre " + str(minimum) + " et " + str(maximum))
    time.sleep(1)

    while your_guess != le_nombre:
        your_guess=input("Essai numéro " + str(essais) + " :\n")
        if your_guess != le_nombre:
            essais=essais+1
            time.sleep(1)
            if your_guess > le_nombre:
                print("Non, plus bas")
            else:
                print("Non, plus haut")
            time.sleep(1)
    else:
        print("Bien joué. Le nombre était " + str(le_nombre) + " et tu as deviné en " + str(essais) + " essais")
        time.sleep(2)
        oui_ou_nonv2= input("Tu veux rejouer ? (réponds par oui ou non)\n")
        oui_ou_non_v2min = oui_ou_nonv2.lower()
        if oui_ou_non_v2min == "non":
            rejouer=False
            print("Pas de problème.\nSalut !")
            time.sleep(1)
            sys.exit()
        if oui_ou_non_v2min == "oui":
            rejouer=True
            print("Pas de problème ! Laisse moi juste me réinitialiser")
            time.sleep(2)
            print("Réinitialisation terminée")
            time.sleep(1)
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
        if oui_ou_non_v2min != "oui" and oui_ou_non_v2min != "non":
            print("T'as toujours pas compris ?")
            time.sleep(1)
            print("Cadeau !")
            time.sleep(1)
            sys.exit()
