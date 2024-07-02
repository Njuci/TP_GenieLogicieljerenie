import mysql.connector
from tkinter.messagebox import showerror,showinfo,askyesno

class note_Backend:
    def __init__(self,curseur,compte,idTit,conn):
        self.compte=compte
        self.IdTitulaire=idTit
        self.connexion=conn

        self.curseur=curseur
    def AddNotes(self,liste):
        try:
            sql = 'update tb_cotation set P1=%s,P2=%s,P3=%s,P4=%s,E1=%s,E2=%s where id_Eleve=%s and id_anneeSco=%s and id_classe=%s and id_Cours=%s'
            val = (liste[0],liste[1],liste[2],liste[3],liste[4],liste[5],liste[6],liste[7],liste[8],liste[9])
            self.curseur.execute(sql,val)
            self.connexion.commit()
            showinfo('GEST-NOTES', "Elève coté")
        except Exception as exp :
            er=str(exp)[0]+''+str(exp)[1]+''+str(exp)[2]+''+str(exp)[3]
            if er=='1062':
                showerror('GEST-NOTES', "Erreur")
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

    def GetCours(self,idClasse):
        try:
            sql = 'SELECT tb_classes.id_classe,tb_cours.id_Cours,tb_cours.desi_cours FROM tb_classes inner join tb_cours on tb_classes.id_classe=%s and tb_classes.id_classe_1=tb_cours.id_classe  '
            val=[idClasse,]
            self.curseur.execute(sql,val)
            resultat= self.curseur.fetchall()
            return resultat
        except Exception as exp :
            showerror('Erreur', str(exp))

    def GetMaxCours(self,idClasse,idCours):
        try:
            sql = 'SELECT tb_cours.maxP,tb_cours.maxExamen FROM tb_classes inner join tb_cours on tb_classes.id_classe=%s and tb_classes.id_classe_1=tb_cours.id_classe and tb_cours.id_Cours=%s '
            val=[idClasse,idCours]
            self.curseur.execute(sql,val)
            resultat= self.curseur.fetchall()
            return resultat
        except Exception as exp :
            showerror('Erreur', str(exp))


    def GetDataClassesDefaultCombo(self,Annee):
        if self.compte=='admin':
            try:

                sql = 'SELECT * from tb_classes'
                self.curseur.execute(sql)
                resultat= self.curseur.fetchall()
                return resultat

            except Exception as exp :
                showerror('Erreur', str(exp))
        else:
            try:

                sql = 'SELECT tb_classes.id_classe,tb_classes.desiClasse,tb_classes.id_classe_1,tb_titulaire.idTut from tb_classes inner join tb_titulaire on tb_titulaire.id_anneeSco=%s and tb_titulaire.id_classe=tb_classes.id_classe and tb_titulaire.idtut=%s'
                val=[Annee,self.IdTitulaire]
                self.curseur.execute(sql,val)
                resultat= self.curseur.fetchall()
                return resultat

            except Exception as exp :
                showerror('Erreur', str(exp))

    def GetDataEleveCote(self,liste):
        try:
            sql = 'SELECT tb_eleves.id_Eleve,tb_eleves.nomEleve,tb_cotation.P1,tb_cotation.P2,tb_cotation.P3,tb_cotation.P4,tb_cotation.E1,tb_cotation.E2 FROM tb_eleves inner join  tb_cotation on tb_eleves.id_Eleve=tb_cotation.id_Eleve and tb_cotation.id_anneeSco=%s and tb_cotation.id_classe=%s and tb_cotation.id_Cours=%s '
            val=[liste[0],liste[1],liste[2]]
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

    #selection des enseignants ttiulaire par classe
    def getTitulaireClasse(self,liste):
        try:
            sql = 'SELECT E.nomTut,T.idtut from enseignantstitu E inner join tb_titulaire T on E.idtut=T.idtut and T.id_anneeSco=%s and T.id_classe=%s'
            val=[liste[0],liste[1]]
            self.curseur.execute(sql,val)
            resultat= self.curseur.fetchall()
            return resultat
           
        except Exception as exp :
            showerror('Erreur', str(exp))
        
    #La methode qui permet de renvoyer les données des bulletins d'une classe particulière
    def getDataInfosBulletins(self,liste):
            try:
                #La requete pour selectionner les informations sur les  élèves 
                sql = 'SELECT EL.id_Eleve as IdEleve,EL.nomEleve,EL.sexe,EL.lieuNaissance,EL.dateNaissance,EL.numPerm,CL.id_classe,Do.designDomaine,COU.desi_cours,COU.MaxP,COU.MaxExamen,CT.P1,CT.P2,CT.E1,CT.P3,CT.P4,CT.E2,CL.desiClasse FROM tb_eleves EL inner join tb_classes CL inner join tb_domaines DO inner join tb_cours COU inner join tb_cotation CT ON EL.id_Eleve=CT.id_Eleve and CT.id_classe=CL.id_classe and CT.id_Cours=COU.id_Cours and CT.id_anneeSco=%s and CL.id_classe=%s and CL.id_classe_1=COU.id_classe and COU.id_domaine=DO.id_domaine'
                val=[liste[0],liste[1]]
                self.curseur.execute(sql,val)
                resultat= self.curseur.fetchall()
                #Filtrage des données par élèves 


                nomEleve=""
                DonneeFiltre=[]
                DataEleve=[]

                #Filtrage de noms des élèves de façon à avoir des noms uniques dans les tableau
                idVer=""
                for i in (resultat):
                    IdEleve=i[0]
                    if idVer!=IdEleve:
                        for j in (resultat):
                            if IdEleve==j[0]:
                                if len(DataEleve)==0:
                                    liste=[j[0],j[1],j[2],j[3],j[4],j[17]]
                                    DataEleve.append(liste)
                                    break
                                else:
                                    ver=True
                                    for t in DataEleve:
                                        if t[0]==IdEleve:
                                            ver=False
                                            break
                                        else:
                                            ver=True
                                    if ver==True:
                                        liste=[j[0],j[1],j[2],j[3],j[4],j[17]]
                                        DataEleve.append(liste)
                        idVer=IdEleve
                
                #Filtrage des domaines 
                Domaines=[]
                Domaine=""
                for i in (resultat):
                    domaine=i[7]
                    if Domaine!=domaine:
                        for j in (resultat):
                            if domaine==j[7]:
                                if len(Domaines)==0:
                                    Domaines.append(j[7])
                                    break
                                else:
                                    ver=True
                                    for t in Domaines:
                                        if t==domaine:
                                            ver=False
                                            break
                                        else:
                                            ver=True
                                    if ver==True:
                                        Domaines.append(j[7])
                        Domaine=domaine

                #Filtrages de notes pour chaque élève et suivant le domaine
                ListefIltre=[[],[]]
                for i in (DataEleve):
                    ListefIltre[0].append(i)
                    for d in (Domaines):
                        for t in (resultat):
                            if t[0]==i[0] and t[7]==d:
                                liste=[t[7],t[8],t[9],t[10],t[11],t[12],t[13],t[14],t[15],t[16]]
                                ListefIltre[1].append(liste)

                    DonneeFiltre.append(ListefIltre)       
                    ListefIltre=[[],[]]
                return DonneeFiltre
            except Exception as exp :
                showerror('Erreur', str(exp))

    #Statistiques 

    #la methodes pour renvoyer les effectifs par classe

    def getEffectifClasse(self,liste):
        try:
            sql = 'SELECT E.Sexe,I.id_Eleve from tb_eleves as E inner join tb_inscription as I on I.id_eleve=E.id_Eleve and I.id_anneeSco=%s and I.id_classe=%s'
            val=[liste[0],liste[1]]
            self.curseur.execute(sql,val)
            resultat= self.curseur.fetchall()
            return resultat
        except Exception as exp :
            showerror('Erreur', str(exp))




