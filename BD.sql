drop database if exists gest_espoir;
create database gest_espoir;
use gest_espoir;
drop table if exists ClasseParDefaut;
drop table if exists AnneeScolaire;
drop table if exists Eleves;
drop table if exists Domaines;
drop table if exists Classes;
drop table if exists Cours;
drop table if exists Inscription;
drop table if exists Cours;
drop table if exists Cotation;

CREATE TABLE AnneeScolaire(
   idAnnee Varchar(4),
   libelle VARCHAR(25),
   AnneeEncours BOOL ,
   PRIMARY KEY(idAnnee)
);

CREATE TABLE ClasseParDefaut(
   idDefault Varchar(4),
   Libelle VARCHAR(25),
   PRIMARY KEY(idDefault)
);

CREATE TABLE Eleves(
   Id_Eleve Varchar(4),
   nomEleve VARCHAR(25),
   sexe CHAR(1),
   lieuNaissance VARCHAR(25),
   dateNaissance DATE,
   NumPermanent VARCHAR(25),
   PRIMARY KEY(Id_Eleve)
);

CREATE TABLE Domaines(
   Id_Domaines Varchar(4),
   designation CHAR(25),
   PRIMARY KEY(Id_Domaines)
);

CREATE TABLE classes(
   Id_classes Varchar(4),
   nouveauNom CHAR(25),
   idDefault Varchar(4),
   PRIMARY KEY(Id_classes),
   constraint pk_DefaultClasse FOREIGN KEY(idDefault) REFERENCES ClasseParDefaut(idDefault)
);

CREATE TABLE Cours(
   Id_Cours Varchar(4),
   nomCours CHAR(25),
   maxP INT,
   maxExamen INT,
   Id_classes Varchar(4),
   Id_Domaines Varchar(4),
   PRIMARY KEY(Id_Cours),
   constraint pk_classeId FOREIGN KEY(Id_classes) REFERENCES classes(Id_classes),
   constraint pk_domaineId FOREIGN KEY(Id_Domaines) REFERENCES Domaines(Id_Domaines)
);

CREATE TABLE Inscription(
   idanneeScolaire Varchar(4),
   Id_Eleves Varchar(4),
   Id_classe Varchar(4), 
   PRIMARY KEY( idanneeScolaire,Id_Eleves),
   FOREIGN KEY(idanneeScolaire) REFERENCES AnneeScolaire(idAnnee),
   FOREIGN KEY(Id_Eleves) REFERENCES Eleves(Id_Eleve),
   FOREIGN KEY(Id_classe) REFERENCES Classes(Id_classes)
);

CREATE TABLE Cotation(
   idAnnee Varchar(4),
   Id_Eleve Varchar(4),
   Id_Cours Varchar(4),
   Id_classes Varchar(4),
   P1 float(5,2),
   P2 float(5,2),
   P3 float(5,2),
   P4 float(5,2),
   E1 float(5,2),
   E2 float(5,2),
   PRIMARY KEY(idAnnee, Id_Eleve, Id_Cours, Id_classes),
   FOREIGN KEY(idAnnee) REFERENCES AnneeScolaire(idAnnee),
   FOREIGN KEY(Id_Eleve) REFERENCES Eleves(Id_Eleve),
   FOREIGN KEY(Id_Cours) REFERENCES Cours(Id_Cours),
   FOREIGN KEY(Id_classes) REFERENCES classes(Id_classes)
);
