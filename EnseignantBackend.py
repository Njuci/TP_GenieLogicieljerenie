import mysql.connector
from tkinter.messagebox import showerror,showinfo,askyesno

class enseignant_Backend:
    def __init__(self,curseur):

        self.curseur=curseur

        #Cryptage de mot de passe suivant l'algo rsa
        p=29
        q=37
        n=1073
        fi=1008
        e=773
        d=7901
        public=7731073
        priv=79011073
    def ChiffrerPassword(self,m):
            e=773
            d=7901
            n=1073
            listeChiffre=[]
            C=''
            Chaine=''
        
            for l in m:
                liste=[l,]
                C=pow (ord(liste[0]),e)%n
                listeChiffre.append(C)
            for l in listeChiffre:
                Chaine+=l+','
            print(Chaine)
    def AddDefaultClasse(self,liste):
        try:
            self.Identifiant=liste[0]
            self.Designation=liste[1]
            self.passeWord=liste[2]
  
            sql = 'INSERT INTO enseignantstitu  VALUES (%s,%s,%s)'
            val = (self.Identifiant,self.passeWord,self.Designation)
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES', "Enseignant (e) Ajouté (e)")
        except Exception as exp :
            er=str(exp)[0]+''+str(exp)[1]+''+str(exp)[2]+''+str(exp)[3]
            if er=='1062':
                showerror('GEST-NOTES', "L'Enseignant avec cette identifiant existe")
            else:
                showerror('GEST-NOTES',str(exp))
                print(str(exp))


    # la requete de modification des donnees 
    def UpdateDataClasseDefault(self,liste):
        try:
            sql = 'UPDATE enseignantstitu SET  idtut=%s,nomTut=%s,password=%s WHERE idtut = %s'
            val = (liste[0],liste[1],liste[2],liste[0])
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES','Modification reussi')
        except Exception as exp :
            showerror('GEST-NOTES', str(exp))
    def DeleteClasseClasseDefault(self,liste):
        try:
            sql = 'delete from enseignantstitu WHERE idtut = %s'
            val = (liste[0],)
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES','Suppression reussi')
        except Exception as exp :
            showerror('GEST-NOTES', str(exp))

    def GetDataEnseignant(self):
        try:
            sql = 'SELECT * FROM enseignantstitu'
            self.curseur.execute(sql)
            resultat= self.curseur.fetchall()
            return resultat
        except Exception as exp :
            showerror('Erreur', str(exp))

    def GetDataAffectation(self,Id):
        try:

            sql = 'SELECT enseignantstitu.idtut,enseignantstitu.nomTut,tb_classes.desiClasse,tb_titulaire.idtut from enseignantstitu inner join tb_classes inner join tb_titulaire on tb_titulaire.idtut=enseignantstitu.idtut and tb_titulaire.id_classe=tb_classes.id_classe and tb_titulaire.id_anneeSco=%s  '
            val=[Id,]
            self.curseur.execute(sql,val)
            resultat= self.curseur.fetchall()
            return resultat

        except Exception as exp :
            showerror('Erreur', str(exp))
    def GetDataClasses(self):
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

    def AddAffectation(self,liste):
        try:

            sql = 'INSERT INTO tb_titulaire  VALUES (%s,%s,%s)'
            val = (liste[0],liste[1],liste[2])
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES', "Enseignant Affecté")
        except Exception as exp :
            er=str(exp)[0]+''+str(exp)[1]+''+str(exp)[2]+''+str(exp)[3]
            if er=='1062':
                showerror('GEST-NOTES', " cet identifiant existe")
            else:
                showerror('GEST-NOTES',str(exp))

    # la requete de modification des donnees 
    def UpdateDataAffectation(self,liste):
        try:
            sql = 'UPDATE tb_titulaire  SET  id_anneeSco=%s,id_classe=%s WHERE idtut = %s'
            val = (liste[0],liste[1],liste[2])
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES','Modification reussi')
        except Exception as exp :
            showerror('GEST-NOTES', str(exp))

    def DeleteAffectation(self,liste):
        try:
            sql = 'delete from tb_titulaire  WHERE idtut = %s'
            val = (liste[0],)
            self.curseur.execute(sql,val)
            showinfo('GEST-NOTES','Suppression reussi')
        except Exception as exp :
            showerror('GEST-NOTES', str(exp))

