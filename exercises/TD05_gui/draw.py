from tkinter.constants import END


print("Bienvenue dans le jeu du Pendu")
play=int(input("Tape 1 si tu veux jouer ! \n "))
if play == 1 :  
    prénom=input("Quel est ton nom ?")
    print("\n")
    print("Salut", prénom)
    import random
    liste_mots=["laitue", "hareng", "jambon", "pharynx", "phoque", "langue",
                "stylo","agent","fromage","whisky","billet","boyaux",
                "laser","joystick","crane","joyeux","cahier","camping","argent",
                "rivage","physique",]
    score = 0
    print("Tu as 6 vies")
    print("\n")
    vie = 6
    while play == 1 :
        vie = 6
        mot=(liste_mots[random.randint(0,20)])
        longueur=len(mot)
        barre=["_ "]
        barre=barre*longueur
        grandeur=longueur
    else:
                print("Raté")
                if grandeur==longueur :
                    print(longueur*"_ ")
                else:
                    print (resultat)
                vie=vie-1
                print("Il te reste",vie,"vies")
                print("\n")
    if vie==0 :
            print("Tu as perdu")
    elif grandeur==0 :
            print("Bravo ! Tu as trouvé le mot !")
            score=score+5
            print("Tu a gagné 5 points !")
    replay=int(input("Tape 1 pour rejouer, et sur 2 si tu veux quitter le jeu   "))
    if replay != 1 :
        #break
    print(prénom,"vous avez un score de ",score)
