import mysql.connector
from tkinter.messagebox import showerror,showinfo,askyesno

class annee_Backend:
    def __init__(self,curseur,con):

        self.curseur=curseur
        self.connexion=con
    def AddAnnee(self,liste):
        try:
            self.Identifiant=liste[0]
            self.Designation=liste[1]

            sql = 'INSERT INTO tb_anneescolaires VALUES (%s,%s,%s)'
            val = (self.Identifiant,self.Designation,0)
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES', "Années Ajoutée")
        except Exception as exp :
            er=str(exp)[0]+''+str(exp)[1]+''+str(exp)[2]+''+str(exp)[3]
            if er=='1062':
                showerror('GEST-NOTES', "L'année avec cette identifiant existe")
            else:
                showerror('GEST-NOTES',str(exp))


    # la requete de modification des donnees 
    def UpdateAnnee(self,liste):
        try:
            sql = 'UPDATE  tb_anneescolaires  SET  id_anneeSco=%s,libelle=%s WHERE id_anneeSco= %s'
            val = (liste[0],liste[1],liste[2])
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES','Modification reussi')
        except Exception as exp :
            showerror('GEST-NOTES', str(exp))

    #activation de l'annee 
    def ActiverAnnee(self,liste):

        try:
  
            self.connexion.start_transaction()

            sql = 'UPDATE  tb_anneescolaires  SET  active=0'
            self.curseur.execute(sql)

            sql1='UPDATE  tb_anneescolaires  SET  active=1 WHERE id_anneeSco= %s'
            val1 = (liste[0],)
            self.curseur.execute(sql1,val1)
            self.connexion.commit()
            showinfo('GEST-NOTES','Année Activée, l\'application doit s\'arrêter pour intégré l\'année activée')
        except Exception as exp :
            self.connexion.rollback()
            er=str(exp)[0]+''+str(exp)[1]+''+str(exp)[2]+''+str(exp)[3]
            if er=='1062':
                showerror('GEST-NOTES', "L'annee existe déjà")
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
    def DeleteClasseClasseDefault(self,liste):
        try:
            sql = 'delete from tb_classepardefaut WHERE id_classe = %s'
            val = (liste[0],)
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES','Suppression reussi')
        except Exception as exp :
            showerror('GEST-NOTES', str(exp))

    def GetDataAnnee(self):
        try:
            sql = 'SELECT * FROM tb_anneescolaires'
            self.curseur.execute(sql)
            resultat= self.curseur.fetchall()
            return resultat
        except Exception as exp :
            showerror('Erreur', str(exp))

    def GetDataClassesDefaultCombo(self):
        try:

            sql = 'SELECT * from tb_classepardefaut'
            self.curseur.execute(sql)
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
            sql = 'SELECT * FROM tb_cours'
            self.curseur.execute(sql)
            resultat= self.curseur.fetchall()
            return resultat
        except Exception as exp :
            showerror('Erreur', str(exp))
    def GetDataCoursClasse(self,idCours):
        try:
            sql = 'SELECT * FROM tb_cours where id_classe=%s'
            val=[idCours,]
            self.curseur.execute(sql,val)
            resultat= self.curseur.fetchall()
            return resultat
        except Exception as exp :
            showerror('Erreur', str(exp))

    def AddCours(self,liste):
        try:

            sql = 'INSERT INTO tb_cours  VALUES (%s,%s,%s,%s,%s,%s)'
            val = (liste[0],liste[1],liste[2],liste[3],liste[4],liste[5])
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES', "Cours Ajoutés")
        except Exception as exp :
            er=str(exp)[0]+''+str(exp)[1]+''+str(exp)[2]+''+str(exp)[3]
            if er=='1062':
                showerror('GEST-NOTES', "Le cours avec cette identifiant existe")
            else:
                showerror('GEST-NOTES',str(exp))

    # la requete de modification des donnees 
    def UpdateCours(self,liste):
        try:
            sql = 'UPDATE tb_cours  SET  desi_cours=%s,MaxP=%s,MaxExamen=%s,id_classe=%s,id_domaine=%s WHERE id_Cours = %s'
            val = (liste[1],liste[2],liste[3],liste[4],liste[5],liste[0])
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES','Modification reussi')
        except Exception as exp :
            showerror('GEST-NOTES', str(exp))

    def DeleteCours(self,liste):
        try:
            sql = 'delete from tb_cours WHERE id_cours= %s'
            val = (liste[0],)
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES','Suppression reussi')
        except Exception as exp :
            showerror('GEST-NOTES', str(exp))

