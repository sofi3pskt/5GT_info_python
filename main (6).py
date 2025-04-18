print("Bonjour et bienvenue dans ce programme qui vous dit bonjour!")

choix="o"

while choix == "o":
  print("Bonjour!")
  choix=input("Souhaitez-vous être salué encore une fois? ")
  while choix not in ["o","n"]:
    choix=input("Veuillez répondre par 'o' pour oui et par 'n' pour non!") 
 

print("Au revoir!")







