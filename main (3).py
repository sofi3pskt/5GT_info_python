liste_gouts=[]

def menu():
  print("Ecris ce que tu aimes et j'en ferrai une liste.")
  print("Tapes stop si tu souhaites arreter et voir ta liste!")
  print()
  réponse=input("Qu'est ce que tu aimes? ")

  if réponse=="stop":
    print("Voici ce que tu aimes : ")
    for gout in liste_gouts:
      print(gout)
    print()
    print("Au revoir!")
  
  else:
    liste_gouts.append(réponse)
    print()
    menu()


if __name__=="__main__":
  print("Bienvenue dans ce programme qui vous demande ce que vous aimez!")
  menu()


