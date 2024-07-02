from tkinter import *
import os
from tkinter.messagebox import askyesno,showinfo
import mysql.connector
from tkinter import ttk
from CoursBackend import cours_Backend

from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from tkcalendar import DateEntry
import datetime


class CoursGestFrontend: 
    def __init__(self,Curseur,fen,connexion):
        self.Curseur=Curseur
        self.connexion=connexion
        self.dataComboClass=[]
        self.Classes={}
        self.fen = fen
        self.idClasse=0

        #les instances de la classe
        self.DataGlob=cours_Backend(self.Curseur,self.connexion)
        self.ver1=""
        self.ver2=""

     

        self.data=self.DataGlob.GetDataDomaines()
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

        self.TitleForm = Label(self.form, text='GESTION DES DOMAINES',bg='white',font='Arial 14',fg='#6666b9')
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
        self.Update_btn= Button(self.form,bg='white',text='MODIFER',fg='#6666b9',relief="groove", font = "Arial 9 ",command=self.ModifierDomaines)
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



        self.EleveInscritListe=Frame(self.fen,height=700,width=500,relief="groove")
        self.EleveInscritListe.place(x=580,y=20)

        #formulaire de gestion 
        self.DefaultClasss={}
        data=self.dataClasse
        self.dataComboClassDefault=[]
        if len(data)!=0:
            for i in (data):
                self.DefaultClasss[''+i[1]]=i[0]
                self.dataComboClassDefault.append(i[1])

        self.TitleForm = Label(self.EleveInscritListe, text='GESTION DES COURS',font='Arial 14',fg='#6666b9').place(x=0, y=10)
        self.Classe_label = Label(  self.EleveInscritListe, text = "Classe :", font = "Arial 12 ").place(x=0, y=80)
        self.CodeArtEnt=ttk.Combobox(  self.EleveInscritListe,values=self.dataComboClassDefault)
        self.CodeArtEnt.place(x=100,y=80,width=200, height=30)
        self.CodeArtEnt.bind("<<ComboboxSelected>>",self.AfficherClasse)
        self.CodeArtEnt.current(0)

        self.InscrirBtn=Button(self.EleveInscritListe,bg='#6666b9',text='AJOUTER',relief='flat', font=('arial',9),fg='white',command=self.AjoutCours )
        self.InscrirBtn.place(x=330,y=80, width=130,height=30)


        #choix Classe
        self.ClasseFilterSection=Frame( self.EleveInscritListe,height=50,width=500,relief="groove")
        self.ClasseFilterSection.place(x=20,y=160)



     
        #Creation de tableau pour les eleves inscrits
        self.TabSectionInscrit=Frame(self.EleveInscritListe,height=200,width=520,relief="groove")
        self.TabSectionInscrit.place(x=10,y=120)
        self.tableauInscrit=ttk.Treeview(self.TabSectionInscrit, columns=('IDENTIFIANT','LIBELLE','maxP','maxEx'), show='headings')
        self.tableauInscrit.heading('IDENTIFIANT', text='IDENTIFIANT')
        self.tableauInscrit.heading('LIBELLE', text='NOM CLASSE')
        self.tableauInscrit.heading('maxP', text='MAX PERIODE')
        self.tableauInscrit.heading('maxEx', text='MAX EXAMEN')
        self.tableauInscrit.configure(height=20)


   
        self.tableauInscrit.column('IDENTIFIANT',width=80,anchor='center')
        self.tableauInscrit.column('LIBELLE',width=150,anchor='center')
        self.tableauInscrit.column('maxP',width=110,anchor='center')
        self.tableauInscrit.column('maxEx',width=110,anchor='center')


        self.tableauInscrit.tag_configure('evenrow', background='lightblue')
        self.tableauInscrit.tag_configure('oddrow', background='lightyellow')

        dataInscrit=self.DataGlob.GetDataCoursClasse( self.DefaultClasss[self.CodeArtEnt.get()])
        if len(dataInscrit)!=0:
            for i, row in enumerate(dataInscrit):
                tag='evenrow' if i%2==0 else 'oddrow'
                self.tableauInscrit.tag_configure(tag,foreground='black')
                self.tableauInscrit.insert('','end',values=(row[0],row[1],row[2],row[3]),tags=(tag,))

        self.tableauInscrit.bind('<Double-Button-1>',self.UpdateCours)
        self.tableauInscrit.pack()

    def AfficherClasse(self,event):
        Data=self.DataGlob.GetDataCoursClasse( self.DefaultClasss[self.CodeArtEnt.get()])
        # suppression des elements du tableau
        for record in self.tableauInscrit.get_children():
            self.tableauInscrit.delete(record)
        if len(Data)!=0:
            for i, row in enumerate(Data):
                tag='evenrow' if i%2==0 else 'oddrow'
                self.tableauInscrit.tag_configure(tag,foreground='black')
                self.tableauInscrit.insert('','end',values=(row[0],row[1],row[2],row[3]),tags=(tag,))
        self.tableauInscrit.pack()
    
    #la methode d'actualisation de tous les eleves 
    def ActualiserClasseDefault(self):
        Data = self.DataGlob.GetDataDomaines()
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
    def Ajouter (self):
        if self.IdEnt.get()!='' and self.NomEnt.get()!='':
            liste=[self.IdEnt.get(),self.NomEnt.get()]
            self.DataGlob.AddDomain(liste)
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
            self.DataGlob.UpdateDomaines(liste)
            self.resetInput()
            self.ActualiserClasseDefault()
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
    def ModifierDefaultClasse(self):
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
    def AjoutCours (self):

        AjoutCours=self.AjoutCoursForm(self.DataGlob,self.DefaultClasss[self.CodeArtEnt.get()], self.data)
        AjoutCours.fenetre().mainloop()

    def UpdateCours(self,event):
        row_id=self.tableauInscrit.selection()[0]
        select =self.tableauInscrit.set(row_id)
        # recuperation des valeurs de la ligne selectionner du tableau elevesInscrits
        dataTab=[select['IDENTIFIANT'],select['LIBELLE'],select['maxP'],select['maxEx']]
        Data=[dataTab[0],dataTab[1],dataTab[2],dataTab[3]]
        AjoutCours=self.UpdateCoursForm(self.DataGlob,self.dataClasse, self.data,Data)
        AjoutCours.fenetre().mainloop()

    class AjoutCoursForm:
        def __init__(self,backend,dataClasse,datadomaine):
            self.fenSec = Tk()
            self.fenSec.title("GESTION DES NOTES")
            self.Backend=backend
            self.fenSec.geometry("800x600")
            self.fenSec.resizable(width=False,height=False)
            self.idClassse=dataClasse

            # Controle de fermeture de la fenetre
            self.fenSec.protocol("WM_DELETE_WINDOW",self.Close)

            #Ajout de la forme du curseur de souris
            self.fenSec.config(cursor="arrow")

                    #Section sur eleves Inscrits
            data=datadomaine
            self.DomaineFiltre={}
            self.dataComboDomaine=[]
            if len(data)!=0:
                for i in (data):
                    self.DomaineFiltre[''+i[1]]=i[0]
                    self.dataComboDomaine.append(i[1])



            #Creation du conteneur de l'entete de la fenetre du formulaire d'ajout
            self.HeaderContainer=Frame(self.fenSec,height=120,width=830,bg='#6666b9')
            self.HeaderContainer.place(x=0,y=0)
            self.titre = Label(self.HeaderContainer, text = "FORMULAIRE D'AJOUT D'UN COURS", font = "Arial 15 ",bg='#6666b9',fg='white',cursor='fleur',anchor='c',width=70).place(x=10, y=15)

            #Creation de conteneur du formulaire et ses contenus
            self.form=Frame(self.fenSec,height=450,width=560,relief="groove",bg='white')
            self.form.place(x=120,y=50)

            self.IdLab = Label(self.form, text='Identifiant',bg='white',font='20')
            self.IdLab.place(x=80,y=80, height=30)
            self.NomLab = Label(self.form, text='Désignation',bg='white',font='20')
            self.NomLab.place(x=80,y=120, height=30)
            self.NomLab = Label(self.form, text='Domaine',bg='white',font='20')
            self.NomLab.place(x=80,y=160, height=30)

            self.NomLab = Label(self.form, text='Max Période',bg='white',font='20')
            self.NomLab.place(x=80,y=200, height=30)
            self.NomLab = Label(self.form, text='Max Examen',bg='white',font='20')
            self.NomLab.place(x=80,y=240, height=30)

            self.IdEntC=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.IdEntC.place(x=200,y=80,width=280, height=30)
            self.NomEntC=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.NomEntC.place(x=200,y=120,width=280, height=30)

            self.DomaineEnt=ttk.Combobox(self.form,values= self.dataComboDomaine)
            self.DomaineEnt.place(x=200,y=160,width=280, height=30)

            self.MaxPeriode=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.MaxPeriode.place(x=200,y=200,width=280, height=30)

            self.MaxExamen=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.MaxExamen.place(x=200,y=240,width=280, height=30)


            self.Save_btn= Button(self.form,bg='#6666b9',text='AJOUTER',fg='white',relief="flat", font = "Arial 12 ",command=self.AjoutClasse)
            self.Save_btn.place(x=90,y=340, width=100,height=40)
            self.Update_btn= Button(self.form,bg='white',text='ANNULER',fg='#6666b9',relief="groove", font = "Arial 12 ", command=self.Close)
            self.Update_btn.place(x=230,y=340, width=100,height=40)
        def Close (self):
            if self.MaxExamen.get()=='' and self.MaxPeriode.get()=='' and self.IdEntC.get()=='' and self.NomEntC.get()=='' and self.idClassse=='' and self.DomaineEnt.get()=='':
                self.fenSec.destroy()
            else:
                result=askyesno("Confirmation","Voulez - vous vraiment annuler l'ajout ?")
                if result :
                    self.fenSec.destroy()
        def AjoutClasse(self):
            if self.MaxExamen.get()=='' or self.MaxPeriode.get()=='' or self.IdEntC.get()=='' or self.NomEntC.get()=='' or  self.idClassse=='' or self.DomaineEnt.get()=='':
                showinfo('GEST-NOTES','Veuillez remplir tout les champs')
            else:
                liste=[self.IdEntC.get(),self.NomEntC.get(),self.MaxPeriode.get(), self.MaxExamen.get(),self.idClassse,self.DomaineFiltre[self.DomaineEnt.get()]]
                self.Backend.AddCours(liste)
                self.fenSec.destroy()


        def fenetre (self):
            return self.fenSec

    class UpdateCoursForm:
        def __init__(self,backend,dataClasse,datadomaine,Data):
            self.fenSec = Tk()
            self.fenSec.title("GESTION DES NOTES")
            self.Backend=backend
            self.fenSec.geometry("800x600")
            self.fenSec.resizable(width=False,height=False)
            self.Identifiant=0
            
            # Controle de fermeture de la fenetre
            self.fenSec.protocol("WM_DELETE_WINDOW",self.Close)

            #Ajout de la forme du curseur de souris
            self.fenSec.config(cursor="arrow")

                    #Section sur eleves Inscrits
            data=datadomaine
            self.DomaineFiltre={}
            self.dataComboDomaine=[]
            if len(data)!=0:
                for i in (data):
                    self.DomaineFiltre[''+i[1]]=i[0]
                    self.dataComboDomaine.append(i[1])

            #initialisation du combobox
            self.DefaultClasss={}
            data=dataClasse
            self.dataComboClassDefault=[]
            if len(data)!=0:
                for i in (data):
                    self.DefaultClasss[''+i[1]]=i[0]
                    self.dataComboClassDefault.append(i[1])

            #Creation du conteneur de l'entete de la fenetre du formulaire d'ajout
            self.HeaderContainer=Frame(self.fenSec,height=120,width=830,bg='#6666b9')
            self.HeaderContainer.place(x=0,y=0)
            self.titre = Label(self.HeaderContainer, text = "FORMULAIRE DE MODIFICATION", font = "Arial 15 ",bg='#6666b9',fg='white',cursor='fleur',anchor='c',width=70).place(x=10, y=15)

            #Creation de conteneur du formulaire et ses contenus
            self.form=Frame(self.fenSec,height=450,width=560,relief="groove",bg='white')
            self.form.place(x=120,y=50)

            self.IdLab = Label(self.form, text='Identifiant',bg='white',font='20')
            self.IdLab.place(x=80,y=80, height=30)
            self.NomLab = Label(self.form, text='Désignation',bg='white',font='20')
            self.NomLab.place(x=80,y=120, height=30)
            self.NomLab = Label(self.form, text='Classe',bg='white',font='20')
            self.NomLab.place(x=80,y=160, height=30)
            self.NomLab = Label(self.form, text='Domaine',bg='white',font='20')
            self.NomLab.place(x=80,y=200, height=30)

            self.NomLab = Label(self.form, text='Max Période',bg='white',font='20')
            self.NomLab.place(x=80,y=240, height=30)
            self.NomLab = Label(self.form, text='Max Examen',bg='white',font='20')
            self.NomLab.place(x=80,y=280, height=30)

            self.IdEntC=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.IdEntC.place(x=200,y=80,width=280, height=30)
            self.NomEntC=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.NomEntC.place(x=200,y=120,width=280, height=30)

            self.ClassEnt=ttk.Combobox(self.form,values=self.dataComboClassDefault)
            self.ClassEnt.place(x=200,y=160,width=280, height=30)
            self.ClassEnt.bind("<<ComboboxSelected>>")

            self.DomaineEnt=ttk.Combobox(self.form,values= self.dataComboDomaine)
            self.DomaineEnt.place(x=200,y=200,width=280, height=30)

            self.MaxPeriode=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.MaxPeriode.place(x=200,y=240,width=280, height=30)

            self.MaxExamen=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
            self.MaxExamen.place(x=200,y=280,width=280, height=30)

            self.IdEntC.insert(0,Data[0])
            self.Identifiant=Data[0]
            self.NomEntC.insert(0,Data[1])
            self.MaxPeriode.insert(0,Data[2])
            self.MaxExamen.insert(0,Data[3])


            self.Save_btn= Button(self.form,bg='#6666b9',text='MODIFIER',fg='white',relief="flat", font = "Arial 12 ",command=self.AjoutClasse)
            self.Save_btn.place(x=90,y=340, width=100,height=40)
            self.Sup_btn= Button(self.form,bg='red',text='Supprimer',fg='white',relief="flat", font = "Arial 12 ",command=self.SuppressionCours)
            self.Sup_btn.place(x=230,y=340, width=100,height=40)
            self.Update_btn= Button(self.form,bg='white',text='ANNULER',fg='#6666b9',relief="groove", font = "Arial 12 ", command=self.Close)
            self.Update_btn.place(x=370,y=340, width=100,height=40)
        def Close (self):
            if self.MaxExamen.get()=='' and self.MaxPeriode.get()=='' and self.IdEntC.get()=='' and self.NomEntC.get()=='' and self.ClassEnt.get()=='' and self.DomaineEnt.get()=='':
                self.fenSec.destroy()
            else:
                result=askyesno("Confirmation","Voulez - vous vraiment annuler l'ajout ?")
                if result :
                    self.fenSec.destroy()
        def AjoutClasse(self):
            if self.MaxExamen.get()=='' or self.MaxPeriode.get()=='' or self.IdEntC.get()=='' or self.NomEntC.get()=='' or self.ClassEnt.get()=='' or self.DomaineEnt.get()=='':
                showinfo('GEST-NOTES','Veuillez remplir tout les champs')
            else:
                if self.Identifiant==self.IdEntC.get():
                    liste=[self.IdEntC.get(),self.NomEntC.get(),self.MaxPeriode.get(), self.MaxExamen.get(), self.DefaultClasss[self.ClassEnt.get()],self.DomaineFiltre[self.DomaineEnt.get()]]
                    self.Backend.UpdateCours(liste)
                    self.fenSec.destroy()
                else:
                      showinfo('GEST-NOTES','Vous n\'allez modifer l\'identifiant')
        def SuppressionCours(self):
            if self.MaxExamen.get()=='' or self.MaxPeriode.get()=='' or self.IdEntC.get()=='' or self.NomEntC.get()=='':
                showinfo('GEST-NOTES','Veuillez remplir tout les champs')
            else:
                if self.Identifiant==self.IdEntC.get():
                    liste=[self.IdEntC.get()]
                    self.Backend.DeleteCours(liste)
                    self.fenSec.destroy()
                else:
                      showinfo('GEST-NOTES','Vous n\'allez modifer l\'identifiant')

        def fenetre (self):
            return self.fenSec




