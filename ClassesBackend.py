import mysql.connector
from tkinter.messagebox import showerror,showinfo,askyesno

class classe_Backend:
    def __init__(self,curseur):

        self.curseur=curseur
    def AddDefaultClasse(self,liste):
        try:
            self.Identifiant=liste[0]
            self.Designation=liste[1]

            sql = 'INSERT INTO tb_classepardefaut  VALUES ( %s,%s)'
            val = (self.Identifiant,self.Designation)
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES', "Classe Ajoutées")
        except Exception as exp :
            er=str(exp)[0]+''+str(exp)[1]+''+str(exp)[2]+''+str(exp)[3]
            if er=='1062':
                showerror('GEST-NOTES', "La classe avec cette identifiant existe")
            else:
                showerror('GEST-NOTES',str(exp))


    # la requete de modification des donnees 
    def UpdateDataClasseDefault(self,liste):
        try:
            sql = 'UPDATE tb_classepardefaut  SET  id_classe=%s,Libelle=%s WHERE id_classe = %s'
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

    def GetDataClasseDefault(self):
        try:
            sql = 'SELECT * FROM tb_classepardefaut'
            self.curseur.execute(sql)
            resultat= self.curseur.fetchall()
            return resultat
        except Exception as exp :
            showerror('Erreur', str(exp))

    def GetDataClasseParalle(self):
        try:

            sql = 'SELECT * from tb_classes'
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
            sql = 'SELECT * FROM tb_classes'
            self.curseur.execute(sql)
            resultat= self.curseur.fetchall()
            return resultat
        except Exception as exp :
            showerror('Erreur', str(exp))

    def AddClasseParalele(self,liste):
        try:
            self.Identifiant=liste[0]
            self.Designation=liste[1]
            self.IdPar=liste[2]

            sql = 'INSERT INTO tb_classes  VALUES (%s,%s,%s)'
            val = (self.Identifiant,self.Designation,self.IdPar)
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES', "Classe Ajoutées")
        except Exception as exp :
            er=str(exp)[0]+''+str(exp)[1]+''+str(exp)[2]+''+str(exp)[3]
            if er=='1062':
                showerror('GEST-NOTES', "La classe avec cette identifiant existe")
            else:
                showerror('GEST-NOTES',str(exp))

    # la requete de modification des donnees 
    def UpdateDataClassParallele(self,liste):
        try:
            sql = 'UPDATE tb_classes  SET  id_classe=%s,desiClasse=%s WHERE id_classe = %s'
            val = (liste[0],liste[1],liste[0])
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES','Modification reussi')
        except Exception as exp :
            showerror('GEST-NOTES', str(exp))

    def DeleteClasseClassParallele(self,liste):
        try:
            sql = 'delete from tb_classes WHERE id_classe = %s'
            val = (liste[0],)
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES','Suppression reussi')
        except Exception as exp :
            showerror('GEST-NOTES', str(exp))

