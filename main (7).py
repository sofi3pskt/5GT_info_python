import random

nombre1= random.randint(-100,100)
nombre2= random.randint(-100,100)

question="Que vaut la somme de "+str(nombre1)+" et "+str(nombre2)+" ? "
reponse= input(question)
reponse=int(reponse)


valid=0

while valid==0:
 try: 
   reponse= int(reponse)
   valid=1

 except:
   print("Votre réponse n'est pas valide...")
   reponse= input("Je réessaie. Quelle est votre réponse?")


somme1= nombre1+nombre2


if somme1==reponse:
  print("Vous avez la bonne réponse! Félicitations!")

elif somme1!=reponse:
  print("Vous n'avez pas la bonne réponse...Dommage!")


else: 
  print("Je ne comprends pas votre réponse.")