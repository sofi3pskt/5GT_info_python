from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt6.QtGui import QAction, QIcon

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.setWindowTitle("TODO List")
        self.set_menu()
        self.statusBar()
        #self.setWindowIcon(QIcon("./UI/icons/odego.svg"))

        #1. créer le widget conteneur central
        central_widget = QWidget 
    
    def set_menu(self):
        menubar = self.menuBar()
        appMenu = menubar.addMenu("&Application")
        taskMenu= menubar.addMenu("&Tâche")

        quitAction = QAction("&Quitter", self)
        quitAction.setShortcut('Crtl+Q')
        quitAction.setStatusTip("Quitter le programme")
        #fenêtre,texte d'information
        #petit texte qui s'affiche lorsque la souris passe sur l'action
        quitAction.triggered.connect(lambda : quit(self))

        appMenu.addAction(quitAction)
