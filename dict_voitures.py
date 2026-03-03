
from datetime import datetime
#on importe une sous partie de la bibliotheque datetime car pas besoin de tout


def prod_list_voiture():
    """"Lecture du fichier contenant les infos et production d'une liste où chaque élément est un dict contenant les informations d'un véhicule"""
    list_voitures=[]
    with open('./voitures_location.tsv', 'r', encoding='utf8') as f: #Pour ouvrir un fichier en python
        for ligne in f:
            dict_datas={} #Accolade pour montrer que c'est un dico
            datas=ligne.strip().split('\t')
            dict_datas['id']=int(datas[0]) #L
            dict_datas['moteur']=datas[1]
            dict_datas['kilometrage']=int(datas[2])
            dict_datas['marque']=datas[3]
            dict_datas['places']=int(datas[4])
            dict_datas['année']=int(datas[5])
            list_voitures.append(dict_datas)
    return list_voitures

def old_cars():
    """Crée une liste de voitures trop vieilles,cad les voitures de plus de 10 ans et plus de 5000km"""
    #2 types de 'ou' pour conditions
    #XOR et NOR
    list_old_cars=[]
    now=datetime.now()
    current_year=now.year
    for voiture in list_voitures:
        age=current_year-voiture['année']
        if (age>10) & (voiture['kilometrage']>5000):
            list_old_cars.append(voiture['id'])
    return list_old_cars

def print_engine_type():
    dict_carburant={}
    for voiture in list_voitures:
        moteur=voiture['moteur']
        if moteur not in dict_carburant.keys():
            #keys(), fonction pour récupérer clés du dict
            dict_carburant[moteur]=[]
        dict_carburant[moteur].append(voiture['id'])
        
        max_length=max(len(dict_carburant['Diesel']),len(dict_carburant['Essence']), len(dict_carburant['Electrique']))
#code moche car plusieurs actions sur même ligne
        print(40*'=')
        print("|   Essence  |   Diesel   | Electrique |")
        print(40*'-')
        
        for i in range(max_length):
            print("|",end="")
            #pour éviter le saut à la ligne
            try:
                car_id=dict_carburant['Diesel'][i]
                blanks=12-len(str(car_id))
                print(f"{blanks*' '}{car_id}",end="")
            except:
                print("            ",end="")
                print("|",ends="")
                        #pour éviter le saut à la ligne
            try:
                car_id=dict_carburant['Essence'][i]
                blanks=12-len(str(car_id))
                print(f"{blanks*' '}"f"{car_id}",end="")
            except:
                print("          ",end="")
                print("|",ends="")
                        #pour éviter le saut à la ligne
            try:
                car_id=dict_carburant['Electrique'][i]
                blanks=12-len(str(car_id))
                print(f"{blanks*' '}{car_id}",end="")

            except:
                print("            ",end="")
                print("|",ends="")
                
    
        
        #if voiture['moteur']=='essence':
            #dict_carburant['essence'].append(voiture['id'])
        #elif voiture['moteur']=='diesel':
            #dict_carburant['diesel'].append(voiture['id'])
        #elif voiture['moteur']=='electrique':
            #dict_carburant['electrique'].append(voiture['id'])
        #else:
            #print(f"Un moteur inconnu a été rencontré pour la voiture: {voiture['id']}")
    
        
def sport_cars():
    """Crée une liste de voitures de sport, cad les voitures de 2 à 4 places et à essence"""
    list_sport_cars=[]
    list_old_cars=old-cars()
    for voiture in list_voitures:
        if (voiture['places']<5) & (voiture['moteur']=="Essence"):
            if voiture['id'] not in list_old_cars:
                #in not in type de test
                list_sport_cars.append(voiture['id'])
    return list_sport_cars

def print_list_cars(list_selected_cars, list_name):
    #la variable peut être remplacée par une variable n'importe ex: peut mettre 'a' MAIS pour être plus précis, plus clair, on met un nom en rapport avec les variables qui vont être introduites
    print(f"Voici la liste des voitures {list_name} :")
    #f string de formatage, on peut introduire des variables directement !entier et string (l'entier sera converti en string)
    for car in list_selected_cars:
        print(car)
    
def menu():
    print("Pour afficher les véhicules trop anciens, tapez 1")
    print("Pour afficher une liste des véhicules par type de carburant, tapez 2")
    print("Pour afficher une liste de voitures de sport, tapez 3")
    print("Pour enregistrer un nouveau véhicule, tapez 4")
    print("Pour supprimer un véhicule de la liste, tapez 5")
    print("Pour enregistrer la liste dans un fichier, tapez 6")
    choix= input("Votre choix: ")
    
    try:
        choix=int(choix)
        
        if choix==1:
            list_old_cars=old_cars()
            #ainsi on stocke la valeur donnée (par return) par la fonction def
            print_list_cars(list_old_cars,"trop vieilles") #les variables introduites avec lesquelles on va executer la fonction def
        
        elif choix==2:
            print_engine_type()
            
        elif choix==3:
            list_sport_cars=sport_cars()
            print_list_cars(list_sport_cars,"de sport")
        
    

        
    except:
        menu()
    
    #while choix not in [1, 2, 3, 4, 5, 6]:
        #print("	Veuillez choisir un numéro entre 1 et 6")
        

                
  
if __name__=="__main__":
    list_old_cars=old_cars()
    prod_list_voiture()
        #for voiture in list_voitures: # 'voiture' est le nom d'une variable temporaire définie par 'for in liste', pourrait avoir n'importe quel nom
        # voiture.values(), liste des valeurs pour chaque voiture
        # voiture.keys(), liste des étiquettes de chaque dictionnaire dans la liste
        # voiture['marque'], liste des éléments avec l'étiquettes 'marque' dans chaque dictionnnaire
        # print(voiture'), liste des dictionnaires de façon structurée
        #= fonction pour parcourir un dictionnaire
        
    menu()
