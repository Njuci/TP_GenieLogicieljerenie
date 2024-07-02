import mysql.connector
from tkinter.messagebox import showerror,showinfo,askyesno

class cours_Backend:
    def __init__(self,curseur,connexion):

        self.curseur=curseur
        self.connexion=connexion
        
    def AddDomain(self,liste):
        try:
            self.Identifiant=liste[0]
            self.Designation=liste[1]

            sql = 'INSERT INTO tb_domaines VALUES (%s,%s)'
            val = (self.Identifiant,self.Designation)
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES', "Domaines Ajoutés")
        except Exception as exp :
            er=str(exp)[0]+''+str(exp)[1]+''+str(exp)[2]+''+str(exp)[3]
            if er=='1062':
                showerror('GEST-NOTES', "La classe avec cette identifiant existe")
            else:
                showerror('GEST-NOTES',str(exp))


    # la requete de modification des donnees 
    def UpdateDomaines(self,liste):
        try:
            sql = 'UPDATE tb_domaines  SET  id_domaine=%s,designDomaine=%s WHERE id_domaine = %s'
            val = (liste[0],liste[1],liste[2])
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES','Modification reussi')
        except Exception as exp :
            showerror('GEST-NOTES', str(exp))
    def DeleteClasseClasseDefault(self,liste):
        try:
            sql = 'delete from tb_classepardefaut WHERE id_classe = %s'
            val = (liste[0],)
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES','Suppression reussi')
        except Exception as exp :
            showerror('GEST-NOTES', str(exp))

    def GetDataDomaines(self):
        try:
            sql = 'SELECT * FROM tb_domaines'
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
            self.connexion.start_transaction()

            #Requete d'insertion de cours
            sql = 'INSERT INTO tb_cours  VALUES (%s,%s,%s,%s,%s,%s)'
            val = (liste[0],liste[1],liste[2],liste[3],liste[4],liste[5])
            self.curseur.execute(sql,val)

            #requetes verification s'il y a des élèves déjà inscrit dans la classe
            sql = 'SELECT CD.id_classe,CL.id_classe as IDCLASSE,I.id_Eleve,A.id_anneeSco from tb_classepardefaut as CD inner join tb_classes as CL inner join tb_inscription as I inner join tb_anneescolaires  as A ON CD.id_classe=CL.id_classe_1 and CL.id_classe=I.id_classe and I.id_anneeSco=A.id_anneeSco and A.active=1'
            self.curseur.execute(sql)
            resultat= self.curseur.fetchall()
            print(resultat)

            # Ajouts de cours pour les eleves deja inscrits s'ils existe

            if len(resultat)!=0:
                for i in (resultat):
                    sql1='INSERT INTO tb_cotation (id_Eleve,id_anneeSco,id_classe,id_Cours) VALUES (%s,%s,%s,%s)'
                    val1 = (i[2],i[3],i[1],liste[0])
                    self.curseur.execute(sql1,val1)
   
            showinfo('GEST-NOTES', "Cours Ajoutés")
            self.connexion.commit()
        except Exception as exp :
            self.connexion.rollback()
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

