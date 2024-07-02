from tkinter import *
import os
from tkinter.messagebox import askyesno,showinfo
import mysql.connector
from tkinter import ttk
from AnneeBackend import annee_Backend

from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from tkcalendar import DateEntry
import datetime


class AnneeGestFrontend: 
    def __init__(self,Curseur,fen,con,fenetre):
        self.Curseur=Curseur
        self.Connexion=con
        self.dataComboClass=[]
        self.Classes={}
        self.fen = fen
        self.menuPrincipale=fenetre
        self.idClasse=0

        #les instances de la classe
        self.DataGlob=annee_Backend(self.Curseur,self.Connexion)
        self.ver1=""
        self.ver2=""

     
        #Obtention des données depuis le backend
        self.data=self.DataGlob.GetDataAnnee()
        self.dataClasse=self.DataGlob.GetDataClassesDefaultCombo()

        #Selection de l'annee active
        self.AnneeACtive=self.DataGlob.getAnneeActive()
        if len(self.AnneeACtive)==0:
            self.AnneeACtive=[('None','None')]

        #Sections des tous les élèves 
        self.ElevesListe=Frame(self.fen,height=700,width=560,relief="groove")
        self.ElevesListe.place(x=10,y=20)

        #Formulaire de gestion de classe 
        self.form=Frame(self.ElevesListe,height=260,width=560,relief="groove",bg='white')
        self.form.place(x=5,y=20)

        self.TitleForm = Label(self.form, text='Opérations sur année',bg='white',font='Arial 15',fg='#6666b9')
        self.TitleForm .place(x=160,y=20, height=30)
        self.IdLab = Label(self.form, text='Identifiant',bg='white',font='20')
        self.IdLab.place(x=80,y=80, height=30)
        self.NomLab = Label(self.form, text='Désignation',bg='white',font='20')
        self.NomLab.place(x=80,y=130, height=30)

        self.IdEnt=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
        self.IdEnt.place(x=200,y=80,width=280, height=30)
        self.NomEnt=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
        self.NomEnt.place(x=200,y=130,width=280, height=30)

        self.Save_btn= Button(self.form,bg='#6666b9',text='AJOUTER',fg='white',relief="flat", font = "Arial 12 ",command=self.Ajouter)
        self.Save_btn.place(x=50,y=200, width=100,height=40)
        self.Update_btn= Button(self.form,bg='white',text='MODIFER',fg='#6666b9',relief="groove", font = "Arial 12 ",command=self.ModifierDomaines)
        self.Update_btn.place(x=160,y=200, width=100,height=40)
        self.active_btn= Button(self.form,bg='#6666b9',text='ACTIVER',fg='white',relief="flat", font = "Arial 12 ",command=self.ActiverAnnee)
        self.active_btn.place(x=270,y=200, width=100,height=40)
        self.delete_btn= Button(self.form,bg='red',text='SUPPRIMER',fg='white',relief="flat", font = "Arial 12 ")
        self.delete_btn.place(x=380,y=200, width=100,height=40)


        #Actions sur tous eleves 



        #Creation de tableau pour tous les élèves 
        self.TabSection=Frame( self.ElevesListe,height=350,width=520,relief="groove")
        self.TabSection.place(x=20,y=300)
        self.tableau=ttk.Treeview(self.TabSection, columns=('Identifiant','Libelle','Status'), show='headings')
        self.tableau.heading('Identifiant', text='IDENTIFIANT')
        self.tableau.heading('Libelle', text='LIBELLE')
        self.tableau.heading('Status', text='STATUS')

   
        self.tableau.column('Identifiant',width=150,anchor='center')
        self.tableau.column('Status',width=150,anchor='center')
        self.tableau.column('Libelle',width=200,anchor='center')


        self.tableau.tag_configure('evenrow', background='lightblue')
        self.tableau.tag_configure('oddrow', background='lightyellow')

        #L'qppel des donnees et affichage de donnees dans le tableau
        if len(self.data)!=0:
            for i, row in enumerate(self.data):
                tag='evenrow' if i%2==0 else 'oddrow'
                stat='OFF'
                self.tableau.tag_configure(tag,foreground='black')
                if row[2]==1 :
                    stat="ON"
                    self.tableau.insert('','end',values=(row[0],row[1],stat),tags=(tag,))
                else:
                    stat="OFF"
                    self.tableau.insert('','end',values=(row[0],row[1],stat),tags=(tag,))

        self.tableau.bind('<Double-Button-1>',self.SelectionClasseDefault)
        self.tableau.pack()

        self.EleveInscritListe=Frame(self.fen,height=700,width=500,relief="groove")
        self.EleveInscritListe.place(x=580,y=20)

       

    def AfficherClasse(self,event):
        Data=self.DataGlob.GetDataCoursClasse( self.DefaultClasss[self.CodeArtEnt.get()])
        # suppression des elements du tableau
        for record in self.tableauInscrit.get_children():
            self.tableauInscrit.delete(record)
        if len(Data)!=0:
            for i, row in enumerate(Data):
                tag='evenrow' if i%2==0 else 'oddrow'
                stat='OFF'
                self.tableau.tag_configure(tag,foreground='black')
                if row[2]==1 :
                    stat="ON"
                    self.tableau.insert('','end',values=(row[0],row[1],stat),tags=(tag,))
                else:
                    stat="OFF"
                    self.tableau.insert('','end',values=(row[0],row[1],stat),tags=(tag,))
        self.tableauInscrit.pack()
    
    #la methode d'actualisation de tous les eleves 
    def ActualiserClasseDefault(self):
        Data = self.DataGlob.GetDataAnnee()
        self.data=Data
        # suppression des elements du tableau
        for record in self.tableau.get_children():
            self.tableau.delete(record)
        if len(Data)!=0:
            for i, row in enumerate(Data):
                tag='evenrow' if i%2==0 else 'oddrow'
                stat='OFF'
                self.tableau.tag_configure(tag,foreground='black')
                if row[2]==1 :
                    stat="ON"
                    self.tableau.insert('','end',values=(row[0],row[1],stat),tags=(tag,))
                else:
                    stat="OFF"
                    self.tableau.insert('','end',values=(row[0],row[1],stat),tags=(tag,))
        self.tableau.pack()

    #La methode d'actualisation des eleves inscrits
    def ActualiserClasseParalle(self):
        Data=self.DataGlob.GetDataClasseParalle()
        # suppression des elements du tableau
        for record in self.tableauInscrit.get_children():
            self.tableauInscrit.delete(record)
        if len(Data)!=0:
            for i, row in enumerate(Data):
                tag='evenrow' if i%2==0 else 'oddrow'
                self.tableauInscrit.tag_configure(tag,foreground='black')
                self.tableauInscrit.insert('','end',values=(row[0],row[1]),tags=(tag,))
        self.tableauInscrit.pack()

    #la Méthode d'activation de l'année
    def ActiverAnnee(self):
        if self.IdEnt.get()!='' and self.NomEnt.get()!='':
            result=askyesno("Confirmation","Voulez-vous vraiment activer l'année "+self.NomEnt.get())
            if result :
                liste=[self.IdEnt.get()]
                self.DataGlob.ActiverAnnee(liste)
                self.resetInput()
                self.ActualiserClasseDefault()
                self.menuPrincipale.destroy()

        else:
            showinfo('GEST-NOTE','Veuillez remplir tout les champs')
    #La fonction d'appelle du formulaire d'ajout eleve

    def resetInput (self):
        self.IdEnt.delete(0,END)
        self.NomEnt.delete(0,END)
    def Ajouter (self):
        if self.IdEnt.get()!='' and self.NomEnt.get()!='':
            liste=[self.IdEnt.get(),self.NomEnt.get()]
            self.DataGlob.AddAnnee(liste)
            self.resetInput()
            self.ActualiserClasseDefault()

        else:
            showinfo('GEST-NOTE','Veuillez remplir tout les champs')


    #La fonction d'appelle du formulaire de modification
    def SelectionClasseDefault (self,event):
        row_id=self.tableau.selection()[0]
        select = self.tableau.set(row_id)
        # recuperation des valeurs de la ligne selectionner du tableau eleves
        dataTab=[select['Identifiant'],select['Libelle']]
        self.resetInput()
        self.IdEnt.insert(0,dataTab[0])
        self.NomEnt.insert(0,dataTab[1])
        self.idClasse=dataTab[0]
    
    def ModifierDomaines(self):
        if self.IdEnt.get()!='' and self.NomEnt.get()!='':
            liste=[self.IdEnt.get(),self.NomEnt.get(),self.idClasse]
            self.DataGlob.UpdateAnnee(liste)
            self.resetInput()
            self.ActualiserClasseDefault()
        else:
            showinfo('GEST-NOTE','Veuillez remplir tout les champs')
        

    


    # la fonction pour vider les cha;ps de formulaire de classe parallele
    def resetInputClasseParallele (self):
        self.IdEntC.delete(0,END)
        self.NomEntC.delete(0,END)
        self.ClassEnt.delete(0,END)



    