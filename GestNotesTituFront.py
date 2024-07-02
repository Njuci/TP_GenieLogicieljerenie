from tkinter import *
import os
from tkinter.messagebox import askyesno,showinfo,showwarning
import mysql.connector
from tkinter import filedialog
from tkinter import ttk
from NoteBackend import note_Backend
from BullModel import Bulletin

from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from reportlab.platypus import Paragraph

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from tkcalendar import DateEntry
import datetime

class GestNotesFrontend2: 
    def __init__(self,Curseur,fen,compte,IdTit,nom,connexion):
        self.Curseur=Curseur
        self.dataComboCours=[]
        self.nom=nom
        self.CoursData={}
        self.compte=compte
        self.EleveIdentifiant={}
        self.fen = fen
        self.idClasse=0
        self.IdTitulaire=IdTit
        self.connexion=connexion
        self.EleveActif=''

        #les instances de la classe
        self.DataGlob=note_Backend(self.Curseur,self.compte,self.IdTitulaire,self.connexion)
        self.ver1=""
        self.ver2=""


        
        self.data=self.DataGlob.GetDataDomaines()

        #Selection de l'annee active
        self.AnneeACtive=self.DataGlob.getAnneeActive()
        if len(self.AnneeACtive)==0:
            self.AnneeACtive=[('None','None')]

        self.dataClasse=self.DataGlob.GetDataClassesDefaultCombo(self.AnneeACtive[0][0])
        


        self.EleveInscritListe=Frame(self.fen,height=700,width=730,relief="groove")
        self.EleveInscritListe.place(x=20,y=20)

        #formulaire de gestion 
        self.DefaultClasss={}
        data=self.dataClasse
        self.dataComboClassDefault=[]
        if len(data)!=0:
            for i in (data):
                self.DefaultClasss[''+i[1]]=i[0]
                self.dataComboClassDefault.append(i[1])

        self.Classe_label = Label( self.EleveInscritListe, text = "Classe :", font = "Arial 12 ").place(x=0, y=20)
        self.CodeArtEnt=ttk.Combobox(  self.EleveInscritListe,values=self.dataComboClassDefault)
        self.CodeArtEnt.place(x=100,y=20,width=200, height=30)
        self.CodeArtEnt.bind("<<ComboboxSelected>>",self.AfficherClasse)
        self.CodeArtEnt.current(0)

        self.Classe_label = Label( self.EleveInscritListe, text = "Cours :", font = "Arial 12 ").place(x=0, y=60)
        self.Cours=ttk.Combobox(  self.EleveInscritListe,values= self.dataComboCours)
        self.Cours.place(x=100,y=60,width=200, height=30)
        self.Cours.bind("<<ComboboxSelected>>",self.AfficherPointsCours)
     

        self.SearchBar=Frame(self.EleveInscritListe,height=50,width=500,relief="groove")
        self.SearchBar.place(x=10,y=90)
        self.SearchEntry=Entry(self.SearchBar,relief="flat")
        self.SearchEntry.place(x=0,y=10,width=350, height=30)
        self.SearchBtn=Button(self.SearchBar,bg='#6666b9',text='Rechercher',relief='flat', font=('arial',9),fg='white',command=self.SearchInfos)
        self.SearchBtn.place(x=360,y=10, width=130,height=30)
        self.pdffile=Button(self.EleveInscritListe,bg='red',text='PDF BULL',relief='flat', font=('arial',9),fg='white',command=self.GenererBulletins)
        self.pdffile.place(x=520,y=100, width=90,height=30)

        self.pdffileCote=Button(self.EleveInscritListe,bg='red',text='PDF Fiche',relief='flat', font=('arial',9),fg='white',command=self.GenererFiche)
        self.pdffileCote.place(x=620,y=100, width=90,height=30)

        #choix Classe
        self.ClasseFilterSection=Frame( self.EleveInscritListe,height=50,width=500,relief="groove")
        self.ClasseFilterSection.place(x=20,y=260)



     
        #Creation de tableau pour les eleves inscrits
        self.TabSectionInscrit=Frame(self.EleveInscritListe,height=200,width=600,relief="groove")
        self.TabSectionInscrit.place(x=10,y=140)
        self.tableauInscrit=ttk.Treeview(self.TabSectionInscrit, columns=('num','nom','p1','p2','ex1','ts1','p3','p4','ex2','ts2','tg'), show='headings')
        self.tableauInscrit.heading('num', text='N°')
        self.tableauInscrit.heading('nom', text='NOM & POSTNOM')
        self.tableauInscrit.heading('p1', text='1e P')
        self.tableauInscrit.heading('p2', text='2e P')
        self.tableauInscrit.heading('ex1', text='EX.')
        self.tableauInscrit.heading('ts1', text='T.S.')
        self.tableauInscrit.heading('p3', text='3e P')
        self.tableauInscrit.heading('p4', text='4e P')
        self.tableauInscrit.heading('ex2', text='EX.')
        self.tableauInscrit.heading('ts2', text='T.S.')
        self.tableauInscrit.heading('tg', text='T.G.')


   
        self.tableauInscrit.column('p1',width=50,anchor='center')
        self.tableauInscrit.column('p2',width=50,anchor='center')
        self.tableauInscrit.column('p3',width=50,anchor='center')
        self.tableauInscrit.column('p4',width=50,anchor='center')

        self.tableauInscrit.column('num',width=50,anchor='center')
        self.tableauInscrit.column('ts1',width=50,anchor='center')
        self.tableauInscrit.column('ts2',width=50,anchor='center')
        self.tableauInscrit.column('ex1',width=50,anchor='center')
        self.tableauInscrit.column('ex2',width=50,anchor='center')
        self.tableauInscrit.column('tg',width=50,anchor='center')


        self.tableauInscrit.tag_configure('evenrow', background='lightblue')
        self.tableauInscrit.tag_configure('oddrow', background='lightyellow')
        self.tableauInscrit.configure(height=20)

        self.tableauInscrit.bind('<Double-Button-1>',self.SelectionClasseDefault)
        self.tableauInscrit.pack()

        # Creation du formulaire de cotation des élèves
        self.CotationSection=Frame(self.fen,height=700,width=560,relief="groove")
        self.CotationSection.place(x=750,y=20)
                #formulaire de gestion 
        self.form=Frame(self.CotationSection,height=560,width=300,relief="groove",bg='white')
        self.form.place(x=15,y=5)
        self.TitleForm = Label(self.form, text='FORMULAIRE DE COTATION',bg='white',font='Arial 12',fg='#6666b9')
        self.TitleForm .place(x=30,y=20, height=30)


        self.TitleForm = Label(self.form, text='PREMIER SEMESTRE',bg='white',font='Arial 10',fg='gray')
        self.TitleForm .place(x=30,y=80, height=30)
        self.IdLab = Label(self.form, text='Période 1',bg='white',font='15')
        self.IdLab.place(x=40,y=120, height=30)
        self.NomLab = Label(self.form, text='Période 2',bg='white',font='15')
        self.NomLab.place(x=40,y=160, height=30)
        self.NomLab = Label(self.form, text='Examen',bg='white',font='15')
        self.NomLab.place(x=40,y=200, height=30)

        self.P1=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
        self.P1.place(x=130,y=120,width=80, height=30)
        self.P2=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
        self.P2.place(x=130,y=160,width=80, height=30)
        self.E1=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
        self.E1.place(x=130,y=200,width=80, height=30)



        self.TitleForm = Label(self.form, text='SECOND SEMESTRE',bg='white',font='Arial 10',fg='gray')
        self.TitleForm .place(x=30,y=260, height=30)

        self.IdLab = Label(self.form, text='Période 3',bg='white',font='15')
        self.IdLab.place(x=40,y=300, height=30)
        self.NomLab = Label(self.form, text='Période 4',bg='white',font='15')
        self.NomLab.place(x=40,y=340, height=30)
        self.NomLab = Label(self.form, text='Examen',bg='white',font='15')
        self.NomLab.place(x=40,y=380, height=30)

        self.P3=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
        self.P3.place(x=130,y=300,width=80, height=30)
        self.P4=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
        self.P4.place(x=130,y=340,width=80, height=30)
        self.E2=Entry(self.form,bg='lightblue',relief="flat",fg='#6666b9')
        self.E2.place(x=130,y=380,width=80, height=30)

        self.Save_btn= Button(self.form,bg='#6666b9',text='ENREGISTRER',fg='white',relief="flat", font = "Arial 13 ", command=self.Ajouter)
        self.Save_btn.place(x=40,y=450, width=200,height=40)
        
    def GenererBulletins(self):
        result=filedialog.asksaveasfilename(defaultextension='.pdf',filetypes=[('PDF files',"*.pdf")])
        if result:
            liste=[self.AnneeACtive[0][0],self.DefaultClasss[self.CodeArtEnt.get()]]
            self.DataBulletins=self.DataGlob.getDataInfosBulletins(liste)
            if len(self.DataBulletins)!=0:
                bull=Bulletin(self.DataBulletins,self.AnneeACtive[0][1])
                bull.getBulletinPDF(result)

    def GenererFiche(self):
        if self.Cours.get()!='':
            liste=[self.AnneeACtive[0][0],self.DefaultClasss[self.CodeArtEnt.get()],self.CoursData[self.Cours.get()]]
            Data=self.DataGlob.GetDataEleveCote(liste)
            listeData=[self.Cours.get(),self.nom, Data]
            result=filedialog.asksaveasfilename(defaultextension='.pdf',filetypes=[('PDF files',"*.pdf")])
            if result:
                liste=[self.AnneeACtive[0][0],self.DefaultClasss[self.CodeArtEnt.get()]]
                self.DataBulletins=self.DataGlob.getDataInfosBulletins(liste)
                if len(self.DataBulletins)!=0:
                    bull=Bulletin(self.DataBulletins,self.AnneeACtive[0][1])
                    bull.getFicheCote(result,listeData)
                    showinfo('GEST-NOTES','Enregistrement reussi')

        else:
            showwarning("GEST - NOTES",'Veuillez selctionné un cours')
    def resetInput (self):
        self.P1.delete(0,END)
        self.P2.delete(0,END)
        self.P3.delete(0,END)
        self.P4.delete(0,END)
        self.E1.delete(0,END)
        self.E2.delete(0,END)

    def SelectionClasseDefault (self,event):
        row_id=self.tableauInscrit.selection()
        select = self.tableauInscrit.set(row_id)
        # recuperation des valeurs de la ligne selectionner du tableau eleves
        self.TitleForm = Label(self.form, text=select['nom'],bg='white',font='Arial 12',fg='gray')
        self.TitleForm .place(x=30,y=50, height=30,width=280)
        dataTab=[select['p1'],select['p2'],select['p3'],select['p4'],select['ex1'],select['ex2']]
        self.resetInput()
        self.P1.insert(0,dataTab[0])
        self.P2.insert(0,dataTab[1])
        self.P3.insert(0,dataTab[2])
        self.P4.insert(0,dataTab[3])
        self.E1.insert(0,dataTab[4])
        self.E2.insert(0,dataTab[5])
        self.EleveActif=select['nom']


 
    def AfficherClasse(self,event):
        Data=self.DataGlob.GetDataCoursClasse( self.DefaultClasss[self.CodeArtEnt.get()])
        Data1 = self.DataGlob.GetCours(self.DefaultClasss[self.CodeArtEnt.get()])
        self.CoursData={}
        self.dataComboCours=[]
        if len( Data1)!=0:
            for i in (Data1):
                self.CoursData[''+i[2]]=i[1]
                self.dataComboCours.append(i[2])

        self.Classe_label = Label( self.EleveInscritListe, text = "Cours :", font = "Arial 12 ").place(x=0, y=60)
        self.Cours=ttk.Combobox(  self.EleveInscritListe,values=self.dataComboCours)
        self.Cours.place(x=100,y=60,width=200, height=30)
        self.Cours.bind("<<ComboboxSelected>>",self.AfficherPointsCours)

    def AfficherPointsCours(self,event):
        self.ActualiserPoint()
    def ActualiserPoint(self):
        liste=[self.AnneeACtive[0][0],self.DefaultClasss[self.CodeArtEnt.get()],self.CoursData[self.Cours.get()]]
        Data=self.DataGlob.GetDataEleveCote(liste)

        Data1 = self.DataGlob.GetMaxCours(self.DefaultClasss[self.CodeArtEnt.get()],self.CoursData[self.Cours.get()])
        tot1=0
        tot2=0
        for record in self.tableauInscrit.get_children():
            self.tableauInscrit.delete(record)
        if len(Data)!=0:
            for i, row in enumerate(Data):
                tag='evenrow' if i%2==0 else 'oddrow'
                liste=[]
                for a in row:
                    if a==None:
                        liste.append(0)
                    else:
                        liste.append(a)

                ('num','nom','p1','p2','ex1','ts1','p3','p4','ex2','ts2','tg')
                self.EleveIdentifiant[''+row[1]]=row[0]
                self.tableauInscrit.tag_configure(tag,foreground='black')
                tot1=liste[2]+liste[3]+liste[6]
                tot2=liste[4]+liste[5]+liste[7]
                self.tableauInscrit.insert('','end',values=(i+1,liste[1],liste[2],liste[3],liste[6],tot1,liste[4],liste[5],liste[7],tot2,tot1+tot2),tags=(tag,))
        self.tableauInscrit.pack()

        self.Per = Label(self.form, text='/'+Data1[0][0],bg='white',font='11',fg='gray')
        self.Per .place(x=210,y=120, height=30)
        self.Per = Label(self.form, text='/'+Data1[0][0],bg='white',font='11',fg='gray')
        self.Per .place(x=210,y=160, height=30)
        self.Ex11 = Label(self.form, text='/'+Data1[0][1],bg='white',font='11',fg='gray')
        self.Ex11.place(x=210,y=200, height=30)
        self.Per = Label(self.form, text='/'+Data1[0][0],bg='white',font='11',fg='gray')
        self.Per .place(x=210,y=300, height=30)
        self.Per = Label(self.form, text='/'+Data1[0][0],bg='white',font='11',fg='gray')
        self.Per .place(x=210,y=340, height=30)
        self.Ex11 = Label(self.form, text='/'+Data1[0][1],bg='white',font='11',fg='gray')
        self.Ex11.place(x=210,y=380, height=30)

    def SearchInfos(self):

        liste=[self.AnneeACtive[0][0],self.DefaultClasss[self.CodeArtEnt.get()],self.CoursData[self.Cours.get()]]
        Data=self.DataGlob.GetDataEleveCote(liste)
        # suppression des elements du tableau
        tot1=0
        tot2=0
        for record in self.tableauInscrit.get_children():
            self.tableauInscrit.delete(record)
        if len(Data)!=0:
            if self.SearchEntry.get()=="":
                for i, row in enumerate(Data):
                    tag='evenrow' if i%2==0 else 'oddrow'
                    liste=[]
                    for a in row:
                        if a==None:
                            liste.append(0)
                        else:
                            liste.append(a)
                    ('num','nom','p1','p2','ex1','ts1','p3','p4','ex2','ts2','tg')
                    self.EleveIdentifiant[''+row[1]]=row[0]
                    self.tableauInscrit.tag_configure(tag,foreground='black')
                    tot1=liste[2]+liste[3]+liste[6]
                    tot2=liste[4]+liste[5]+liste[7]
                    self.tableauInscrit.insert('','end',values=(i+1,liste[1],liste[2],liste[3],liste[6],tot1,liste[4],liste[5],liste[7],tot2,tot1+tot2),tags=(tag,))
            else :
                 for i, row in enumerate(Data):
                    tag='evenrow' if i%2==0 else 'oddrow'
                    liste=[]
                    for a in row:
                        if a==None:
                            liste.append(0)
                        else:
                            liste.append(a)
                    if self.SearchEntry.get().upper() in row[1]:
                        ('num','nom','p1','p2','ex1','ts1','p3','p4','ex2','ts2','tg')
                        self.EleveIdentifiant[''+row[1]]=row[0]
                        self.tableauInscrit.tag_configure(tag,foreground='black')
                        tot1=liste[2]+liste[3]+liste[6]
                        tot2=liste[4]+liste[5]+liste[7]
                        self.tableauInscrit.insert('','end',values=(i+1,liste[1],liste[2],liste[3],liste[6],tot1,liste[4],liste[5],liste[7],tot2,tot1+tot2),tags=(tag,))

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

    def Ajouter (self):
        chaine='0123456789'
        Data1 = self.DataGlob.GetMaxCours(self.DefaultClasss[self.CodeArtEnt.get()],self.CoursData[self.Cours.get()])
        if self.P1.get()=="" or self.P2.get()=='' or self.P3.get()=='' or self.P4.get()=='' or self.E1.get()=='' or self.E2.get()=='':
            showwarning("GEST-NOTES","Veuillez remplir tout les champs")
        else:
            if self.P1.get().isdigit() and self.P2.get().isdigit() and self.P3.get().isdigit() and self.P4.get().isdigit() and self.E1.get().isdigit() and self.E2.get().isdigit() :
                if int(self.P1.get()) <= int(Data1[0][0])  and int(self.P2.get()) <= int(Data1[0][0]) and int(self.P3.get()) <= int(Data1[0][0]) and int(self.P4.get()) <= int(Data1[0][0]) and int(self.E1.get()) <=  int(Data1[0][1]) and int(self.E2.get()) <=  int(Data1[0][1]):
                    print (6 <= 2)
                    eleve=[int(self.P1.get()),self.P2.get(),self.P3.get(),self.P4.get(),self.E1.get(),self.E2.get(),self.EleveIdentifiant[self.EleveActif],self.AnneeACtive[0][0],self.DefaultClasss[self.CodeArtEnt.get()],self.CoursData[self.Cours.get()]]
                    self.DataGlob.AddNotes(eleve)
                    self.resetInput()
                    self.ActualiserPoint()
                else :
                    showwarning("GEST-NOTES","Vous avez depasser le maxima dans un champs")
            else :
                g= self.P1.get()
                
                showwarning("GEST-NOTES","Vueillez entré des valeurs numériques")
            

 