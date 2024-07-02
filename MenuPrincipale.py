from tkinter import *
import os
from tkinter.messagebox import askyesno,showinfo
import mysql.connector
from tkinter import ttk


from EleveBackend import Eleve_Backend
from EleveGest_Front import EleveGestFrontend
from GestClasseFront import ClasseGestFrontend
from GesCoursFront import CoursGestFrontend
from GestNotesFront import GestNotesFrontend
from GestAnneeFront import AnneeGestFrontend
from GestEnseignantTitu import TitulaireGestFrontend


from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from tkcalendar import DateEntry
import datetime


class MenuPrincipaleFrontend:
    ver=0
    def __init__(self,Curseur,con,compte,IDTitu):
        self.Curseur=Curseur
        self.dataComboClass=[]
        self.Classes={}
        self.fen = Tk()
        self.Connexion=con
        self.IdTitulaire=IDTitu
        self.fen.title("GESTION DES NOTES")
        self.fen.geometry("800x600")
        self.compte=compte
        #les instances de la classe
        self.DataGlob=Eleve_Backend(self.Curseur,self.Connexion)
     

        self.data=self.DataGlob.GetDataEleves()

        #Selection de l'annee active
        self.AnneeACtive=self.DataGlob.getAnneeActive()
        if len(self.AnneeACtive)==0:
            self.AnneeACtive=[('None','None')]

        #Creation du conteneur de l'entete de l
        self.HeaderContainer=Frame(self.fen,height=120,width=1530,bg='#6666b9')
        self.HeaderContainer.place(x=0,y=0)
        self.titre = Label(self.HeaderContainer, text = "BIENVENUE DANS ESPOIR1 GEST-NOTES", font = "Arial 15 bold",bg='#6666b9',fg='white').place(x=450, y=15)
        self.AnneeTitle = Label(self.HeaderContainer, text =self.AnneeACtive[0][1], font = "Arial 15 bold",bg='#6666b9',fg='white').place(x=900, y=15)
        self.titre1 = Label(self.HeaderContainer, text = 'GESTION DES ELEVES', font = "Arial 14",bg='#6666b9',fg='white',width=200,anchor='w').place(x=280, y=60)


        #Creation du conteneur de menu
        self.MenuContainer=Frame(self.fen,height=700,width=250,bg='white')
        self.MenuContainer.place(x=20,y=60)

       
        #Creation des conteneurs d'ecrant
        self.GestEleve=Frame(self.fen,height=700,width=1080)
        self.GestEleve.place(x=280,y=100)
        

        self.GestClasse=Frame(self.fen,height=700,width=1080)
        self.GestClasse.place(x=280,y=100)
        self.GestClasse.place_forget()

        self.GestCours=Frame(self.fen,height=700,width=1080)
        self.GestCours.place(x=280,y=100)
        self.GestCours.place_forget()

        self.GestNotes=Frame(self.fen,height=700,width=1080)
        self.GestNotes.place(x=280,y=100)
        self.GestNotes.place_forget()
       

        self.GestAnnee=Frame(self.fen,height=700,width=1080)
        self.GestAnnee.place(x=280,y=100)
        self.GestAnnee.place_forget()

        self.GestInfos=Frame(self.fen,height=700,width=1080)
        self.GestInfos.place(x=280,y=100)
        self.GestInfos.place_forget()

        Menu1=EleveGestFrontend(self.Curseur,self.GestEleve,self.Connexion)
        Menu2=ClasseGestFrontend(self.Curseur,self.GestClasse)
        Menu3=CoursGestFrontend(self.Curseur,self.GestCours,self.Connexion)
        Menu4=GestNotesFrontend(self.Curseur,self.GestNotes,self.compte,self.IdTitulaire,self.Connexion)
        Menu5=AnneeGestFrontend(self.Curseur,self.GestAnnee,self.Connexion,self.fen)
        Menu6=TitulaireGestFrontend(self.Curseur,self.GestInfos)
        
        self.title_menu = Label( self.MenuContainer, text = " NAVIGATIONS", font = "Arial 12 bold",bg='#6666b9',fg='white').place(x=60, y=20)
        self.GestEleve_btn= Button(self.MenuContainer,bg='white',text='Gestion Elèves',fg='#6666b9',relief="groove", font = "Arial 12 ",command=self.AfficherSlide1)
        self.GestEleve_btn.place(x=20,y=80, width=200,height=40)
        self.GestClasse_btn= Button(self.MenuContainer,bg='white',text='Gestion Classes',fg='#6666b9',relief="groove", font = "Arial 12 ",command=self.AfficherSlide2)
        self.GestClasse_btn.place(x=20,y=140, width=200,height=40)
        self.GestCours_btn= Button(self.MenuContainer,bg='white',text='Gestion Cours',fg='#6666b9',relief="groove", font = "Arial 12 ",command=self.AfficherSlide3)
        self.GestCours_btn.place(x=20,y=200, width=200,height=40)
        self.GestNotes_btn= Button(self.MenuContainer,bg='white',text='Gestion Notes',fg='#6666b9',relief="groove", font = "Arial 12 ",command=self.AfficherSlide4)
        self.GestNotes_btn.place(x=20,y=260, width=200,height=40)
        self.GestAnnee_btn= Button(self.MenuContainer,bg='white',text='Gestion Années',fg='#6666b9',relief="groove", font = "Arial 12 ",command=self.AfficherSlide5)
        self.GestAnnee_btn.place(x=20,y=320, width=200,height=40)
        self.GestInfos_btn= Button(self.MenuContainer,bg='white',text='Gestion Titulaires',fg='#6666b9',relief="groove", font = "Arial 12 ",command=self.AfficherSlide6)
        self.GestInfos_btn.place(x=20,y=380, width=200,height=40)
        self.Exit_btn= Button(self.MenuContainer,bg='white',text='Déconnexion',fg='#6666b9',relief="groove", font = "Arial 12 ")
        self.Exit_btn.place(x=20,y=440, width=200,height=40)
        self.ver=0

        #self.ComboContainer.place_forget()

    def cacherSlide(self):
        self.GestEleve.place_forget()
        self.GestClasse.place_forget()
        self.GestCours.place_forget()
        self.GestNotes.place_forget()
        self.GestAnnee.place_forget()
        self.GestInfos.place_forget()

    def AfficherSlide1(self):
        self.titre1 = Label(self.HeaderContainer, text = 'GESTION DES ELEVES', font = "Arial 14",bg='#6666b9',fg='white',width=200,anchor='w').place(x=280, y=60)
        self.cacherSlide()
        self.GestEleve.place(x=280,y=100)

    def AfficherSlide2(self):
        self.titre1 = Label(self.HeaderContainer, text = 'GESTION DES CLASSES', font = "Arial 14",bg='#6666b9',fg='white',width=200,anchor='w').place(x=280, y=60)
        self.cacherSlide()
        self.GestClasse.place(x=280,y=100)

    def AfficherSlide3(self):
        self.titre1 = Label(self.HeaderContainer, text = 'GESTION DES COURS', font = "Arial 14",bg='#6666b9',fg='white',width=200,anchor='w').place(x=280, y=60)
        self.cacherSlide()
        self.GestCours.place(x=280,y=100)
    
    def AfficherSlide4(self):
        self.titre1 = Label(self.HeaderContainer, text = 'GESTION DES NOTES', font = "Arial 14",bg='#6666b9',fg='white',width=200,anchor='w').place(x=280, y=60)
        self.cacherSlide()
        self.GestNotes.place(x=280,y=100)
    
    def AfficherSlide5(self):
        self.titre1 = Label(self.HeaderContainer, text = 'GESTION DES ANNEES', font = "Arial 14",bg='#6666b9',fg='white',width=200,anchor='w').place(x=280, y=60)
        self.cacherSlide()
        self.GestAnnee.place(x=280,y=100)

    def AfficherSlide6(self):
        self.titre1 = Label(self.HeaderContainer, text = "GESTION ENSEIGNANT TITULAIRE", font = "Arial 14",bg='#6666b9',fg='white',width=200,anchor='w').place(x=280, y=60)
        self.cacherSlide()
        self.GestInfos.place(x=280,y=100)

    def fenetre (self):
        return self.fen

        

       