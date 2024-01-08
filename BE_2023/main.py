# -*- coding: utf-8 -*-
"""
TEl 311 - Initiation aux bases de données -- BE 2023
====================================================

Ce fichier est le code Python principal du sujet du BE de BDD IPSA 2023

Le but de ce BE est de mettre en relation une IHM de commande d'instruments
avec une interface de monitoring en faisant transiter les données par une base de données.
Les données sont stockées avec un ID d'instrument, une date et une valeur, qui sont ensuite utilisés
par l'IHM de monitoring pour l'affichage.


Changelog
---------
- 25/12/2023 : Création

Bugs et Corrections
-------------------
- N/A
"""

# %% Informations Gébérales du Code
__author__     = "Alexandre CONDETTE"
__copyright__  = "Copyright 2023, Alexandre CONDETTE"
__credits__    = ["Alexandre CONDETTE"]
__licence__    = "MIT"
__version__    = "1.0.0"
__maintainer__ = "Alexandre CONDETTE"
__email__      = "alexandre2.condette@ipsa.fr"
__status__     = "Production"

# %% Import des librairies
# Libs pour l'IHM
from qtpy.QtWidgets import QApplication, QMainWindow
from qtpy import uic
import matplotlib.pyplot as plt

# Autres
import sys
import pathlib
import os
import threading
import time
import random
import subprocess
import matplotlib.pyplot as plt
import tkinter as tk

# Libs Perso
import src.config as Config
import src.instrument as Inst
import src.serveur as Server
import src.client as Client
import src.commande as Command
import src.monitoring as Monitor

# %% Constantes et variables globales
# Chemins
CURRENT_PATH: pathlib.Path  = pathlib.Path(os.getcwd())
UIS_PATH: pathlib.Path      = CURRENT_PATH / "uis"
CONFIG_PATH: pathlib.Path   = CURRENT_PATH / "config" 

# STR
MAIN_UI: str     = "main.ui"    # Nom du fichier de l'IHM
CONFIG_FILE: str = "instruments.config"

# INT
DUREE_SIMU: int = 10   # Durée de la simulation en secondes
PORT: int = random.randint(1000,10000)

# DICT
INSTRUMENTS: dict = dict()

# %% Classe de l'IHM Principale

# %% Main
if __name__ == "__main__":
    """
    """
    # Etape 1 : Lire le fichier de configuration Instrument :
    instrumentsData: Config.confFile = Config.confFile(CONFIG_PATH / CONFIG_FILE)
    
    # Etape 2 : Initialisation des instruments
    for instrument in instrumentsData.sections : 
        tmp_Instr: Inst.Instrument = Inst.Instrument()

        tmp_Instr.NOM    = instrument       
        tmp_Instr.IP     = instrumentsData.parser[instrument]['IP']
        tmp_Instr.FREQ   = int(instrumentsData.parser[instrument]['FREQ'])
        tmp_Instr.status = [0 if instrumentsData.parser[instrument]['STATUS'] == "OFF" else 1]
        tmp_Instr.FABR   = instrumentsData.parser[instrument]['FABR']

        if tmp_Instr.IP == "192.168.1.103" :
            tmp_Instr.dataRange = 50
        INSTRUMENTS[instrument] = tmp_Instr

    # Etape 3 : Initilisation de l'IHM de Commande
    IHM_commande = subprocess.Popen(["python", pathlib.Path("src/commande.py"), UIS_PATH, MAIN_UI])

    # Etape 4 : Initilisation du Serveur
    serveur = Server.serveur(PORT)
    serveur.start()
    serveur_thread = threading.Thread(target=serveur.listen)

    serveur_thread.start()

    time.sleep(1)

    for instrument in INSTRUMENTS.values():
        instrument.connexion = Client.client(PORT)
        instrument.connexion.connect()
        instrument.thread = threading.Thread(target=instrument.send_data_to_server)
        instrument.thread.start()

    # Etape 5 : Initialisation de l'Interface de monitoring
    # Création de la fenêtre principale
    root = tk.Tk()

    # Initialisation de l'IHM de monitoring
    ihm_monitoring = Monitor.IHM_Monitoring(root)
    ihm_monitoring.start()
    #threading.Thread(target=root.mainloop).start()    

    # Etape 6 : Réception du serveur
    t0 = time.time()
    tf = time.time()
    x1 = 0
    x3 = 0
    while tf <= t0 + DUREE_SIMU: 
        t = int(time.time())
        for client in serveur.clients :
            client.settimeout(0.1)
            try:
                data = client.recv(1048).decode()
            except:
                pass
            if "192.168.1.100" in data.split(':')[0]:
                x1 = float(data.split(': ')[-1])
            elif "192.168.1.103" in data.split(':')[0]:
                x3 = float(data.split(': ')[-1])
            ihm_monitoring.plot(t, x1, 1)
            ihm_monitoring.plot(t, x3, 3)
            ihm_monitoring.update(1)
        time.sleep(0.1)
        tf = time.time()
 

# FIN
root.mainloop()
os.system('pkill -9 python')    

