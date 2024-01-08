# -*- coding: utf-8 -*-
"""
"""

import socket
import threading

class serveur(object):
    """
    Classe serveur pour gérer plusieurs connexions client.
    """
    def __init__(self, PORT):
        """
        Initialise le serveur avec le port spécifié.
        
        Paramètres :
        - port (int) : Le port sur lequel le serveur écoutera.
        """
        self.IP: str   = "localhost"
        self.PORT: int = PORT
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def start(self):
        """
        Lance le serveur en se liant à l'IP et au port spécifiés,
        et en écoutant les connexions entrantes.

        Retourne :
        - int : 0 si réussi.
        """
        self.socket.bind((self.IP, self.PORT))
        self.socket.listen()
        
        print(f"Le serveur écoute sur {self.IP}:{self.PORT}")
        
        return 0
    
    def listen(self):
        """
        Écoute les connexions entrantes des clients et crée un nouveau thread
        pour gérer chaque client connecté.
        """
        while True:
            client_sock, client_address = self.socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_sock, client_address))
            client_thread.start()

    def handle_client(self, socket, address):
        """
        Gère une connexion client individuelle.

        Paramètres :
        - client_socket (socket) : L'objet socket représentant la connexion client.
        - client_address (tuple) : Un tuple représentant l'adresse du client (IP, port).
        """
        print(f"Connexion de {address}")
        self.clients.append(socket)

        
    def close(self):
        """
        Ferme le socket du serveur.
        """
        self.socket.close()

# Exemple d'utilisation :
if __name__ == "__main__":
    PORT = 8080  # Changez-le avec le port désiré
    serveur = serveur(PORT)
    serveur.start()
    thread_serveur = threading.Thread(target=serveur.listen)
    thread_serveur.start()

    # Gardez le thread principal en cours d'exécution
    try:
        thread_serveur.join()
    except KeyboardInterrupt:
        print("\nArrêt du serveur...")
        serveur.close()