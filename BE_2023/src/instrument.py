# -*- coding: utf-8 -*-
"""
"""

# %%
# %%
import random
import time

# %%
class Instrument(object):
    """
    Classe représentant un instrument.
    """
    def __init__(self):
        """
        Initialise les attributs de l'instrument.
        """
        self.IP: str  = "01:01:01:01:01:01"        # Adresse Mac de l'équipement
        self.NOM: str  = "Test"                     # Nom de l'équipement
        self.FABR: str = "None"                     # Nom du Fabricant
        self.FREQ: float = 1.0  # Fréquence en Hz
        self.status: int = 0
        self.connexion = None
        self.dataRange = 25
        self.thread = None

    def send_data_to_server(self):
        """
        Envoie des données au serveur à une fréquence spécifiée.
        """
        while True : 
            if self.status == [1]:
                try:
                    data = random.uniform(self.dataRange - 1, self.dataRange + 1)
                    data = f"{self.IP} : {data}"
                    self.connexion.socket.send(str(data).encode())

                except Exception as e:
                    print(f"Error sending data to the server: {e}")
            
            else:
                pass

            time.sleep(float(1/float(self.FREQ)))