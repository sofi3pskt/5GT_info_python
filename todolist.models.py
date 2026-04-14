import datetime

class Task(object):
    #définir caractéristiques (attributs) de l'objet en faisant appel à la class
    #atrributs propres à l'objet
    def __init__(self):
        self.text=""
        self.priority=int()
        #entier car prend moins place en mémoire
        self.done= bool()
        self.html= ""
        self.date=datetime.datetime.now()
        self.id=int()

    def gen_html(self):
        if self.done :
            #car pas nécessaire de mettre True, car issue ou Vrai ou Faux
            #méthode = fonction propre à l'objet
            self.html=f"<p style='color: grey'><s>{self.text}</s></p>"

        elif not self.done:
            if self.priority==0:
                self.html=f"<p style='color: red'>{self.text}</p>"
            elif self.priority==1:
                self.html=f"<p style='color: orange'>{self.text}</p>"
            elif self.priority==2:
                self.html=f"<p style='color: green'>{self.text}</p>"
