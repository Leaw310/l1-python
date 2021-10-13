#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    mes_secondes = temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]
    return mes_secondes 

mon_temps = (3,23,1,34)
secondes = tempsEnSeconde(mon_temps)
print(tempsEnSeconde(mon_temps)) 


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    mes_jours = seconde // 86400
    mes_heures = (seconde - (mes_jours * 86400)) // 3600
    mes_minutes = (seconde - (mes_jours * 86400) - (mes_heures*3600)) // 60
    mes_secondes = (seconde - (mes_jours * 86400) - (mes_heures*3600) - (mes_minutes*60)) // 60
    return (mes_jours,mes_heures,mes_minutes,mes_secondes)

temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")


#fonction auxiliaire ici

def afficheTemps(temps):
    if temps[0] == 1 :
        print (str("nombre de jour:"), int(temps[0]), end="")
    elif temps[0] > 1: 
        print (str("nombre de jours:"), int(temps[0]), end="")
    if temps[1] == 1 :
        print (str(", nombre d'heure:"), int(temps[1]), end="")
    elif temps[1] > 1: 
        print (str(", nombre d'heures:"), int(temps[1]), end="")
    if temps[2] == 1 :
        print (str(", nombre de minute:"), int(temps[2]), end="")
    elif temps[2] > 1: 
        print (str(", nombre de minutes:"), int(temps[2]), end="")
    if temps[3] == 1 :
        print (str(", nombre de seconde:"), int(temps[3]), end="")
    elif temps[3] > 1: 
        print (str(", nombre de secondes:"), int(temps[3]), end="")
afficheTemps((1,0,14,23))   


def demandeTemps():
    pass

afficheTemps(demandeTemps())
