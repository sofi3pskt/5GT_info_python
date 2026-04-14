
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
import sys
from view_MVC_todolist import UI

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI()
    ui.show()
    app.exec()
