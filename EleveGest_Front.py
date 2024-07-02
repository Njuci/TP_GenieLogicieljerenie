from tkinter import *
import os
from tkinter.messagebox import askyesno,showinfo,showwarning
import mysql.connector
from tkinter import ttk
from EleveBackend import Eleve_Backend
from tkinter import filedialog

from EtatDeSortie import DocumentsScolaire
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from tkcalendar import DateEntry
import datetime


class EleveGestFrontend:
    def __init__(self,Curseur,fen,con):
        self.Curseur=Curseur
        self.dataComboClass=[]
        self.Classes={}
        self.fen = fen
        self.DocumentPdf=DocumentsScolaire()
        self.Conexion=con

        #les instances de la classe
        self.DataGlob=Eleve_Backend(self.Curseur,self.Conexion)
     

        self.data=self.DataGlob.GetDataEleves()
        self.eleveFille=0
        self.eleveGarcon=0

        #Selection de l'annee active
        self.AnneeACtive=self.DataGlob.getAnneeActive()
        if len(self.AnneeACtive)==0:
            self.AnneeACtive=[('None','None')]

        #Sections des tous les élèves 
        self.title_section1 = Label(self.fen, text = "Tout les élèves", font = "Arial 12 ",fg='#6666b9').place(x=10, y=20)
        self.ElevesListe=Frame(self.fen,height=700,width=560,relief="groove")
        self.ElevesListe.place(x=10,y=60)

        #Les éléments de la section

        #Actions sur tous eleves 
        self.ActionBar=Frame( self.ElevesListe,height=40,width=520,relief="groove")
        self.ActionBar.place(x=20,y=120)
        self.AjoutBtn=Button(self.ActionBar,bg='#6666b9',text='AJOUTER +',relief='flat', font=('arial',9),fg='white',command=self.Ajouter)
        self.AjoutBtn.place(x=360,y=5, width=130,height=30)
        self.ActualiserBtn=Button(self.ActionBar,bg='white',text='Actualiser',relief='groove', font=('arial',9),fg='#6666b9',command=self.ActualiserEleves)
        self.ActualiserBtn.place(x=210,y=5, width=130,height=30)

        #Search section sur tous les eleves
        self.SearchBar=Frame( self.ElevesListe,height=50,width=500,relief="groove")
        self.SearchBar.place(x=20,y=160)
        self.SearchEntry=Entry(self.SearchBar,relief="flat")
        self.SearchEntry.place(x=0,y=10,width=350, height=30)
        self.SearchBtn=Button(self.SearchBar,bg='#6666b9',text='Rechercher',relief='flat', font=('arial',9),fg='white', command=self.Recherche)
        self.SearchBtn.place(x=360,y=10, width=130,height=30)

        #Creation de tableau pour tous les élèves 
        self.TabSection=Frame( self.ElevesListe,height=350,width=520,relief="groove")
        self.TabSection.place(x=0,y=250)
        self.tableau=ttk.Treeview(self.TabSection, columns=('IdEleve','Nom','Sexe','LieuNaissance','DateNaissance','NumPermanent'), show='headings')
        self.tableau.heading('IdEleve', text='IDENTIFIANT')
        self.tableau.heading('Nom', text='NOMS ET POST - NOMS')
        self.tableau.heading('Sexe', text='SEXE')
        self.tableau.heading('LieuNaissance', text='LIEU DE NAISS.')
        self.tableau.heading('DateNaissance', text='DATE DE NAISS.')
        self.tableau.heading('NumPermanent', text='NUM PERM.')
   
        self.tableau.column('Sexe',width=60,anchor='center')
        self.tableau.column('IdEleve',width=80,anchor='center')
        self.tableau.column('Nom',width=130,anchor='center')
        self.tableau.column('LieuNaissance',width=100,anchor='center')
        self.tableau.column('DateNaissance',width=100,anchor='center')
        self.tableau.column('NumPermanent',width=100,anchor='center')

        self.tableau.tag_configure('evenrow', background='lightblue')
        self.tableau.tag_configure('oddrow', background='lightyellow')

        #L'qppel des donnees et affichage de donnees dans le tableau
        if len(self.data)!=0:
            self.eleveFille=0
            self.eleveGarcon=0
            for i, row in enumerate(self.data):
                tag='evenrow' if i%2==0 else 'oddrow'
                self.tableau.tag_configure(tag,foreground='black')
                self.tableau.insert('','end',values=(row[0],row[1],row[2],row[3],row[4],row[5]),tags=(tag,))
                if row[2]=='M':
                    self.eleveGarcon+=1
                else:
                    self.eleveFille+=1

        self.tableau.bind('<Double-Button-1>',self.ModifierEleve)
        self.tableau.pack()

        #Les statistiques
        self.TotalEleve=Frame( self.ElevesListe,height=80,width=160,relief="groove",bg='lightyellow')
        self.TotalEleve.place(x=20,y=30)
        self.title_Tot = Label( self.TotalEleve, text = "Total", font = "Arial 12 ",bg='lightyellow',fg='#6666b9').place(x=10, y=10)
        self.Nbr_Tot = Label( self.TotalEleve, text = len(self.data), font = "Arial 30 ",bg='lightyellow',fg='#6666b9').place(x=60, y=10)

        self.TotalGarcons=Frame( self.ElevesListe,height=80,width=160,relief="groove",bg='lightyellow')
        self.TotalGarcons.place(x=200,y=30)
        self.title_Garc= Label( self.TotalGarcons, text = "Garçons", font = "Arial 12 ",bg='lightyellow',fg='#6666b9').place(x=10, y=10)
        self.Nbr_Garc = Label( self.TotalGarcons, text =self.eleveGarcon, font = "Arial 30 ",bg='lightyellow',fg='#6666b9').place(x=80, y=10)

        self.TotalFilles=Frame( self.ElevesListe,height=80,width=160,relief="groove",bg='lightyellow')
        self.TotalFilles.place(x=380,y=30)
        self.title_Garc= Label(self.TotalFilles, text = "Filles", font = "Arial 12 ",bg='lightyellow',fg='#6666b9').place(x=10, y=10)
        self.Nbr_Garc = Label(self.TotalFilles, text =self.eleveFille, font = "Arial 30 ",bg='lightyellow',fg='#6666b9').place(x=80, y=10)



        # Les informations sur les classes
        data=self.DataGlob.GetDataClasses()
        self.Classes["toutes les classes"]="tous"
        self.ClassesSansFiltre=[]
        self.dataComboClass.append("toutes les classes")
        if len(data)!=0:
            for i in (data):
                self.Classes[''+i[1]]=i[0]
                self.dataComboClass.append(i[1])
                self.ClassesSansFiltre.append(i[1])

        #Section sur eleves Inscrits
        self.title_section2 = Label(self.fen, text = "Les élèves Inscrits", font = "Arial 12 ",fg='#6666b9').place(x=580, y=20)
        self.EleveInscritListe=Frame(self.fen,height=700,width=500,relief="groove")
        self.EleveInscritListe.place(x=580,y=60)

        #Les éléments de la section eleves inscrits


         #Actions sur tous eleves inscrits
        self.ActionBar=Frame(  self.EleveInscritListe,height=40,width=520,relief="groove")
        self.ActionBar.place(x=20,y=120)
        self.InscrirBtn=Button(self.ActionBar,bg='#6666b9',text='INSCRIR',relief='flat', font=('arial',9),fg='white',command=self.InscrirEleve)
        self.InscrirBtn.place(x=330,y=5, width=130,height=30)

        self.Pdf=Button(self.ActionBar,bg='red',text='PDF',relief='flat', font=('arial',9),fg='white',command=self.getPdfListeEleve)
        self.Pdf.place(x=180,y=5, width=130,height=30)


        #choix Classe
        self.ClasseFilterSection=Frame( self.EleveInscritListe,height=50,width=500,relief="groove")
        self.ClasseFilterSection.place(x=20,y=160)

        self.Classe_label = Label(self.ClasseFilterSection, text = "Classe :", font = "Arial 12 ").place(x=0, y=10)
        
        self.CodeArtEnt=ttk.Combobox(self.ClasseFilterSection,values=self.dataComboClass)
        self.CodeArtEnt.place(x=100,y=10,width=200, height=30)
        self.CodeArtEnt.bind("<<ComboboxSelected>>",self.AfficherClasse)
        self.CodeArtEnt.current(0)


     
        #Creation de tableau pour les eleves inscrits
        self.TabSectionInscrit=Frame(self.EleveInscritListe,height=350,width=520,relief="groove")
        self.TabSectionInscrit.place(x=40,y=250)
        self.tableauInscrit=ttk.Treeview(self.TabSectionInscrit, columns=('IdEleve','Nom','Sexe'), show='headings')
        self.tableauInscrit.heading('IdEleve', text='IDENTIFIANT')
        self.tableauInscrit.heading('Nom', text='NOMS ET POST - NOMS')
        self.tableauInscrit.heading('Sexe', text='SEXE')

   
        self.tableauInscrit.column('Sexe',width=80,anchor='center')
        self.tableauInscrit.column('IdEleve',width=120,anchor='center')
        self.tableauInscrit.column('Nom',width=200,anchor='center')


        self.tableauInscrit.tag_configure('evenrow', background='lightblue')
        self.tableauInscrit.tag_configure('oddrow', background='lightyellow')

        dataInscrit=self.DataGlob.GetDataElevesInscrits(self.AnneeACtive[0][0],'tous')
        self.eleveFille=0
        self.eleveGarcon=0
        if len(dataInscrit)!=0:

            for i, row in enumerate(dataInscrit):
                tag='evenrow' if i%2==0 else 'oddrow'
                self.tableauInscrit.tag_configure(tag,foreground='black')
                self.tableauInscrit.insert('','end',values=(row[0],row[1],row[2]),tags=(tag,))
                if row[2]=='M':
                    self.eleveGarcon+=1
                else:
                    self.eleveFille+=1

        self.tableauInscrit.bind('<Double-Button-1>',self.ModifierInscription)
        self.tableauInscrit.pack()

        #Creation de bouton d'actualisation des eleves inscrit
        #self.ActualiserBtn=Button(self.ActionBar,bg='white',text='Actualiser',relief='groove', font=('arial',10),fg='#6666b9',command=self.ActualiserElevesInscrit(self.AnneeACtive[0][0],self.Classes[self.CodeArtEnt.get()]))
        #self.ActualiserBtn.place(x=180,y=5, width=130,height=30)

        # les statistique
        self.TotalEleveInscrit=Frame( self.EleveInscritListe,height=80,width=140,relief="groove",bg='#6666b9')
        self.TotalEleveInscrit.place(x=20,y=30)
        self.title_Tot = Label(self.TotalEleveInscrit, text = "Total", font = "Arial 12 ",bg='#6666b9',fg='white').place(x=10, y=10)
        self.Nbr_Tot = Label(self.TotalEleveInscrit, text =len(dataInscrit), font = "Arial 30 ",bg='#6666b9',fg='white').place(x=60, y=10)

        self.TotFilleInscrit=Frame( self.EleveInscritListe,height=80,width=140,relief="groove",bg='#6666b9')
        self.TotFilleInscrit.place(x=180,y=30)
        self.title_Tot = Label(self.TotFilleInscrit, text = "Filles", font = "Arial 12 ",bg='#6666b9',fg='white').place(x=10, y=10)
        self.Nbr_Tot = Label(self.TotFilleInscrit, text = self.eleveFille, font = "Arial 30 ",bg='#6666b9',fg='white').place(x=60, y=10)

        self.TotGarcInscrit=Frame( self.EleveInscritListe,height=80,width=140,relief="groove",bg='#6666b9')
        self.TotGarcInscrit.place(x=340,y=30)
        self.title_Tot = Label(self.TotGarcInscrit, text = "Garçons", font = "Arial 12 ",bg='#6666b9',fg='white').place(x=10, y=10)
        self.Nbr_Tot = Label(self.TotGarcInscrit, text = self.eleveGarcon, font = "Arial 30 ",bg='#6666b9',fg='white').place(x=80, y=10)


    #La methode pour generer le pdf de la liste des eleves d'une classe
    def getPdfListeEleve(self):
        if self.CodeArtEnt.get()!='' and self.CodeArtEnt.get()!='toutes les classes':
            result=filedialog.asksaveasfilename(defaultextension='.pdf',filetypes=[('PDF files',"*.pdf")])
            if result:
                Data=self.DataGlob.GetDataElevesInscrits(self.AnneeACtive[0][0],self.Classes[self.CodeArtEnt.get()])
                if len(Data)!=0:
                    self.DocumentPdf.getListeEleve(result,Data,self.AnneeACtive[0][1])
                    showinfo('GEST-NOTES','Enregistrement reussi')
                else:
                    showwarning('GEST-NOTES','Pas d\'Eleves inscrits pour cette classe')

        else:
            showwarning('GEST-NOTES','Veuillez choisir une classe particulière')
    def AfficherClasse(self,event):
        self. ActualiserElevesInscrit(self.AnneeACtive[0][0],self.Classes[self.CodeArtEnt.get()])
    
    #la methode d'actualisation de tous les eleves 
    def Recherche(self):
        Data = self.DataGlob.GetDataEleves()
        self.data=Data
        # suppression des elements du tableau
        for record in self.tableau.get_children():
            self.tableau.delete(record)
        if len(Data)!=0:
            for i, row in enumerate(Data):
                if self.SearchEntry.get()=='':
                    tag='evenrow' if i%2==0 else 'oddrow'
                    self.tableau.tag_configure(tag,foreground='black')
                    self.tableau.insert('','end',values=(row[0],row[1],row[2],row[3],row[4],row[5]),tags=(tag,))
                else:
                    if self.SearchEntry.get().upper() in row[1]:
                        tag='evenrow' if i%2==0 else 'oddrow'
                        self.tableau.tag_configure(tag,foreground='black')
                        self.tableau.insert('','end',values=(row[0],row[1],row[2].upper(),row[3],row[4],row[5]),tags=(tag,))
        self.tableau.pack()
    def ActualiserEleves(self):
        Data = self.DataGlob.GetDataEleves()
        self.data=Data
        # suppression des elements du tableau
        for record in self.tableau.get_children():
            self.tableau.delete(record)
        if len(Data)!=0:
            self.eleveFille=0
            self.eleveGarcon=0
            for i, row in enumerate(Data):
                tag='evenrow' if i%2==0 else 'oddrow'
                self.tableau.tag_configure(tag,foreground='black')
                self.tableau.insert('','end',values=(row[0],row[1],row[2],row[3],row[4],row[5]),tags=(tag,))
                if row[2]=='M':
                    self.eleveGarcon+=1
                else:
                    self.eleveFille+=1
        self.tableau.pack()
        #Les statistiques
        self.TotalEleve=Frame( self.ElevesListe,height=80,width=160,relief="groove",bg='lightyellow')
        self.TotalEleve.place(x=20,y=30)
        self.title_Tot = Label( self.TotalEleve, text = "Total", font = "Arial 12 ",bg='lightyellow',fg='#6666b9').place(x=10, y=10)
        self.Nbr_Tot = Label( self.TotalEleve, text = len(Data), font = "Arial 30 ",bg='lightyellow',fg='#6666b9').place(x=60, y=10)

        self.TotalGarcons=Frame( self.ElevesListe,height=80,width=160,relief="groove",bg='lightyellow')
        self.TotalGarcons.place(x=200,y=30)
        self.title_Garc= Label( self.TotalGarcons, text = "Garçons", font = "Arial 12 ",bg='lightyellow',fg='#6666b9').place(x=10, y=10)
        self.Nbr_Garc = Label( self.TotalGarcons, text =self.eleveGarcon, font = "Arial 30 ",bg='lightyellow',fg='#6666b9').place(x=80, y=10)

        self.TotalFilles=Frame( self.ElevesListe,height=80,width=160,relief="groove",bg='lightyellow')
        self.TotalFilles.place(x=380,y=30)
        self.title_Garc= Label(self.TotalFilles, text = "Filles", font = "Arial 12 ",bg='lightyellow',fg='#6666b9').place(x=10, y=10)
        self.Nbr_Garc = Label(self.TotalFilles, text =self.eleveFille, font = "Arial 30 ",bg='lightyellow',fg='#6666b9').place(x=80, y=10)

    #La methode d'actualisation des eleves inscrits
    def ActualiserElevesInscrit(self,annee,type):
        Data=self.DataGlob.GetDataElevesInscrits(annee,self.Classes[self.CodeArtEnt.get()])
        # suppression des elements du tableau
        for record in self.tableauInscrit.get_children():
            self.tableauInscrit.delete(record)
        if len(Data)!=0:
            self.eleveFille=0
            self.eleveGarcon=0
            for i, row in enumerate(Data):
                tag='evenrow' if i%2==0 else 'oddrow'
                self.tableauInscrit.tag_configure(tag,foreground='black')
                self.tableauInscrit.insert('','end',values=(row[0],row[1],row[2]),tags=(tag,))
                if row[2]=='M':
                    self.eleveGarcon+=1
                else:
                    self.eleveFille+=1
        self.tableauInscrit.pack()

        # les statistique
        self.TotalEleveInscrit=Frame( self.EleveInscritListe,height=80,width=140,relief="groove",bg='#6666b9')
        self.TotalEleveInscrit.place(x=20,y=30)
        self.title_Tot = Label(self.TotalEleveInscrit, text = "Total", font = "Arial 12 ",bg='#6666b9',fg='white').place(x=10, y=10)
        self.Nbr_Tot = Label(self.TotalEleveInscrit, text =len(Data), font = "Arial 30 ",bg='#6666b9',fg='white').place(x=60, y=10)

        self.TotFilleInscrit=Frame( self.EleveInscritListe,height=80,width=140,relief="groove",bg='#6666b9')
        self.TotFilleInscrit.place(x=180,y=30)
        self.title_Tot = Label(self.TotFilleInscrit, text = "Filles", font = "Arial 12 ",bg='#6666b9',fg='white').place(x=10, y=10)
        self.Nbr_Tot = Label(self.TotFilleInscrit, text = self.eleveFille, font = "Arial 30 ",bg='#6666b9',fg='white').place(x=60, y=10)

        self.TotGarcInscrit=Frame( self.EleveInscritListe,height=80,width=140,relief="groove",bg='#6666b9')
        self.TotGarcInscrit.place(x=340,y=30)
        self.title_Tot = Label(self.TotGarcInscrit, text = "Garçons", font = "Arial 12 ",bg='#6666b9',fg='white').place(x=10, y=10)
        self.Nbr_Tot = Label(self.TotGarcInscrit, text = self.eleveGarcon, font = "Arial 30 ",bg='#6666b9',fg='white').place(x=80, y=10)

    #La fonction d'appelle du formulaire d'ajout eleve
    def Ajouter (self):
        if self.AnneeACtive[0][0]=='None':
            showinfo("GEST-NOTES","Veuillez activer une année")
        else:
            eleve=self.FormulaireAjout(self.fen,self.ClassesSansFiltre,self.DataGlob,self.AnneeACtive[0][0],self.Classes)
            eleve.fenetre().mainloop()
    #La fonction d'appelle du formulaire de modification
    def ModifierEleve (self,event):
        row_id=self.tableau.selection()[0]
        select = self.tableau.set(row_id)
        # recuperation des valeurs de la ligne selectionner du tableau eleves
        dataTab=[select['IdEleve'],select['Nom'],select['Sexe'],select['LieuNaissance'],select['DateNaissance'],select['NumPermanent']]
        UpdateForm=self.UpdateForm(dataTab,self.DataGlob)
        UpdateForm.fenetre().mainloop()

    #La methode pour l'appel du formulaire d'inscription
    def InscrirEleve (self):
        if self.AnneeACtive[0][0]=='None':
            showinfo("GEST-NOTES","Veuillez activer une année")
        else:
            eleve=self.FormInscription(self.fen,self.data,self.ClassesSansFiltre,self.Classes,self.DataGlob,self.AnneeACtive[0][0])
            eleve.fenetre().mainloop()

     #La methode pour l'appel du formulaire de modification d'inscription
    def ModifierInscription (self,event):
        row_id=self.tableauInscrit.selection()[0]
        select = self.tableauInscrit.set(row_id)
        # recuperation des valeurs de la ligne selectionner du tableau elevesInscrits
        dataTab=[select['IdEleve'],select['Nom'],2]
        UpdateForm=self.UpdateEleveInscrit(dataTab,self.ClassesSansFiltre,self.Classes,self.DataGlob,self.AnneeACtive[0][0]) 
        UpdateForm.fenetre().mainloop()



    #la fonction de modification de donnees 
    def Update (self):
        pass
    #la fonction de suppressions
    def DeleteClient (self):
        pass
    def generate_pdf(self):
        pass

    def fenetre (self):
        return self.fen

    class FormulaireAjout:
        def __init__(self,fen,dataClasse,DataGlob,idAnnee,DataValueCombo):
            self.fen=fen
            self.fenSec = Tk()
            self.dataComboClass=dataClasse
            self.DataGlob=DataGlob
            self.ValuesCombo=DataValueCombo
            self.anneeEncours=idAnnee
            print(self.anneeEncours,'annee')
            self.fenSec.title("GESTION DES NOTES")
            self.fenSec.geometry("800x600")
            self.fenSec.resizable(width=False,height=False)
            
            # Controle de fermeture de la fenetre
            self.fenSec.protocol("WM_DELETE_WINDOW",self.Close)

            #Ajout de la forme du curseur de souris
            self.fenSec.config(cursor="arrow")

            #Creation du conteneur de l'entete de la fenetre du formulaire d'ajout
            self.HeaderContainer=Frame(self.fenSec,height=120,width=830,bg='#6666b9')
            self.HeaderContainer.place(x=0,y=0)

            #Creation de conteneur du formulaire et ses contenus
            self.form=Frame(self.fenSec,height=480,width=560,relief="groove",bg='white')
            self.form.place(x=120,y=50)

            self.TitleForm = Label(self.form, text='Informations sur élève',bg='white',font='Arial 17',fg='#6666b9')
            self.TitleForm .place(x=160,y=20, height=30)
            self.IdLab = Label(self.form, text='Identifiant',bg='white',font='20')
            self.IdLab.place(x=80,y=80, height=30)
            self.NomLab = Label(self.form, text='Noms',bg='white',font='20')
            self.NomLab.place(x=80,y=130, height=30)
            self.SexeLab = Label(self.form, text='Sexe',bg='white',font='20')
            self.SexeLab.place(x=80,y=180, height=30)
            self.LieuLab = Label(self.form, text='Lieu Naissance',bg='white',font='20')
            self.LieuLab.place(x=80,y=230, height=30)
            self.DateLab = Label(self.form, text='Date Naiss.',bg='white',font='20')
            self.DateLab.place(x=80,y=280, height=30)
            self.PermLab = Label(self.form, text='Numéro Perm.',bg='white',font='20')
            self.PermLab.place(x=80,y=330, height=30)

            
            self.IdEnt=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.IdEnt.place(x=200,y=80,width=280, height=30)
            self.NomEnt=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.NomEnt.place(x=200,y=130,width=280, height=30)
            self.SexeEnt=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.SexeEnt.place(x=200,y=180,width=280, height=30)
            self.LieuEnt=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.LieuEnt.place(x=200,y=230,width=280, height=30)
            self.DateEnt=DateEntry(self.form,bg='lightblue',relief="flat",fg='#6666b9',date_pattern='yyyy-mm-dd')
            self.DateEnt.place(x=200,y=280,width=280, height=30)
            self.PermEnt=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.PermEnt.place(x=200,y=330,width=280, height=30)
            
            self.PermLab = Label(self.form, text='Classe',bg='white',font='20')
            self.PermLab.place(x=80,y=380, height=30)
            self.Classe=ttk.Combobox(self.form,values=self.dataComboClass)
            self.Classe.place(x=200,y=380,width=280, height=30)
            self.Classe.bind("<<ComboboxSelected>>")

              

            #Les buttons d'actions sur le formulaire
            self.Save_btn= Button(self.form,bg='#6666b9',text='AJOUTER',fg='white',relief="flat", font = "Arial 12 ", command=self.ConfirmeInscription)
            self.Save_btn.place(x=80,y=430, width=180,height=40)
            self.Cancel_btn= Button(self.form,bg='white',text='ANNULER',fg='#6666b9',relief="groove", font = "Arial 12 ",command=self.Close)
            self.Cancel_btn.place(x=300,y=430, width=180,height=40)


        #Creation de l'anition
        def fade_in(frame,alpha=0):
            if alpha<1:
                alpha+=0.01 #Ajustez la vitesse de la transition a votre convenance
                frame.place_configure(relwidth=1,relheight=1)# Agrandire progressivement le Frame
                frame.attributes('-alpha',alpha)# ajuster la transparence pour un fondu 
                self.fenSec.after(10,lambda:fade_in(frame,alpha))
       
        #la Methode pour reinisialiser les champs
        def ReseteInput(self):
            self.IdEnt.delete(0,END)
            self.NomEnt.delete(0,END)
            self.SexeEnt.delete(0,END)
            self.LieuEnt.delete(0,END)
            self.DateEnt.delete(0,END)
            self.SexeEnt.delete(0,END)
            self.PermEnt.delete(0,END)
            
        #la Methode pour le bouton annuler du formulaire
        def Close (self):
            if self.IdEnt.get()=="" and self.NomEnt.get()=="" and self.Classe.get()=="" :
                self.fenSec.destroy()
            else :
                result=askyesno("Confirmation","Voulez - vous vraiment annuler l'ajout ?")
                if result :
                    self.fenSec.destroy()
        def fenetre (self):
            return self.fenSec
        
        #la methode pour ajouter les eleves dans la BD

        def AddEleve(self):
            if self.IdEnt.get()=='' or self.NomEnt.get()=='' or self.SexeEnt.get()=='' or self.LieuEnt.get()=='' or self.DateEnt.get()=='' or self.PermEnt.get()=='' :
                showinfo('GEST-NOTES','Veuillez remplir tous les champs')
            else:
                liste=[self.IdEnt.get(),self.NomEnt.get(),self.SexeEnt.get(),self.LieuEnt.get(),self.DateEnt.get(),self.PermEnt.get(),self.Classe.get(), self.anneeEncours]
                self.DataGlob.AddDataEleve(liste)
                self.form.place_forget()
                self.ComboContainer.place(x=120,y=50)
        def ConfirmeInscription(self):
                liste=[self.IdEnt.get(),self.NomEnt.get(),self.SexeEnt.get(),self.LieuEnt.get(),self.DateEnt.get(),self.PermEnt.get(), self.anneeEncours,self.ValuesCombo[self.Classe.get()]]
                print("DataListe",liste)
                self.DataGlob.InscrirEleve(liste)
                self.ReseteInput()
                self.fenSec.destroy()

    # Classe du formulaire de modification et de suppression
    class UpdateForm:
        def __init__(self,data,backend):
            self.DataInput=data
            self.fenSec = Tk()
            self.Back=backend
            self.fenSec.title("GESTION DES NOTES")
            self.fenSec.geometry("800x600")
            self.fenSec.resizable(width=False,height=False)
            
            # Controle de fermeture de la fenetre
            self.fenSec.protocol("WM_DELETE_WINDOW",self.Close)

            #Ajout de la forme du curseur de souris
            self.fenSec.config(cursor="arrow")

            #Creation du conteneur de l'entete de la fenetre du formulaire d'ajout
            self.HeaderContainer=Frame(self.fenSec,height=120,width=830,bg='#6666b9')
            self.HeaderContainer.place(x=0,y=0)
            self.titre = Label(self.HeaderContainer, text = "FORMULAIRE DE MODIFICATION DE "+self.DataInput[1], font = "Arial 15 ",bg='#6666b9',fg='white',cursor='fleur',anchor='c',width=70).place(x=10, y=15)

            #Creation de conteneur du formulaire et ses contenus
            self.form=Frame(self.fenSec,height=450,width=560,relief="groove",bg='white')
            self.form.place(x=120,y=50)


            self.NomLab = Label(self.form, text='Noms',bg='white',font='20')
            self.NomLab.place(x=80,y=50, height=30)
            self.SexeLab = Label(self.form, text='Sexe',bg='white',font='20')
            self.SexeLab.place(x=80,y=100, height=30)
            self.LieuLab = Label(self.form, text='Lieu Naissance',bg='white',font='20')
            self.LieuLab.place(x=80,y=150, height=30)
            self.DateLab = Label(self.form, text='Date Naiss.',bg='white',font='20')
            self.DateLab.place(x=80,y=200, height=30)
            self.PermLab = Label(self.form, text='Numéro Perm.',bg='white',font='20')
            self.PermLab.place(x=80,y=250, height=30)

            self.NomEnt=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.NomEnt.place(x=200,y=50,width=280, height=30)
            self.SexeEnt=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.SexeEnt.place(x=200,y=100,width=280, height=30)
            self.LieuEnt=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.LieuEnt.place(x=200,y=150,width=280, height=30)
            self.DateEnt=DateEntry(self.form,bg='lightblue',relief="flat",fg='#6666b9',date_pattern='yyyy-mm-dd')
            self.DateEnt.place(x=200,y=200,width=280, height=30)
            self.PermEnt=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.PermEnt.place(x=200,y=250,width=280, height=30)

            #Les buttons d'actions sur le formulaire
            self.Save_btn= Button(self.form,bg='#6666b9',text='MODIFIER',fg='white',relief="flat", font = "Arial 12 ",command=self.Modification)
            self.Save_btn.place(x=80,y=380, width=120,height=40)
            self.Delete_btn= Button(self.form,bg='white',text='SUPPRIMER',fg='red',relief="groove", font = "Arial 12 ",command=self.DeleteEleve)
            self.Delete_btn.place(x=220,y=380, width=120,height=40)
            self.Cancel_btn= Button(self.form,bg='white',text='ANNULER',fg='#6666b9',relief="groove", font = "Arial 12 ",command=self.Close)
            self.Cancel_btn.place(x=360,y=380, width=120,height=40)

            #Ajout des donnees dans les champs du formulaire
            self.NomEnt.insert(0,self.DataInput[1])
            self.SexeEnt.insert(0,self.DataInput[2])
            self.DateEnt.insert(0,self.DataInput[4])
            self.LieuEnt.insert(0,self.DataInput[3])
            self.PermEnt.insert(0,self.DataInput[5])
        
        #La methode de modification de l'élève

        def Modification(self):
            if self.NomEnt.get()!=self.DataInput[1] or self.SexeEnt.get()!=self.DataInput[2] or self.LieuEnt.get()!=self.DataInput[3] or self.DateEnt.get()!=self.DataInput[4] or self.PermEnt.get()!=self.DataInput[5]:
                if self.NomEnt.get()!='' or self.SexeEnt.get()!='' or self.LieuEnt.get()!='' or self.DateEnt.get()!='' or self.PermEnt.get()!='':
                    liste=[self.NomEnt.get(),self.SexeEnt.get(),self.LieuEnt.get(),self.DateEnt.get(),self.PermEnt.get(),self.DataInput[0]]
                    self.Back.UpdateData(liste)
                    self.fenSec.destroy()
            else:
                showinfo('GEST-NOTES',"Vous n'avez rien modifier")
        
        def DeleteEleve(self):
            result=askyesno("Confirmation","La supression de l'élève va occasionné la perte de toutes ses données dans votre systèmes; Voulez-vous vraiment supprimé "+ self.DataInput[1])
            if result :
                self.Back.DeleteData(self.DataInput[0])
                self.fenSec.destroy()

        #la Methode pour le bouton annuler du formulaire
        def Close (self):
            if self.NomEnt.get()!=self.DataInput[1] or self.SexeEnt.get()!=self.DataInput[2] or self.LieuEnt.get()!=self.DataInput[3] or self.DateEnt.get()!=self.DataInput[4] or self.PermEnt.get()!=self.DataInput[5]:
                result=askyesno("Confirmation","Voulez - vous vraiment annuler la modification ?")
                if result :
                    self.fenSec.destroy()
            else :
                 self.fenSec.destroy()


        def fenetre (self):
            return self.fenSec

    #Formulaire d'inscription d'eleves 
    class FormInscription:
        def __init__(self,fen,Data,DataCombo,comboValues,DataGlob,Annee):
            self.fen=fen
            self.fenSec = Tk()
            self.fenSec.title("GESTION DES NOTES")
            self.fenSec.geometry("800x600")
            self.ComboData=DataCombo
            self.ValuesCombo=comboValues
            self.AnneeEncours=Annee
            self.DataGlob=DataGlob
            self.dataTab=[]
            self.fenSec.resizable(width=False,height=False)
            
            # Controle de fermeture de la fenetre
            self.fenSec.protocol("WM_DELETE_WINDOW",self.Close)

            #Ajout de la forme du curseur de souris
            self.fenSec.config(cursor="arrow")

            #Creation du conteneur de l'entete de la fenetre du formulaire d'ajout
            self.HeaderContainer=Frame(self.fenSec,height=120,width=830,bg='#6666b9')
            self.HeaderContainer.place(x=0,y=0)
            self.titre = Label(self.HeaderContainer, text = "FORMULAIRE D'INSCRIPTION ", font = "Arial 15 bold",bg='#6666b9',fg='white',cursor='fleur').place(x=250, y=15)

            #Creation de conteneur du formulaire et ses contenus
            self.form=Frame(self.fenSec,height=200,width=560,relief="groove",bg='white')
            self.form.place(x=120,y=50)


            self.ClassLab = Label(self.form, text='Classe',bg='white',font='20')
            self.ClassLab .place(x=80,y=50, height=30)

            self.ClassEnt=ttk.Combobox(self.form,values=self.ComboData)
            self.ClassEnt.place(x=200,y=50,width=280, height=30)
            self.ClassEnt.bind("<<ComboboxSelected>>")

            #Les buttons d'actions sur le formulaire
            self.Save_btn= Button(self.form,bg='#6666b9',text='INSCRIR',fg='white',relief="flat", font = "Arial 12 ",command=self.ConfirmeInscription)
            self.Save_btn.place(x=80,y=100, width=180,height=40)
            self.Cancel_btn= Button(self.form,bg='white',text='ANNULER',fg='#6666b9',relief="groove", font = "Arial 12 ",command=self.Close)
            self.Cancel_btn.place(x=300,y=100, width=180,height=40)

            #Search section sur tous les eleves
            self.SearchBar=Frame(self.fenSec,height=50,width=500,relief="groove")
            self.SearchBar.place(x=100,y=260)
            self.SearchEntry=Entry(self.SearchBar,relief="flat")
            self.SearchEntry.place(x=0,y=10,width=350, height=30)
            self.SearchBtn=Button(self.SearchBar,bg='#6666b9',text='Rechercher',relief='flat', font=('arial',12),fg='white')
            self.SearchBtn.place(x=360,y=10, width=130,height=30)

            self.TabSectionInscrit=Frame(self.fenSec,height=350,width=520,relief="groove")
            self.TabSectionInscrit.place(x=100,y=310)
            self.tableauInscrit=ttk.Treeview(self.TabSectionInscrit, columns=('IdEleve','Nom','Sexe'), show='headings')
            self.tableauInscrit.heading('IdEleve', text='IDENTIFIANT')
            self.tableauInscrit.heading('Nom', text='NOMS ET POST - NOMS')
            self.tableauInscrit.heading('Sexe', text='SEXE')
            for i, row in enumerate(Data):
                tag='evenrow' if i%2==0 else 'oddrow'
                self.tableauInscrit.tag_configure(tag,foreground='black')
                self.tableauInscrit.insert('','end',values=(row[0],row[1],row[2]),tags=(tag,))

            self.tableauInscrit.bind('<Double-Button-1>',self.ModifierInscription)
            self.tableauInscrit.pack()

        #la Methode pour selectionner les valeurs du tableau
        def ModifierInscription (self,event):
            row_id=self.tableauInscrit.selection()[0]
            select = self.tableauInscrit.set(row_id)
            # recuperation des valeurs de la ligne selectionner du tableau elevesInscrits
            self.dataTab.append(select['IdEleve'])
            self.SelectEleve = Label(self.form,text="Inscription de "+select['Nom'], font = "Arial 13",bg='white',fg='#6666b9',cursor='fleur',width=70).place(x=10, y=10)
        
        def ConfirmeInscription(self):
            liste=[self.dataTab[0],self.ValuesCombo[self.ClassEnt.get()],  self.AnneeEncours]
            print("DataListe",liste)
            self.DataGlob.ReeInscriptionEleve(liste)

            self.fenSec.destroy()
        
        #la Methode pour le bouton annuler du formulaire
        def Close (self):
            if self.ClassEnt.get()=="":
                self.fenSec.destroy()
            else :
                result=askyesno("Confirmation","Voulez - vous vraiment annuler l'inscription ?")
                if result :
                    self.fenSec.destroy()
        def fenetre (self):
            return self.fenSec
    
    # Classe du formulaire de modification et de suppression
    class UpdateEleveInscrit:
        def __init__(self,data,DataCombo,comboValues,DataGlob,annee):
            self.DataInput=data
            self.fenSec = Tk()
            self.fenSec.title("GESTION DES NOTES")
            self.anneeEncours=annee
            self.fenSec.geometry("800x600")
            self.fenSec.resizable(width=False,height=False)
            self.ComboData=DataCombo
            self.ValuesCombo=comboValues
            self.DataGlob=DataGlob
            
            # Controle de fermeture de la fenetre
            self.fenSec.protocol("WM_DELETE_WINDOW",self.Close)

            #Ajout de la forme du curseur de souris
            self.fenSec.config(cursor="arrow")

            #Creation du conteneur de l'entete de la fenetre du formulaire d'ajout
            self.HeaderContainer=Frame(self.fenSec,height=120,width=830,bg='#6666b9')
            self.HeaderContainer.place(x=0,y=0)
            self.titre = Label(self.HeaderContainer, text = "MODIFIER LA CLASSE DE  "+self.DataInput[1], font = "Arial 13 ",bg='#6666b9',fg='white',cursor='fleur',anchor='c',width=90).place(x=10, y=15)

            #Creation de conteneur du formulaire et ses contenus
            self.form=Frame(self.fenSec,height=200,width=560,relief="groove",bg='white')
            self.form.place(x=120,y=50)

            self.IdLab = Label(self.form, text='Classe',bg='white',font='20')
            self.IdLab.place(x=80,y=50, height=30)


            option=['option1','option2','option3','option4']
            self.ClassEnt=ttk.Combobox(self.form,values=self.ComboData)
            self.ClassEnt.place(x=200,y=50,width=280, height=30)
            self.ClassEnt.bind("<<ComboboxSelected>>")

            #Les buttons d'actions sur le formulaire
            self.Save_btn= Button(self.form,bg='#6666b9',text='MODIFIER',fg='white',relief="flat", font = "Arial 12 ",command=self.ConfirmeInscription)
            self.Save_btn.place(x=80,y=120, width=180,height=40)
            self.Cancel_btn= Button(self.form,bg='white',text='ANNULER',fg='#6666b9',relief="groove", font = "Arial 12 ",command=self.Close)
            self.Cancel_btn.place(x=300,y=120, width=180,height=40)

        #la Methode pour renvoyer la fenetre du formulaire
        def ConfirmeInscription(self):
            if self.ClassEnt.get()=="":
                showinfo('GEST-NOTES',"Veuillez Choisir une classe")

            else :
                
                print("DataListe",self.ValuesCombo[self.ClassEnt.get()])
                liste=[self.DataInput[0],self.ValuesCombo[self.ClassEnt.get()], self.anneeEncours]
                self.DataGlob.UpdateDataInscrit(liste)
                self.fenSec.destroy()
        
        #la Methode pour le bouton annuler du formulaire
        def Close (self):
            if self.ClassEnt.get()=="":
                self.fenSec.destroy()
            else :
                result=askyesno("Confirmation","Voulez - vous vraiment annuler la modification ?")
                if result :
                    self.fenSec.destroy()
        def fenetre (self):
            return self.fenSec

    class InscrirElevee:
        def __init__(self,data,nom):
            self.DataInput=data
            self.fenSec = Tk()
            self.fenSec.title("GESTION DES NOTES")
            self.fenSec.geometry("800x600")
            self.fenSec.resizable(width=False,height=False)
            
            # Controle de fermeture de la fenetre
            self.fenSec.protocol("WM_DELETE_WINDOW",self.Close)

            #Ajout de la forme du curseur de souris
            self.fenSec.config(cursor="arrow")

            #Creation du conteneur de l'entete de la fenetre du formulaire d'ajout
            self.HeaderContainer=Frame(self.fenSec,height=120,width=830,bg='#6666b9')
            self.HeaderContainer.place(x=0,y=0)
            self.titre = Label(self.HeaderContainer, text = "CHOISIR LA CLASSE DE "+nom, font = "Arial 15 bold",bg='#6666b9',fg='white',cursor='fleur').place(x=250, y=15)

            #Creation de conteneur du formulaire et ses contenus
            self.form=Frame(self.fenSec,height=200,width=560,relief="groove",bg='white')
            self.form.place(x=120,y=50)

            self.IdLab = Label(self.form, text='Classe',bg='white',font='20')
            self.IdLab.place(x=80,y=50, height=30)


            option=['option1','option2','option3','option4']
            self.ClassEnt=ttk.Combobox(self.form,values=option)
            self.ClassEnt.place(x=200,y=50,width=280, height=30)
            self.ClassEnt.bind("<<ComboboxSelected>>")

            #Les buttons d'actions sur le formulaire
            self.Save_btn= Button(self.form,bg='#6666b9',text='INSCRIR',fg='white',relief="flat", font = "Arial 12 ")
            self.Save_btn.place(x=80,y=120, width=180,height=40)
            self.Cancel_btn= Button(self.form,bg='white',text='ANNULER',fg='#6666b9',relief="groove", font = "Arial 12 ",command=self.Close)
            self.Cancel_btn.place(x=300,y=120, width=180,height=40)

        #la Methode pour renvoyer la fenetre du formulaire
        
        #la Methode pour le bouton annuler du formulaire
        def Close (self):
            if self.ClassEnt.get()=="":
                self.fenSec.destroy()
            else :
                result=askyesno("Confirmation","Voulez - vous vraiment annuler la modification ?")
                if result :
                    self.fenSec.destroy()
        def fenetre (self):
            return self.fenSec



            

