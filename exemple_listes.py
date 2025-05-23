liste_points=[12,15,18,10,5,2,7]

somme=0
nb_echecs=0
liste_echec=[]
for cote in liste_points:
    somme=somme+cote
    if cote<10:
        nb_echecs+=1
        liste_echec.append(cote)
moyenne=somme/len(liste_points)
print("Votre moyenne vaut : ",round(moyenne,3))
print("Il y a ",nb_echecs,"echecs")
print("Les echecs sont : ")
for echec in liste_echec:
    print(echec,"/20")