class Chaise(): #objet
    def __init__(self): #fonction du constructeur
        self.materiau=""
        self.prix=int()
        self.hauteur=float()
        self.largeur=float()
        self.profondeur=float()
        self.couleur=""
        self.poids=int()
        self.surface=float()
    #self pour déterminer que c'est un attribut de la classe, sans quoi on ne peut pas appeler les attributs depuis l'extérieur de la classe
    #= pour le "matériau" la chaise vaut, on parle des diff variables depuis l'intérieur de la classe      
    def calc_surface(self): #def dans classe = méthode
        self.surface=self.largeur*self.profondeur
chaise=Chaise()
#instanciation d'une variable, ici la classe chaise !comme nombre1=int(nombre)
chaise.materiau="bois"
chaise.prix=160
chaise.hauteur=0.8
chaise.profondeur=0.5
chaise.largeur=0.4
    
chaise.calc_surface()

print(chaise.surface)                                                                                                                                                                 
