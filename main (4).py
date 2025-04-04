import datetime

print("Bonjour")

nom1 = input("Quel est ton nom?")
nom2 = input("Quel est le nom de ton/ta voisin/voisine?")
nombre1= input("En quelle année est-tu né(e)?")
nombre2= input("En quelle année ton/ta voisin/voisine est-il/elle né(e)?")
nombre1= int(nombre1)
nombre2= int(nombre2)

now= datetime.datetime.now()
now_year=now.year
age1= now_year-nombre1
age2= now_year-nombre2

print(nom1,"a",age1,"ans.")
print(nom2,"a",age2,"ans.")


if age1>age2: 
  soustraction1= age1-age2
  print(nom1,"est plus agé que",nom2,".")
  print(nom1,"et",nom2,"ont",soustraction1,"année(s) de différence.")


elif age1==age2:
  print(nom1,"et",nom2,"ont le même age.")
  print(nom1,"et",nom2,"n'ont pas d'années de différence.")


elif age1<age2:  
  soustraction2= age2-age1
  print(nom2,"est plus agé que",nom1,".")
  print(nom1,"et",nom2,"ont",soustraction2,"années de différence.")

else: 
  print("Une situation inattendue a été rencontrée.")

