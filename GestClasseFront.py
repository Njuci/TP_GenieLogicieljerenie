from tkinter import *
import os
from tkinter.messagebox import askyesno,showinfo
import mysql.connector
from tkinter import ttk
from ClassesBackend import classe_Backend

from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from tkcalendar import DateEntry
import datetime


class ClasseGestFrontend:
    def __init__(self,Curseur,fen):
        self.Curseur=Curseur
        self.dataComboClass=[]
        self.Classes={}
        self.fen = fen
        self.idClasse=0

        #les instances de la classe
        self.DataGlob=classe_Backend(self.Curseur)
        self.ver1=""
        self.ver2=""
     

        self.data=self.DataGlob.GetDataClasseDefault()

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

        self.TitleForm = Label(self.form, text='GESTION DES CLASSES',bg='white',font='Arial 14',fg='#6666b9')
        self.TitleForm .place(x=60,y=20, height=30)
        self.IdLab = Label(self.form, text='Identifiant',bg='white',font='20')
        self.IdLab.place(x=60,y=80, height=30)
        self.NomLab = Label(self.form, text='Désignation',bg='white',font='20')
        self.NomLab.place(x=60,y=130, height=30)

        self.IdEnt=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
        self.IdEnt.place(x=180,y=80,width=280, height=30)
        self.NomEnt=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
        self.NomEnt.place(x=180,y=130,width=280, height=30)

        self.Save_btn= Button(self.form,bg='#6666b9',text='AJOUTER',fg='white',relief="flat", font = "Arial 9 ",command=self.Ajouter)
        self.Save_btn.place(x=60,y=200, width=100,height=30)
        self.Update_btn= Button(self.form,bg='white',text='MODIFER',fg='#6666b9',relief="groove", font = "Arial 9 ",command=self.ModifierDefaultClasse)
        self.Update_btn.place(x=210,y=200, width=100,height=30)
        self.delete_btn= Button(self.form,bg='red',text='SUPPRIMER',fg='white',relief="flat", font = "Arial 9 ",command=self.DeleteDefaultClasse)
        self.delete_btn.place(x=350,y=200, width=100,height=30)


        #Actions sur tous eleves 



        #Creation de tableau pour tous les élèves 
        self.TabSection=Frame( self.ElevesListe,height=350,width=520,relief="groove")
        self.TabSection.place(x=0,y=300)
        self.tableau=ttk.Treeview(self.TabSection, columns=('Identifiant','Libelle'), show='headings')
        self.tableau.heading('Identifiant', text='IDENTIFIANT')
        self.tableau.heading('Libelle', text='LIBELLE')

   
        self.tableau.column('Identifiant',width=300,anchor='center')
        self.tableau.column('Libelle',width=300,anchor='center')


        self.tableau.tag_configure('evenrow', background='lightblue')
        self.tableau.tag_configure('oddrow', background='lightyellow')

        #L'qppel des donnees et affichage de donnees dans le tableau
        if len(self.data)!=0:
            for i, row in enumerate(self.data):
                tag='evenrow' if i%2==0 else 'oddrow'
                self.tableau.tag_configure(tag,foreground='black')
                self.tableau.insert('','end',values=(row[0],row[1]),tags=(tag,))

        self.tableau.bind('<Double-Button-1>',self.SelectionClasseDefault)
        self.tableau.pack()

        #Section sur eleves Inscrits
        self.EleveInscritListe=Frame(self.fen,height=700,width=500,relief="groove")
        self.EleveInscritListe.place(x=580,y=20)

        #formulaire de gestion 
        self.form=Frame(self.EleveInscritListe,height=260,width=560,relief="groove",bg='white')
        self.form.place(x=5,y=20)
        self.TitleForm = Label(self.form, text='GESTION DES CLASSES PARALLELE',bg='white',font='Arial 14',fg='#6666b9')
        self.TitleForm .place(x=60,y=20, height=30)

        #Bouton d'actualisation de la liste de classe


        self.IdLab = Label(self.form, text='Identifiant',bg='white',font='20')
        self.IdLab.place(x=60,y=80, height=30)
        self.NomLab = Label(self.form, text='Désignation',bg='white',font='20')
        self.NomLab.place(x=60,y=120, height=30)
        self.NomLab = Label(self.form, text='Classe',bg='white',font='20')
        self.NomLab.place(x=60,y=160, height=30)

        self.IdEntC=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
        self.IdEntC.place(x=180,y=80,width=280, height=30)
        self.NomEntC=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
        self.NomEntC.place(x=180,y=120,width=280, height=30)

        data=self.data
        self.Classes["toutes les classes"]="tous"
        self.dataComboClass=[]
        if len(data)!=0:
            for i in (data):
                self.Classes[''+i[1]]=i[0]
                self.dataComboClass.append(i[1])

        self.ClassEnt=ttk.Combobox(self.form,values=self.dataComboClass)
        self.ClassEnt.place(x=180,y=160,width=280, height=30)
        self.ClassEnt.bind("<<ComboboxSelected>>",self.AfficherClasse)

        self.Save_btn= Button(self.form,bg='#6666b9',text='AJOUTER',fg='white',relief="flat", font = "Arial 9",command=self.AjouterParallele)
        self.Save_btn.place(x=90,y=200, width=100,height=30)
        self.Update_btn= Button(self.form,bg='white',text='MODIFER',fg='#6666b9',relief="groove", font = "Arial 9",command=self.ModifierParalleClasse)
        self.Update_btn.place(x=230,y=200, width=100,height=30)
        self.delete_btn= Button(self.form,bg='red',text='SUPPRIMER',fg='white',relief="flat", font = "Arial 9",command=self.DeleteClasseParallele)
        self.delete_btn.place(x=370,y=200, width=100,height=30)

     
        #Creation de tableau pour les eleves inscrits
        self.TabSectionInscrit=Frame(self.EleveInscritListe,height=350,width=520,relief="groove")
        self.TabSectionInscrit.place(x=20,y=300)
        self.tableauInscrit=ttk.Treeview(self.TabSectionInscrit, columns=('IDENTIFIANT','LIBELLE'), show='headings')
        self.tableauInscrit.heading('IDENTIFIANT', text='IDENTIFIANT')
        self.tableauInscrit.heading('LIBELLE', text='NOM CLASSE')


   
        self.tableauInscrit.column('IDENTIFIANT',width=250,anchor='center')
        self.tableauInscrit.column('LIBELLE',width=250,anchor='center')


        self.tableauInscrit.tag_configure('evenrow', background='lightblue')
        self.tableauInscrit.tag_configure('oddrow', background='lightyellow')

        dataInscrit=self.DataGlob.GetDataClasseParalle()
        if len(dataInscrit)!=0:
            for i, row in enumerate(dataInscrit):
                tag='evenrow' if i%2==0 else 'oddrow'
                self.tableauInscrit.tag_configure(tag,foreground='black')
                self.tableauInscrit.insert('','end',values=(row[0],row[1]),tags=(tag,))

        self.tableauInscrit.bind('<Double-Button-1>',self.ModifierInscription)
        self.tableauInscrit.pack()

    def AfficherClasse(self,event):
        pass
    
    #la methode d'actualisation de tous les eleves 
    def ActualiserClasseDefault(self):
        Data = self.DataGlob.GetDataClasseDefault()
        self.data=Data
        # suppression des elements du tableau
        for record in self.tableau.get_children():
            self.tableau.delete(record)
        if len(Data)!=0:
            for i, row in enumerate(Data):
                tag='evenrow' if i%2==0 else 'oddrow'
                self.tableau.tag_configure(tag,foreground='black')
                self.tableau.insert('','end',values=(row[0],row[1]),tags=(tag,))
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

    #La fonction d'appelle du formulaire d'ajout eleve

    def resetInput (self):
        self.IdEnt.delete(0,END)
        self.NomEnt.delete(0,END)
    
    #La methode pour actualiser les donnees des combobox
    def RefreshDataComboBox(self):
        #Actualisation du combobox de classe par defaut
        data=self.DataGlob.GetDataClasseDefault()
        self.Classes["toutes les classes"]="tous"
        self.dataComboClass=[]
        if len(data)!=0:
            for i in (data):
                self.Classes[''+i[1]]=i[0]
                self.dataComboClass.append(i[1])

        self.ClassEnt=ttk.Combobox(self.form,values=self.dataComboClass)
        self.ClassEnt.place(x=180,y=160,width=280, height=30)
        self.ClassEnt.bind("<<ComboboxSelected>>",self.AfficherClasse)
    def Ajouter (self):
        if self.IdEnt.get()!='' and self.NomEnt.get()!='':
            liste=[self.IdEnt.get(),self.NomEnt.get()]
            self.DataGlob.AddDefaultClasse(liste)
            self.resetInput()
            self.ActualiserClasseDefault()
            self.RefreshDataComboBox()

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
    
    def ModifierDefaultClasse(self):
        if self.IdEnt.get()!='' and self.NomEnt.get()!='':
            liste=[self.IdEnt.get(),self.NomEnt.get(),self.idClasse]
            self.DataGlob.UpdateDataClasseDefault(liste)
            self.resetInput()
            self.ActualiserClasseDefault()
            self.RefreshDataComboBox()
        else:
            showinfo('GEST-NOTE','Veuillez remplir tout les champs')
        
    def DeleteDefaultClasse(self):
        if self.IdEnt.get()!='' and self.NomEnt.get()!='':
            result=askyesno("Confirmation","La suppression de cette classe va occassioné la suppression de toutes les classes y associées et tout les élèves associé à cette classe ?")
            if result :
                liste=[self.IdEnt.get()]
                self.DataGlob.DeleteClasseClasseDefault(liste)
                self.resetInput()
                self.ActualiserClasseDefault()
                self.RefreshDataComboBox()
        else:
            showinfo('GEST-NOTE','Veuillez remplir tout les champs')
        
    


    # la fonction pour vider les cha;ps de formulaire de classe parallele
    def resetInputClasseParallele (self):
        self.IdEntC.delete(0,END)
        self.NomEntC.delete(0,END)
        self.ClassEnt.delete(0,END)

     #La methode pour remplir les champs de classes parallele
    def ModifierInscription (self,event):
        row_id=self.tableauInscrit.selection()[0]
        select = self.tableauInscrit.set(row_id)
        # recuperation des valeurs de la ligne selectionner du tableau elevesInscrits
        dataTab=[select['IDENTIFIANT'],select['LIBELLE']]
        self.resetInputClasseParallele()
        self.ver1=dataTab[0]
        self.ver2=dataTab[1]
        self.IdEntC.insert(0,dataTab[0])
        self.NomEntC.insert(0,dataTab[1])

    #la methode pour ajouter la classe parallele
    def AjouterParallele (self):
        if self.IdEntC.get()!='' and self.NomEntC.get()!='' and self.ClassEnt.get()!='':
            liste=[self.IdEntC.get(),self.NomEntC.get(),self.Classes[ self.ClassEnt.get()]]
            self.DataGlob.AddClasseParalele(liste)
            self.resetInputClasseParallele()
            self.ActualiserClasseParalle()

        else:
            showinfo('GEST-NOTE','Veuillez remplir tout les champs')

    # Methode de suppression de classe parallele
    def DeleteClasseParallele(self):
        if self.IdEntC.get()!='' :
            result=askyesno("Confirmation","La suppression de cette classe va occassioné la suppression de  tout les élèves associé à cette classe ainsi que leurs côtes?")
            if result :
                liste=[self.IdEntC.get()]
                self.DataGlob.DeleteClasseClassParallele(liste)
                self.resetInputClasseParallele()
                self.ActualiserClasseParalle()
        else:
            showinfo('GEST-NOTE','Veuillez remplir tout les champs')
    # Methode de modification de classe parallele
    def ModifierParalleClasse(self):
        if self.ver1!=self.IdEntC.get() or self.ver2!=self.NomEntC.get():
            if self.IdEntC.get()!='' and self.NomEntC.get()!='':
                liste=[self.IdEntC.get(),self.NomEntC.get()]
                self.DataGlob.UpdateDataClassParallele(liste)
                self.resetInputClasseParallele()
                self.ActualiserClasseParalle()
            else:
                showinfo('GEST-NOTE','Veuillez remplir tout les champs')
        else:
            showinfo('GEST-NOTE',"Vous n'avez rien modifier")



