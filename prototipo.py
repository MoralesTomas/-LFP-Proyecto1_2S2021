import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

import webbrowser

class ejemplo_GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("Interfaces//vtnPrincipal.ui", self)
        

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     GUI = ejemplo_GUI()
#     GUI.show()
#     sys.exit(app.exec_())

nombreArchivo = "C:\\Users\\DELL\\3D Objects\\ejemplo.html"
webbrowser.open_new_tab(nombreArchivo)