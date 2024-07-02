import mysql.connector
from tkinter.messagebox import showerror,showinfo,askyesno

class Eleve_Backend:
    def __init__(self,curseur,con):

        self.curseur=curseur
        self.connexion=con
    def AddDataEleve(self,liste):
        try:


            sql = 'INSERT INTO tb_eleves  VALUES (%s,%s,%s,%s,%s,%s)'
            val = (self.idEleve,self.Nom,self.Sexe,self.Lieu,self.Date,self.NumP)
            self.curseur.execute(sql,val)
        except Exception as exp :
            er=str(exp)[0]+''+str(exp)[1]+''+str(exp)[2]+''+str(exp)[3]
            if er=='1062':
                showerror('GEST-NOTES', "L'élève est déjà Ajouté")
            else:
                showerror('GEST-NOTES',str(exp))

    def InscrirEleve(self,liste):
        print(liste)

        try:
            self.idEleve=liste[0]
            self.Nom=liste[1]
            self.Sexe=liste[2]
            self.Lieu=liste[3]
            self.Date=liste[4]
            self.NumP=liste[5]
            self.Classe=liste[7]
            self.Annee=liste[6]

            self.connexion.start_transaction()

            sql = 'INSERT INTO tb_eleves  VALUES (%s,%s,%s,%s,%s,%s)'
            val = (self.idEleve,self.Nom,self.Sexe,self.Lieu,self.Date,self.NumP)
            self.curseur.execute(sql,val)


            sql1='INSERT INTO tb_inscription (id_Eleve,id_anneeSco,id_classe) VALUES (%s,%s,%s)'
            val1 = (self.idEleve,self.Annee,self.Classe)
            self.curseur.execute(sql1,val1)

            # la requete de selection de tous les cours d'une classe
            sql = 'SELECT tb_cours.id_Cours,tb_classes.id_classe FROM tb_classes inner join tb_cours on tb_classes.id_classe_1=tb_cours.id_classe and tb_classes.id_classe=%s'
            val=[self.Classe,]
            
            self.curseur.execute(sql,val)
            resultat= self.curseur.fetchall()
            if len(resultat)!=0:
                for i in (resultat):
                    sql1='INSERT INTO tb_cotation (id_Eleve,id_anneeSco,id_classe,id_Cours) VALUES (%s,%s,%s,%s)'
                    val1 = (self.idEleve,self.Annee,self.Classe,i[0])
                    self.curseur.execute(sql1,val1)
            else:
                self.connexion.rollback()
                showerror('GEST-NOTES', "Veuillez terminer la configuration de la classe")
            self.connexion.commit()

            showinfo('GEST-NOTES','Elève Inscrit')
        except Exception as exp :
            self.connexion.rollback()
            er=str(exp)[0]+''+str(exp)[1]+''+str(exp)[2]+''+str(exp)[3]
            if er=='1062':
                showerror('GEST-NOTES', "L'élève est déjà Inscrit")
            else:
                showerror('GEST-NOTES',str(exp))

    def ReeInscriptionEleve(self,liste):
        print(liste)

        try:
            self.idEleve=liste[0]
            self.Classe=liste[1]
            self.Annee=liste[2]
            self.connexion.start_transaction()

            sql1='INSERT INTO tb_inscription (id_Eleve,id_anneeSco,id_classe) VALUES (%s,%s,%s)'
            val1 = (self.idEleve,self.Annee,self.Classe)
            self.curseur.execute(sql1,val1)

            # la requete de selection de tous les cours d'une classe
            sql = 'SELECT tb_cours.id_Cours,tb_classes.id_classe FROM tb_classes inner join tb_cours on tb_classes.id_classe_1=tb_cours.id_classe and tb_classes.id_classe=%s'
            val=[self.Classe,]
            
            self.curseur.execute(sql,val)
            resultat= self.curseur.fetchall()
            if len(resultat)!=0:
                for i in (resultat):
                    sql1='INSERT INTO tb_cotation (id_Eleve,id_anneeSco,id_classe,id_Cours) VALUES (%s,%s,%s,%s)'
                    val1 = (self.idEleve,self.Annee,self.Classe,i[0])
                    self.curseur.execute(sql1,val1)
            else:
                self.connexion.rollback()
                showerror('GEST-NOTES', "Veuillez terminer la configuration de la classe")
            self.connexion.commit()

            showinfo('GEST-NOTES','Elève Inscrit')
        except Exception as exp :
            self.connexion.rollback()
            er=str(exp)[0]+''+str(exp)[1]+''+str(exp)[2]+''+str(exp)[3]
            if er=='1062':
                showerror('GEST-NOTES', "L'élève est déjà Inscrit")
            else:
                showerror('GEST-NOTES',str(exp))

    # la requete de modification des donnees 
    def UpdateData(self,liste):
        try:
            sql = 'UPDATE tb_eleves SET  nomEleve=%s,sexe=%s,lieuNaissance=%s,dateNaissance=%s,numPerm=%s WHERE id_Eleve = %s'
            val = (liste[0],liste[1],liste[2],liste[3],liste[4],liste[5])
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES','Elève '+liste[0]+' Modifié')
        except Exception as exp :
            showerror('GEST-NOTES', str(exp))

    def UpdateDataInscrit(self,liste):
        try:
            sql = 'UPDATE tb_inscription SET  id_classe=%s WHERE id_anneeSco = %s and id_Eleve = %s'
            val = (liste[1],liste[2],liste[0])
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES','Classe modifié')
        except Exception as exp :
            showerror('GEST-NOTES', str(exp))

    def DeleteData(self,Id):
        try:
            sql = 'DELETE FROM tb_eleves  WHERE id_Eleve = %s'
            val = (Id,)
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES','Elève supprimé avec succès')
        except Exception as exp :
            showerror('GEST-NOTES', str(exp))

    def GetDataEleves(self):
        try:
            sql = 'SELECT * FROM tb_eleves'
            self.curseur.execute(sql)
            resultat= self.curseur.fetchall()
            return resultat
        except Exception as exp :
            showerror('Erreur', str(exp))

    def GetDataElevesInscrits(self,annee,type):
        try:
            if type=='tous':
                sql = 'SELECT DISTINCT tb_eleves.id_Eleve,tb_eleves.nomEleve,tb_eleves.sexe,tb_inscription.id_classe,tb_classes.desiClasse from tb_eleves inner join tb_inscription inner join tb_classes on tb_eleves.id_Eleve=tb_inscription.id_Eleve and tb_classes.id_classe=tb_inscription.id_classe and tb_inscription.id_anneeSco=%s'
                val=(annee,)
                self.curseur.execute(sql,val)
                resultat= self.curseur.fetchall()
                return resultat
            else :
                sql = 'SELECT DISTINCT  tb_eleves.id_Eleve,tb_eleves.nomEleve,tb_eleves.sexe,tb_inscription.id_classe,tb_classes.desiClasse from tb_eleves inner join tb_inscription inner join tb_classes on tb_eleves.id_Eleve=tb_inscription.id_Eleve and tb_inscription.id_classe=%s and tb_classes.id_classe=tb_inscription.id_classe and tb_inscription.id_anneeSco=%s'
                val=(type,annee)
                self.curseur.execute(sql,val)
                resultat= self.curseur.fetchall()
                return resultat
        except Exception as exp :
            showerror('Erreur', str(exp))
    def getAnneeActive(self):
        try:
            sql = 'SELECT * FROM tb_anneescolaires where active=1'
            self.curseur.execute(sql)
            resultat= self.curseur.fetchall()
            return resultat
        except Exception as exp :
            showerror('Erreur', str(exp))
    def GetDataClasses(self):
        try:
            sql = 'SELECT * FROM tb_classes'
            self.curseur.execute(sql)
            resultat= self.curseur.fetchall()
            return resultat
        except Exception as exp :
            showerror('Erreur', str(exp))

