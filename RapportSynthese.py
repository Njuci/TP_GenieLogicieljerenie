from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph,Image
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.pdfgen import canvas
from tkinter.messagebox import askyesno,showinfo,showwarning
import matplotlib.pyplot as plt
import io
import os

class RapportSynthese:

    def __init__(self,data,annee):
        # Données du tableau avec des fusions
        self.left=10
        self.right=10
        self.top=5
        self.bottom=10
        self.bull=[]
        self.data=data
        self.DataOrientation=[]
        self.place=[]
        self.Infoseleve=0
        self.Data=data
        self.annee=annee

        # Resultats 
        self.rP1=[]
        self.rP2=[]
        self.rP3=[]
        self.rP4=[]
        self.rE1=[]
        self.rS1=[]
        self.rS2=[]
        self.rE2=[]
        self.rF=[]
        self.globalPlace=[]

    def GenererBulletins (self):
        i=0
        # determination de place des élèves
        for Infos in (self.Data):
             #Place par eleve
            self.Infoseleve=Infos
            finAnnee=round( (((int(Infos[1][0][4])+int(Infos[1][1][4])+int(Infos[1][2][4])+
                int(Infos[1][3][4])+int(Infos[1][4][4])+int(Infos[1][5][4])+
                int(Infos[1][6][4])+int(Infos[1][7][4])+int(Infos[1][8][4])+int(Infos[1][9][4])+
                int(Infos[1][10][4])+int(Infos[1][11][4])+
                int(Infos[1][12][4])+int(Infos[1][13][4])+int(Infos[1][14][4])+int(Infos[1][15][4])+
                int(Infos[1][16][4])+int(Infos[1][17][4])+int(Infos[1][18][4])+int(Infos[1][19][4]))+
                (int(Infos[1][0][5])+int(Infos[1][1][5])+int(Infos[1][2][5])+
                int(Infos[1][3][5])+int(Infos[1][4][5])+int(Infos[1][5][5])+
                int(Infos[1][6][5])+int(Infos[1][7][5])+int(Infos[1][8][5])+int(Infos[1][9][5])+
                int(Infos[1][10][5])+int(Infos[1][11][5])+
                int(Infos[1][12][5])+int(Infos[1][13][5])+int(Infos[1][14][5])+int(Infos[1][15][5])+
                int(Infos[1][16][5])+int(Infos[1][17][5])+int(Infos[1][18][5])+int(Infos[1][19][5]))+
                (int(Infos[1][0][6])+int(Infos[1][1][6])+int(Infos[1][2][6])+
                int(Infos[1][3][6])+int(Infos[1][4][6])+int(Infos[1][5][6])+
                int(Infos[1][6][6])+int(Infos[1][7][6])+int(Infos[1][8][6])+int(Infos[1][9][6])+
                int(Infos[1][10][6])+int(Infos[1][11][6])+
                int(Infos[1][12][6])+int(Infos[1][13][6])+int(Infos[1][14][6])+int(Infos[1][15][6])+
                int(Infos[1][16][6])+int(Infos[1][17][6])+int(Infos[1][18][6])+int(Infos[1][19][6])))+

                 ((int(Infos[1][0][7])+int(Infos[1][1][7])+int(Infos[1][2][7])+
                int(Infos[1][3][7])+int(Infos[1][4][7])+int(Infos[1][5][7])+
                int(Infos[1][6][7])+int(Infos[1][7][7])+int(Infos[1][8][7])+int(Infos[1][9][7])+
                int(Infos[1][10][7])+int(Infos[1][11][7])+
                int(Infos[1][12][7])+int(Infos[1][13][7])+int(Infos[1][14][7])+int(Infos[1][15][7])+
                int(Infos[1][16][7])+int(Infos[1][17][7])+int(Infos[1][18][7])+int(Infos[1][19][7]))+

                (int(Infos[1][0][8])+int(Infos[1][1][8])+int(Infos[1][2][8])+
                int(Infos[1][3][8])+int(Infos[1][4][8])+int(Infos[1][5][8])+
                int(Infos[1][6][8])+int(Infos[1][7][8])+int(Infos[1][8][8])+int(Infos[1][9][8])+
                int(Infos[1][10][8])+int(Infos[1][11][8])+
                int(Infos[1][12][8])+int(Infos[1][13][8])+int(Infos[1][14][8])+int(Infos[1][15][8])+
                int(Infos[1][16][8])+int(Infos[1][17][8])+int(Infos[1][18][8])+int(Infos[1][19][8]))+

                (int(Infos[1][0][9])+int(Infos[1][1][9])+int(Infos[1][2][9])+
                int(Infos[1][3][9])+int(Infos[1][4][9])+int(Infos[1][5][9])+
                int(Infos[1][6][9])+int(Infos[1][7][9])+int(Infos[1][8][9])+int(Infos[1][9][9])+
                int(Infos[1][10][9])+int(Infos[1][11][9])+
                int(Infos[1][12][9])+int(Infos[1][13][9])+int(Infos[1][14][9])+int(Infos[1][15][9])+
                int(Infos[1][16][9])+int(Infos[1][17][9])+int(Infos[1][18][9])+int(Infos[1][19][9]))))*100/
                (  (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*8),1)

            #Première periode 
            P1=round(((int(Infos[1][0][4])+int(Infos[1][1][4])+int(Infos[1][2][4])+
                int(Infos[1][3][4])+int(Infos[1][4][4])+int(Infos[1][5][4])+
                int(Infos[1][6][4])+int(Infos[1][7][4])+int(Infos[1][8][4])+int(Infos[1][9][4])+
                int(Infos[1][10][4])+int(Infos[1][11][4])+
                int(Infos[1][12][4])+int(Infos[1][13][4])+int(Infos[1][14][4])+int(Infos[1][15][4])+
                int(Infos[1][16][4])+int(Infos[1][17][4])+int(Infos[1][18][4])+int(Infos[1][19][4]))*100/
                (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))),1)

            #Deuxieme periode
            P2=round((int(Infos[1][0][5])+int(Infos[1][1][5])+int(Infos[1][2][5])+
                int(Infos[1][3][5])+int(Infos[1][4][5])+int(Infos[1][5][5])+
                int(Infos[1][6][5])+int(Infos[1][7][5])+int(Infos[1][8][5])+int(Infos[1][9][5])+
                int(Infos[1][10][5])+int(Infos[1][11][5])+
                int(Infos[1][12][5])+int(Infos[1][13][5])+int(Infos[1][14][5])+int(Infos[1][15][5])+
                int(Infos[1][16][5])+int(Infos[1][17][5])+int(Infos[1][18][5])+int(Infos[1][19][5]))*100/
                (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2])),1)
            
            #PremierSemestre
            E1=round((int(Infos[1][0][6])+int(Infos[1][1][6])+int(Infos[1][2][6])+
                int(Infos[1][3][6])+int(Infos[1][4][6])+int(Infos[1][5][6])+
                int(Infos[1][6][6])+int(Infos[1][7][6])+int(Infos[1][8][6])+int(Infos[1][9][6])+
                int(Infos[1][10][6])+int(Infos[1][11][6])+
                int(Infos[1][12][6])+int(Infos[1][13][6])+int(Infos[1][14][6])+int(Infos[1][15][6])+
                int(Infos[1][16][6])+int(Infos[1][17][6])+int(Infos[1][18][6])+int(Infos[1][19][6]))*100/
                (  (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*2),1)

            # premier semestre 
            Sem1=round(((int(Infos[1][0][4])+int(Infos[1][1][4])+int(Infos[1][2][4])+
                int(Infos[1][3][4])+int(Infos[1][4][4])+int(Infos[1][5][4])+
                int(Infos[1][6][4])+int(Infos[1][7][4])+int(Infos[1][8][4])+int(Infos[1][9][4])+
                int(Infos[1][10][4])+int(Infos[1][11][4])+
                int(Infos[1][12][4])+int(Infos[1][13][4])+int(Infos[1][14][4])+int(Infos[1][15][4])+
                int(Infos[1][16][4])+int(Infos[1][17][4])+int(Infos[1][18][4])+int(Infos[1][19][4]))+
                (int(Infos[1][0][5])+int(Infos[1][1][5])+int(Infos[1][2][5])+
                int(Infos[1][3][5])+int(Infos[1][4][5])+int(Infos[1][5][5])+
                int(Infos[1][6][5])+int(Infos[1][7][5])+int(Infos[1][8][5])+int(Infos[1][9][5])+
                int(Infos[1][10][5])+int(Infos[1][11][5])+
                int(Infos[1][12][5])+int(Infos[1][13][5])+int(Infos[1][14][5])+int(Infos[1][15][5])+
                int(Infos[1][16][5])+int(Infos[1][17][5])+int(Infos[1][18][5])+int(Infos[1][19][5]))+
                (int(Infos[1][0][6])+int(Infos[1][1][6])+int(Infos[1][2][6])+
                int(Infos[1][3][6])+int(Infos[1][4][6])+int(Infos[1][5][6])+
                int(Infos[1][6][6])+int(Infos[1][7][6])+int(Infos[1][8][6])+int(Infos[1][9][6])+
                int(Infos[1][10][6])+int(Infos[1][11][6])+
                int(Infos[1][12][6])+int(Infos[1][13][6])+int(Infos[1][14][6])+int(Infos[1][15][6])+
                int(Infos[1][16][6])+int(Infos[1][17][6])+int(Infos[1][18][6])+int(Infos[1][19][6])))*100/
                (  (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*4),1) 
            
            # Deuxieme Semestre
            P3=round((int(Infos[1][0][7])+int(Infos[1][1][7])+int(Infos[1][2][7])+
                int(Infos[1][3][7])+int(Infos[1][4][7])+int(Infos[1][5][7])+
                int(Infos[1][6][7])+int(Infos[1][7][7])+int(Infos[1][8][7])+int(Infos[1][9][7])+
                int(Infos[1][10][7])+int(Infos[1][11][7])+
                int(Infos[1][12][7])+int(Infos[1][13][7])+int(Infos[1][14][7])+int(Infos[1][15][7])+
                int(Infos[1][16][7])+int(Infos[1][17][7])+int(Infos[1][18][7])+int(Infos[1][19][7]))*100/
                (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2])),1) 
                
            P4=round((int(Infos[1][0][8])+int(Infos[1][1][8])+int(Infos[1][2][8])+
                int(Infos[1][3][8])+int(Infos[1][4][8])+int(Infos[1][5][8])+
                int(Infos[1][6][8])+int(Infos[1][7][8])+int(Infos[1][8][8])+int(Infos[1][9][8])+
                int(Infos[1][10][8])+int(Infos[1][11][8])+
                int(Infos[1][12][8])+int(Infos[1][13][8])+int(Infos[1][14][8])+int(Infos[1][15][8])+
                int(Infos[1][16][8])+int(Infos[1][17][8])+int(Infos[1][18][8])+int(Infos[1][19][8]))*100/
                (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2])),1)
                
            E2=round((int(Infos[1][0][9])+int(Infos[1][1][9])+int(Infos[1][2][9])+
                int(Infos[1][3][9])+int(Infos[1][4][9])+int(Infos[1][5][9])+
                int(Infos[1][6][9])+int(Infos[1][7][9])+int(Infos[1][8][9])+int(Infos[1][9][9])+
                int(Infos[1][10][9])+int(Infos[1][11][9])+
                int(Infos[1][12][9])+int(Infos[1][13][9])+int(Infos[1][14][9])+int(Infos[1][15][9])+
                int(Infos[1][16][9])+int(Infos[1][17][9])+int(Infos[1][18][9])+int(Infos[1][19][9]))*100/
                (  (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*2),1)
                
                #Pourcentage deuxime semestre
            Sem2=round(((int(Infos[1][0][7])+int(Infos[1][1][7])+int(Infos[1][2][7])+
                int(Infos[1][3][7])+int(Infos[1][4][7])+int(Infos[1][5][7])+
                int(Infos[1][6][7])+int(Infos[1][7][7])+int(Infos[1][8][7])+int(Infos[1][9][7])+
                int(Infos[1][10][7])+int(Infos[1][11][7])+
                int(Infos[1][12][7])+int(Infos[1][13][7])+int(Infos[1][14][7])+int(Infos[1][15][7])+
                int(Infos[1][16][7])+int(Infos[1][17][7])+int(Infos[1][18][7])+int(Infos[1][19][7]))+

                (int(Infos[1][0][8])+int(Infos[1][1][8])+int(Infos[1][2][8])+
                int(Infos[1][3][8])+int(Infos[1][4][8])+int(Infos[1][5][8])+
                int(Infos[1][6][8])+int(Infos[1][7][8])+int(Infos[1][8][8])+int(Infos[1][9][8])+
                int(Infos[1][10][8])+int(Infos[1][11][8])+
                int(Infos[1][12][8])+int(Infos[1][13][8])+int(Infos[1][14][8])+int(Infos[1][15][8])+
                int(Infos[1][16][8])+int(Infos[1][17][8])+int(Infos[1][18][8])+int(Infos[1][19][8]))+

                (int(Infos[1][0][9])+int(Infos[1][1][9])+int(Infos[1][2][9])+
                int(Infos[1][3][9])+int(Infos[1][4][9])+int(Infos[1][5][9])+
                int(Infos[1][6][9])+int(Infos[1][7][9])+int(Infos[1][8][9])+int(Infos[1][9][9])+
                int(Infos[1][10][9])+int(Infos[1][11][9])+
                int(Infos[1][12][9])+int(Infos[1][13][9])+int(Infos[1][14][9])+int(Infos[1][15][9])+
                int(Infos[1][16][9])+int(Infos[1][17][9])+int(Infos[1][18][9])+int(Infos[1][19][9])))*100/
                (  (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*4),1)
            
            
            liste=[Infos[0][0][1],P1,P2,E1,Sem1,P3,P4,E2,Sem2,finAnnee,Infos[0][0][2]]
            self.rP1.append(P1)
            self.rP2.append(P2)
            self.rP3.append(P3)
            self.rP4.append(P4)
            self.rE1.append(E1)
            self.rE2.append(E2)
            self.rS1.append(Sem1)
            self.rS2.append(Sem2)
            self.rF.append(finAnnee)
            self.place.append(liste)
        
        #Arrangement selon l'ordre croissant
        self.rP1.sort(reverse=True)
        self.rP2.sort(reverse=True)
        self.rP3.sort(reverse=True)
        self.rP4.sort(reverse=True)
        self.rE1.sort(reverse=True)
        self.rE2.sort(reverse=True)
        self.rF.sort(reverse=True)
        self.rS1.sort(reverse=True)
        self.rS2.sort(reverse=True)
        #Algorithme pour trouver la place de l'eleve

        U=0
        for item in (self.place):
            p1=0
            p2=0
            E1=0
            S1=0
            p3=0
            p4=0
            E2=0
            F=0
            i=1
            for p in (self.rP1):
                if p == item[1]:
                    p1=i
                i+=1
            i=1
            for t in (self.rP2):
                if t == item[2]:
                    p2=i
                i+=1
            i=1
            for t1 in (self.rE1):
                if t1 == item[3]:
                    E1=i
                i+=1
            i=1
            for t2 in (self.rS1):
                if t2 == item[4]:
                    S1=i
                i+=1
            i=1
            for t3 in (self.rP3):
                if t3 == item[5]:
                    p3=i
                i+=1
            i=1
            for t4 in (self.rP4):
                if t4 == item[6]:
                    p4=i
                i+=1
            i=1
            for t5 in (self.rE2):
                if t5 == item[7]:
                    E2=i
                i+=1
            i=1
            for t5 in (self.rS2):
                if t5 == item[8]:
                    S2=i
                i+=1
            i=1
            for t6 in (self.rF):
                if t6 == item[9]:
                    F=i
                i+=1
            i=1
            U+=1
            liste=[item[0],item[10],p1,p2,E1,S1,p3,p4,E2,S2,F]
            self.globalPlace.append(liste)

       
    def getRapportOrientation(self,filename,dataTab1):
        if len(self.data[0][1])==20:
            self.GenererBulletins()
            doc = SimpleDocTemplate(filename, pagesize=letter)
            elements = []

            styles = ParagraphStyle(name="Centered", Parent=getSampleStyleSheet()['Heading1'], fontSize=13, alignement=1) 

            # Entête de la de la fiche 
            Data=[["COMPLEXE SCOLAIRE ESPOIR 1 "],["RAPPORT SYNTHESE DE LA  "+str(self.Infoseleve[0][0][5])+"  "+str(self.annee)]]

            L=[500]
            H=[20,30]
            Header=Table(Data,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.white)])
            style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),15),
            ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
            ('ALIGN', (0, 0), (-1,-1),'CENTER'),
            ('PADDING', (0, 0), (-1,-1),2),
            ])
            Header.setStyle(style)
            elements.append(Header)
            
            #Espace entre elements
            Data=[[""]]
            H=[10]
            TabSpace=Table(Data, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.white)])
            elements.append(TabSpace)
      
            elements.append(Paragraph("TABLEAU SYNTHESE D'EFFECTIF"))
            elements.append(TabSpace)
            #Informations sur eleves 
            fille=0
            garcon=0
            for item in (dataTab1):
                if item[0].lower()=='f':
                    fille+=1
                else:
                    garcon+=1

            Data=[["TOTAL ELEVE",'FILLES','GARCONS'],[len(dataTab1),fille,garcon]]
            L=[200,150,150]
            H=[20,20]
            Tab1=Table(Data,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
            style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),9),
            ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
            ('ALIGN', (0, 0), (-1,-1),'CENTER'),
            ('PADDING', (0, 0), (-1,-1),2),
            ])
            Tab1.setStyle(style)
            elements.append(Tab1)
            elements.append(TabSpace)

            plt.figure()
            couleurs=['#6666b9','green','purple']
            sizes=[fille,garcon]
            labels=['Fille','Garcons']
            plt.pie(sizes,labels=labels,colors=couleurs,autopct='%1.1f%%', startangle=90)
            plt.title('Effectif élèves')
            plt.axis('equal')
            plt.savefig('im1.png')
            im2='im1.png'
            elements.append(Image(im2, width=500,height=250))

            #Resultats annuels des eleves 
            elements.append(TabSpace)
            elements.append(Paragraph("TABLEAU DES RESULTATS ANNUEL"))
            elements.append(TabSpace)

            filleR=0
            garconR=0
            filleE=0
            garconE=0
            
            for it in (self.place):
               
                if it[9]>=50.0 and it[10].lower()=='f':
                    filleR+=1
                elif it[9]>=50.0 and it[10].lower()=='m':
                     garconR+=1

                if it[9]<50.0 and it[10].lower()=='f':
                    filleE+=1
                elif it[9]<50.0 and it[10].lower()=='m':
                     garconE+=1
            Data=[["TOT. REUSSITES",'TOT. ECHECS','RE. GARCONS','RE. FILLES','EC. FILLES','EC. GARCONS'],[filleR+garconR,filleE+garconE,garconR,filleR,filleE,garconE]]
            L=[80]
            H=[20,20]
            Tab1=Table(Data,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
            style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),9),
            ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
            ('ALIGN', (0, 0), (-1,-1),'CENTER'),
            ('PADDING', (0, 0), (-1,-1),2),
            ])
            Tab1.setStyle(style)
            elements.append(Tab1)
            elements.append(TabSpace)

            plt.figure()
            couleurs=['#6666b9','green','purple']
            sizes=[filleR,garconR,filleE,garconE]
            labels=['F Res','G Res','F Ech','G Ech']
            plt.pie(sizes,labels=labels,colors=couleurs,autopct='%1.1f%%', startangle=90)
            plt.title('Resultat annuel')
            plt.axis('equal')
            plt.savefig('im2.png')
            im2='im2.png'
            elements.append(Image(im2, width=500,height=250))
            
            #Tableau d'oreintation
            orientationTable=[['N°','NOMS ET POST - NOMS']]
            c=1
            orient=''
          
            
            L=[80,150]
            Orintation=Table( orientationTable,colWidths=L,style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
            style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),8),
            ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
            ('PADDING', (0, 0), (-1,-1),2),
        
            ])
            Orintation.setStyle(style)

            espace = Paragraph(" ",styles)
            elements.append(espace)

            #ajout de tableau d'orientation à la liste de rendu
        
            doc.build(elements)
            showinfo('GEST-NOTES','Enregistrement reussi')
            plt.close()
            os.remove('im1.png')
            os.remove('im2.png')
        else:
            showwarning('GEST- NOTES','Veuillez terminer la configuration des cours pour cette classe')

