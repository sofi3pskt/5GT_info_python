from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
from math import sqrt
import sys

class MyWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        central_widget = QWidget()

       
        layout = QVBoxLayout()

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
        label = QLabel("Bonjour! Dans la fonction y=ax^2+bx+c:")
        layout.addWidget(label)

        label= QLabel("Que vaut a?")
        layout.addWidget(label)

        self.line_edita=QLineEdit()
        layout.addWidget(self.line_edita)

        
        label= QLabel("Que vaut b?")
        layout.addWidget(label)

        self.line_editb=QLineEdit()
        layout.addWidget(self.line_editb)

        
        label= QLabel("Que vaut c?")
        layout.addWidget(label)

        self.line_editc=QLineEdit()
        layout.addWidget(self.line_editc)

        bouton = QPushButton("Résoudre")
        layout.addWidget(bouton)
        bouton.clicked.connect(self.ma_fonction)

 
    
    def ma_fonction(self):
        a=self.line_edita.text()
        a=float(a)
        b=self.line_editb.text()
        b=float(b)
        c=self.line_editc.text()
        c=float(c)
        delta = ((b)**2)-4*(a)*(c)
        if delta < 0:
            text="<p>Il n'y a <b>pas de racine</b> à cette fonction. </p>"
            
        elif delta > 0:
            racine1=((-b)+(sqrt(delta)))/2*a
            racine2=((-b)-(sqrt(delta)))/2*a
            text=f"<p>Il y a <b>deux racines</b> à cette fonction. </p>"
            text+=f"<p>Elles valent: "
            text+=f"<ul><li>{round(racine1,4)}</li>"
            text+=f"<li>{round(racine2,4)}</li></ul></p>"

        elif delta==0:
            racine=(-b-(sqrt(delta)))/2*a
            text=f"<p>Il y a <b>une racine</b> à cette fonction. </p>"
            text+=f"<p>Elle vaut: "
            text+=f"<ul><li>{round(racine,4)}</li></ul></p>"


        else:
            print("Erreur")

        print(text)
        dial_response = QMessageBox()
        dial_response.setText(text)
        dial_response.exec()
       

    

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = MyWidget()
    gui.show()
    app.exec()
