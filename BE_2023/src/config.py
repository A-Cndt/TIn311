import configparser
import pathlib

class confFile(object):
    """
    Classe représentant un fichier de configuration.

    Attributes
    ----------
    parser : ConfigParser
        Objet ConfigParser pour lire le fichier de configuration.
    sections : list
        Liste des sections du fichier de configuration.
    """
    def __init__(self, path:pathlib.Path):
        """
        Initialise l'objet ConfFile avec le chemin vers le fichier de configuration.

        Paramètres :
        - path (pathlib.Path) : Le chemin vers le fichier de configuration.
        """
        self.parser = configparser.ConfigParser() 
        self.parser.read(path)
        self.sections = self.parser.sections()
