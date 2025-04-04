print("Bienvenu(e) dans notre restaurant!")
print("Pour un hamburger, tapez 1.")
print("Pour une pizza, tapez 2.")
print("Pour une salade, tapez 3.")

choix=input("Votre choix:")
choix=int(choix)

while choix not in [1,2,3]:
  print("Veuillez répondre par 1,2 ou 3.")
  choix=input("Votre choix:")
  choix=int(choix)

if choix==1:
  print("Vous avez choisi: hamburger")

elif choix==2:
  print("Vous avez choisi: pizza")

elif choix==3:
  print("Vous avez chosi: salade")

else:
  pass
 
