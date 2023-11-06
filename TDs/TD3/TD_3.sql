/* 1.2. Créer et supprimer une table */

-- Question 1 : Créer une nouvelle Table
CREATE TABLE IF NOT EXISTS Utilisateur(
	ID_Utilisateur INTEGER PRIMARY KEY AUTOINCREMENT,
	Prenom TEXT NOT NULL,
	Nom TEXT NOT NULL,
	Email TEXT
);

-- Question 2 : Faire de même avec les autres tables du MLD
CREATE TABLE IF NOT EXISTS Service(
	ID_Service INTEGER PRIMARY KEY AUTOINCREMENT,
	Nom TEXT NOT NULL,
	Type TEXT
);

CREATE TABLE IF NOT EXISTS Objet(
	Adresse_MAC TEXT PRIMARY KEY,
	ID_User INTEGER NOT NULL,
	Type TEXT,
	Parametre INT,
	
	FOREIGN KEY(ID_User) REFERENCES Utilisateur(ID_Utilisateur)
);

CREATE TABLE IF NOT EXISTS Souscription(
	ID_User INTEGER NOT NULL,
	ID_Service INTEGER NOT NULL,
	
	PRIMARY KEY(ID_User, ID_Service),
	FOREIGN KEY(ID_User) REFERENCES Utilisateur(ID_Utilisateur),
	FOREIGN KEY(ID_Service) REFERENCES Service(ID_Service)
);

/* 1.3. Insertion de données */

-- Question 1 : Insérer un premier utilisateur
INSERT INTO Utilisateur(ID_Utilisateur, Nom, Prenom, Email) VALUES
(1, 'Frederic', 'Sacre', 'frederic.sacre@ipsa.fr');

-- Question 2 : Insérer encore d’autres utilisateurs - N’utiliser qu’une seule requete SQL
INSERT INTO Utilisateur(ID_Utilisateur, Nom, Prenom, Email) VALUES
(2, 'Heylen', 'Alexandre', 'alexandre.heylen@gmail.com'),
(3, 'Meunier', 'Anne', 'anne.meunier@ipsa.fr'),
(4, 'Garcia', 'Margaret', 'margaret.garcia@spacebel.fr'),
(5, 'Andre', 'Zacharie', 'zacharie.andre@ipsa.fr'),
(6, 'Joly', 'Christine', 'cjy@cnes.fr'),
(7, 'Leleu', 'Maurice', NULL),
(8, 'Begue', 'Georges', 'georges.begue@ipsa.fr'),
(9, 'Pereira', 'Agathe', 'agathe.pereira@ipsa.fr');

-- Question 3 : Insérer les services suivants dans la table Service
INSERT INTO Service(ID_Service, Nom, Type) VALUES
(1, 'myKWHome', 'smarthome'),
(2, 'FridgAlert', 'smarthome'),
(3, 'RUNstats', 'quantifiedself'),
(4, 'traCARE', 'quantifiedself'),
(5, 'dogWATCH', NULL),
(6, 'carUSE', NULL);

-- Question 4 : Insérer les objets connectés suivants dans la table Objet
INSERT INTO Objet(Adresse_MAC, ID_User, Type, Parametre) VALUES
('f0:de:f1:39:7f:17', 1, NULL, NULL),
('f0:de:f1:39:7f:18', 2, NULL, NULL),
('f0:de:f1:39:7f:19', 2, 'thingtempo', 60);

-- Question 5 : Insérer les souscriptions adéquates dans la table Souscription
INSERT INTO Souscription(ID_User, ID_Service) VALUES
(2,1),
(2,2),
(1,3);

/* Selectionner et filtrer des données */

-- Question 1 : Lister les noms des services
SELECT Nom FROM Service;

-- Question 2 : Lister les noms et prénoms des utilisateurs par ordre croissant de nom
SELECT Nom, Prenom FROM Utilisateur ORDER BY Nom ASC ;

-- Question 3 : Lister les utilisateurs qui n’ont pas d’adresse mail ’ipsa’
SELECT * FROM Utilisateur WHERE Email NOT LIKE '%ipsa%' ;

-- Question 4 : Afficher l’utilisateur avec l’ID 5
SELECT * FROM Utilisateur WHERE ID_Utilisateur=5;

-- Question 5 : Lister les adresses MAC des objets connectés que possède l’utilisateur d’ID 2
SELECT Adresse_MAC FROM Objet WHERE ID_User=2;

-- Question 6 : Lister les adresses MAC des objets de type "thingtempo"
SELECT Adresse_MAC FROM Objet WHERE type='thingtempo '

-- Question 7 : Lister les ID et les noms de utilisateurs qui ne possèdent pas d’objet
SELECT DISTINCT ID_Utilisateur, Nom FROM Utilisateur WHERE ID_Utilisateur NOT IN (SELECT DISTINCT ID_User FROM Objet);

-- Question 8 : Lister les ID et les noms de utilisateurs qui possèdent des d’objets
SELECT DISTINCT ID_Utilisateur, Nom FROM Utilisateur WHERE ID_Utilisateur IN (SELECT DISTINCT ID_User FROM Objet);

/* Mettre à jour des données */

-- Question 1 : Mettre la valeur NULL pour toute la colonne type de la table service
UPDATE Service SET type=NULL;

-- Question 2 : Mettre le nom ’WatchDOG2’ pour la ligne qui a l’ID 5
UPDATE Service SET Nom='WatchDOG2' WHERE ID_Service = 5;

-- Question 3 : Multiplier par 1.5 les valeurs de la colonne param des objets connectés
UPDATE Objet SET Parametre = Parametre * 1.5;

-- Question 4 : Modifier le nom du champ Parametre de la table Objet pour devenir Param
ALTER TABLE Objet RENAME Parametre TO Param ;

-- Question 5 : Ajouter un champ "Anniversaire" à la table Utilisateur
ALTER TABLE Utilisateur ADD Anniversaire TEXT ;


/* Supprimer des données */

-- Question 1 : Supprimer l’utilisateur avec l’ID 1
DELETE FROM Utilisateur WHERE ID_Utilisateur = 1 ;

-- Question 2 : Supprimer la souscription de l’utilisateur d’ID 2 au service d’ID 1
DELETE FROM Souscription WHERE ID_User=2 AND ID_Service=1;

-- Question 3 : Supprimer toutes les lignes de la table Objet
DELETE FROM Objet ;

-- Question 4 : Supprimer la colonne "Anniversaire"
ALTER TABLE Utilisateur DROP Anniversaire;

-- Question 5 : Supprimer la table "Objet"
DROP TABLE Objet;