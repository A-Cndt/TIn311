from qtpy.QtWidgets import QMainWindow, QApplication
from qtpy import uic
import sys

class mainWindow(QMainWindow):
    """
    Classe représentant la fenêtre principale de l'IHM de commande.

    Attributes
    ----------
    instr1Bt, instr2Bt, ..., instr6Bt : QPushButton
        Boutons pour la mise à jour de l'état des instruments.
    instr1IP, instr2IP, ..., instr6IP : QLineEdit
        Champs de saisie des adresses IP des instruments.
    """

    def __init__(self, path, ui):
        """
        Initialise la fenêtre principale avec l'interface utilisateur spécifiée.

        Paramètres :
        - path (str) : Le chemin vers le dossier contenant l'interface utilisateur.
        - ui (str) : Le nom du fichier d'interface utilisateur.
        """
        super(mainWindow, self).__init__()
        uic.loadUi(path + "/" + ui, self)
        self.connect_buttons()
        self.show()
    
    def connect_buttons(self):
        """
        Connecte les boutons des instruments aux méthodes de mise à jour correspondantes.
        """
        buttons = [self.instr1Bt, self.instr2Bt, self.instr3Bt, self.instr4Bt, self.instr5Bt, self.instr6Bt]
        ips = [self.instr1IP, self.instr2IP, self.instr3IP, self.instr4IP, self.instr5IP, self.instr6IP]

        for button, ip in zip(buttons, ips):
            button.clicked.connect(lambda state, b=button, i=ip: self.updateBt(b, i))


    def updateBt(self, widget, ip):
        """
        Met à jour l'état du bouton et envoie la modification à la base de données.

        Paramètres :
        - widget (QPushButton) : Le bouton qui a été cliqué.
        - ip (QLineEdit) : Le champ de saisie de l'adresse IP correspondant au bouton.
        """
        IP = ip.text()
        if widget.text() == 'ON' :
            widget.setText('OFF')
            widget.setStyleSheet("background-color: red;") 
        elif widget.text() == 'OFF' :
            widget.setText('ON')
            widget.setStyleSheet("background-color: green;")

        # Envoyer la modification à la BDD
if __name__ == "__main__":
    app = QApplication([])
    print(sys.argv)
    IHM_commande = mainWindow(sys.argv[1], sys.argv[2])
    sys.exit(app.exec_())