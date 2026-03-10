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
        label = QLabel("Bonjour")
        bouton = QPushButton("Cliquez ici")
        bouton.clicked.connect(self.ma_fonction)
        self.line_edit=QLineEdit()
        #self pour que ma fonction le reconnaisse

        # 4. Ajouter les widgets au layout
        layout.addWidget(label)
        layout.addWidget(bouton)
        layout.addWidget(self.line_edit)

        # 4. Appliquer le layout au widget central
        central_widget.setLayout(layout)

        #5. Ajouter le centralwidget à la MainWindow
        self.setCentralWidget(central_widget)
    
    def ma_fonction(self):
        mon_texte=self.line_edit.text()
        print(mon_texte)


if __name__=="__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()
