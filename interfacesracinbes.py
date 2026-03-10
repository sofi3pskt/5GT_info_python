from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

class MyWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        # 1. Créer le widget conteneur central
        central_widget = QWidget()

        # 2. Créer un layout
        layout = QVBoxLayout()
        #soit Layout en grille -> QGridBoxLayout() MAIS il faut préciser coordonnées
        #soit Layout en vertical -> QVBoxLayout()

        # 3. Créer des widgets
        label = QLabel("Bonjour! Dans la fonction y=ax^2+bx+c:")
        labela= QLabel("Que vaut a?")
        self.a_edit=QLineEdit()
        labelb= QLabel("Que vaut b?")
        self.b_edit=QLineEdit()
        labelb= QLabel("Que vaut c?")
        self.c_edit=QLineEdit()
        bouton = QPushButton("Calculer racines!")
        bouton.clicked.connect(self.ma_fonction)
        #self pour que ma fonction le reconnaisse

        # 4. Ajouter les widgets au layout
        layout.addWidget(label)
        layout.addWigdet(labela)
        layout.addWigdet(labelb)
        layout.addWigdet(labelc)
        layout.addWidget(bouton)
        layout.addWidget(self.a_edit)
        layout.addWidget(self.b_edit)
        layout.addWidget(self.c_edit)

        # 4. Appliquer le layout au widget central
        central_widget.setLayout(layout)

        #5. Ajouter le centralwidget à la MainWindow
        self.setCentralWidget(central_widget)
    
    def ma_fonction(self):
        a=self.a_edit.text()
        a=float(a)
        b=self.a_edit.text()
        b=float(b)
        c=self.a_edit.text()
        c=float(c)
        delta= (b**2)-4*a*c
        if delta<0:
            print("Cette fonction n'a pas de racines!")
        elif delta>0:
            racine1=(-b+(sqrt(delta)))/2*a
            racine2=(-b-(sqrt(delta)))/2*a
            print(racine1,"et",racine2,"sont les racines de cette fonction!")
        elif delta==0:
            racine2=(-b-(sqrt(delta)))/2*a
            print(racine2,"est la seule racine de cette fonction!")
        else:
            print("Erreur")
        
        
        


if __name__=="__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()
