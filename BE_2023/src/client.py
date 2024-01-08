import socket

class client(object):
    """
    Classe client pour la gestion d'une connexion à un serveur.
    """
    def __init__(self, PORT):
        """
        Initialise le client avec le port spécifié.
        
        Paramètres :
        - port (int) : Le port sur lequel le client se connectera.
        """
        self.host = "localhost"
        self.port = PORT
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """
        Établit une connexion avec le serveur en utilisant l'adresse et le port spécifiés.
        """
        self.socket.connect((self.host, self.port))

    def close(self):
        """
        Ferme la connexion du client.
        """
        self.socket.close()
