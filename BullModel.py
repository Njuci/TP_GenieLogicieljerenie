from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph,Image
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.pdfgen import canvas
from tkinter.messagebox import askyesno,showinfo,showwarning
class Bulletin:

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
        self.Classe=''

    def GenererBulletins (self):
        i=0
        # determination de place des élèves
        for Infos in (self.Data):
             #Place par eleve
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
            
            
            liste=[Infos[0][0][1],P1,P2,E1,Sem1,P3,P4,E2,Sem2,finAnnee]
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
            liste=[item[0],p1,p2,E1,S1,p3,p4,E2,S2,F]
            self.globalPlace.append(liste)

        for Infos in (self.Data):
            place=[]
            for it in (self.globalPlace):
                if it[0]==Infos[0][0][1]:
                    place=it
                    break
            self.Infoseleve=Infos
            #Entete du bulletins 
            compteur=1
            imgPath="téléchargement.png"
            imgPath1="arm.PNG"
            Data=[[[Image(imgPath, width=80,height=40)],'REPUBLIQUE DEMOCRATIQUE DU CONGO \n MINISTERE DE L\'ENSEIGNEMENT PRIMAIRE, SECONDAIRE ET TECHNIQUE',[Image(imgPath1, width=60,height=40)],]]
            L=[120,350,120,]
            H=[70]
            Entete=Table(Data,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.white)])
            style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),10),
            ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
            ('ALIGN', (0, 0), (-1,-1),'CENTER'),

            ])
            Entete.setStyle(style)



            # N° code section
            EcoleInfo=[['N° ID','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',]]
            L=[60,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15]
            H=[12]
            NumId=Table(EcoleInfo,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
            style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),9),
            ('VALIGN', (0, 0), (0,0),'MIDDLE'),

            ])
            NumId.setStyle(style)
            #Code Ecole creation des cases 
            EcoleInfo=[[7,'-',6,3,0,0,7,5]]
            L=[20,20,20,20,20,20,20,20]
            H=[11]
            CodeEco=Table(EcoleInfo,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
            style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),9),
            ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),

            ])
            CodeEco.setStyle(style)
            #Informations sur ecole 

            EcoleInfo=[['VILLE :','BUKAVU'],['COMMUNE :','IBANDA'],['ECOLE :','C.S ESPOIR 1'],['CODE :',CodeEco]]
            L=[70,180,65,160]
            H=[12,12,12,15]
            EcoInfoTable=Table(EcoleInfo,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.white)])
            style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),8),
            ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
            ('PADDING', (0, 0), (-1,-1),2),
            ])
            EcoInfoTable.setStyle(style)



            #NumeroPermanent
            Num=[['', '','', '','', '','','','','','', '','', '','', '']]
            L=[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]
            H=[11]
            NumPerm=Table(Num,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
            style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),9),
            ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),

            ])
            NumPerm.setStyle(style)

            #Informations sur élève 
            date=Infos[0][0][4].strftime('%d-%m-%Y')
            EleveInfo=[['ELEVE :',Infos[0][0][1],"SEXE :"+Infos[0][0][2]],['NE(E) A :',Infos[0][0][3],date],['CLASSE :',Infos[0][0][5]],['N° PERM :',NumPerm]]
            L=[60,150,100,200]
            H=[12,12,12,15]
            EleveInfoTable=Table(EleveInfo,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.white)])
            style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),8),
            ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
            ('PADDING', (0, 0), (-1,-1),2),
            ('SPAN', (1, 3), (2,3)),
            ('SPAN', (1, 2), (2,2)),
            ])
            EleveInfoTable.setStyle(style)
            self.Classe=Infos[0][0][5]


            #Ligne amnee scolaire

            Data=[['BULLETIN DE LA 8e ANNEE CYCLE TERMINAL DE L\'EDUCATION DE BASE (CTEB) :','ANNEE SCOLAIRE '+ self.annee]]
            L=[440,150]
            H=[15]
            AnneeTable=Table(Data,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.white)])
            style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),9),
            ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
            ('PADDING', (0, 0), (-1,-1),2),
            ])
            AnneeTable.setStyle(style)

            #Informations de pied de page
            ligne1='L\'élève ne pourra passer dans la classe supérieur s\'il n\'a subi avec succès un examen de repêchage en................................................................\n.................................................................................................................................................................................................................................(1)\n- L\'élève passe dans la classe supérieur (1)\n- L\'élève double la classe (1)'
            Data=[['','',''],['Signature de l\'élève ','Sceau de l\'école','Fait à.........................le......./....../20....\n Le chef d\'Etablissement       Nom et Signature'],['(1) Biffer la mention inutile \nNote importante: Le bulletin est sans valeur s\'il est raturé ou surchargé.','','']]
            Data[0][0]=ligne1
            L=[200,190,195]
            H=[50,20,25]
            PiedTable=Table(Data,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.white)])
            style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),9),
            ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
            ('PADDING', (0, 0), (-1,-1),2),
            ('SPAN', (0, 0), (2,0)),
            ('SPAN', (0, 2), (2,2)),
            ])
            PiedTable.setStyle(style)
            #Information générale du bulletin
            data = [
                [Entete,'', '','', '','', '','','','','','', '','', '','', '','','',''],
                [NumId,'', '','', '','', '','','','','','', '','', '','', '','','',''],
                ['PROVINCE : SUD-KIVU','', '','', '','', '','','','','','', '','', '','', '','','',''],
                [EcoInfoTable, '','', '','', '','','',EleveInfoTable,'','', '','', '','', '','','',''],
                [AnneeTable,'', '','', '','', '','','','','','', '','', '','', '','','',''],
                ['BRANCHE','PREMIER SEMESTRE', '','', '','', '','','SECOND SEMESTRE','','','', '','', '','TOTAL\nGENERAL', '','','EXAMEN DE\n REPECHAGE',''],
                ['','MAX', 'TRAV.\n JOUR.','', 'EXAMEN','', 'TOTAL','','MAX','TRAV.\n JOUR.','','EXAMEN', '','TOTAL', '','', '','','',''],
                ['','', '','', '','', '','','','','','', '','', '','', '','','',''],
                ['','', 'P1','P2', '','', '','','','P3','P4','', '','', '','', '','','%','Sign.Prof'],
                ['DOMAINE DES SCIENCES','', '','', '','', '','','','','','', '','', '','', '','','',''],
                [Infos[1][0][0],'', '','', '','', '','','','','','', '','', '','', '','','',''],
                [Infos[1][0][1],int(Infos[1][0][2]),Infos[1][0][4],Infos[1][0][5], Infos[1][0][3],Infos[1][0][6],int(Infos[1][0][2])*4,Infos[1][0][4]+Infos[1][0][5]+Infos[1][0][6],Infos[1][0][2],Infos[1][0][7],Infos[1][0][8],Infos[1][0][3],Infos[1][0][9],int(Infos[1][0][2])*4,Infos[1][0][7]+Infos[1][0][8]+Infos[1][0][9],int(Infos[1][0][2])*8,Infos[1][0][4]+Infos[1][0][5]+Infos[1][0][6]+Infos[1][0][7]+Infos[1][0][8]+Infos[1][0][9],'','',''],
                [Infos[1][1][1],int(Infos[1][1][2]),Infos[1][1][4],Infos[1][1][5], Infos[1][1][3],Infos[1][1][6],int(Infos[1][1][2])*4,Infos[1][1][4]+Infos[1][1][5]+Infos[1][1][6],Infos[1][1][2],Infos[1][1][7],Infos[1][1][8],Infos[1][1][3],Infos[1][1][9], int(Infos[1][1][2])*4, Infos[1][1][7]+Infos[1][1][8]+Infos[1][1][9],int(Infos[1][1][2])*8,Infos[1][1][4]+Infos[1][1][5]+Infos[1][1][6]+Infos[1][1][7]+Infos[1][1][8]+Infos[1][1][9],'','',''],
                [Infos[1][2][1],int(Infos[1][2][2]),Infos[1][2][4],Infos[1][2][5], Infos[1][2][3],Infos[1][2][6],int(Infos[1][2][2])*4,Infos[1][2][4]+Infos[1][2][5]+Infos[1][2][6],Infos[1][2][2],Infos[1][2][7],Infos[1][2][8],Infos[1][2][3],Infos[1][2][9],int(Infos[1][2][2])*4,Infos[1][2][7]+Infos[1][2][8]+Infos[1][2][9],int(Infos[1][2][2])*8, Infos[1][2][4]+Infos[1][2][5]+Infos[1][2][6]+Infos[1][2][7]+Infos[1][2][8]+Infos[1][2][9],'','',''],
                [Infos[1][3][1],int(Infos[1][3][2]),Infos[1][3][4],Infos[1][2][5], Infos[1][3][3],Infos[1][3][6],int(Infos[1][3][2])*4,Infos[1][3][4]+Infos[1][3][5]+Infos[1][3][6],Infos[1][3][2],Infos[1][3][7],Infos[1][3][8],Infos[1][3][3],Infos[1][3][9],int(Infos[1][3][2])*4, Infos[1][3][7]+Infos[1][3][8]+Infos[1][3][9],int(Infos[1][3][2])*8, Infos[1][3][4]+Infos[1][3][5]+Infos[1][3][6]+Infos[1][3][7]+Infos[1][3][8]+Infos[1][3][9],'','',''],
                ['Sous Total',int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+int(Infos[1][3][2]),
                int(Infos[1][0][4])+int(Infos[1][1][4])+int(Infos[1][2][4])+int(Infos[1][3][4]),
                int(Infos[1][0][5])+int(Infos[1][1][5])+int(Infos[1][2][5])+int(Infos[1][3][5]),
                int(Infos[1][0][3])+int(Infos[1][1][3])+int(Infos[1][2][3])+int(Infos[1][3][3]),
                int(Infos[1][0][6])+int(Infos[1][1][6])+int(Infos[1][2][6])+int(Infos[1][3][6]),
                int(Infos[1][0][2])*4+int(Infos[1][1][2])*4+int(Infos[1][2][2])*4+int(Infos[1][3][2])*4,
                Infos[1][0][4]+Infos[1][0][5]+Infos[1][0][6]+Infos[1][1][4]+Infos[1][1][5]+Infos[1][1][6]+Infos[1][2][4]+Infos[1][2][5]+Infos[1][2][6]+Infos[1][3][4]+Infos[1][3][5]+Infos[1][3][6],
                int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+int(Infos[1][3][2]),
                int(Infos[1][0][7])+int(Infos[1][1][7])+int(Infos[1][2][7])+int(Infos[1][3][7]),
                int(Infos[1][0][8])+int(Infos[1][1][8])+int(Infos[1][2][8])+int(Infos[1][3][8]),
                int(Infos[1][0][3])+int(Infos[1][1][3])+int(Infos[1][2][3])+int(Infos[1][3][3]),
                int(Infos[1][0][9])+int(Infos[1][1][9])+int(Infos[1][2][9])+int(Infos[1][3][9]),
                int(Infos[1][0][2])*4+int(Infos[1][1][2])*4+int(Infos[1][2][2])*4+int(Infos[1][3][2])*4,
                Infos[1][0][7]+Infos[1][0][8]+Infos[1][0][9]+Infos[1][1][7]+Infos[1][1][8]+Infos[1][1][9]+Infos[1][2][7]+Infos[1][2][8]+Infos[1][2][9]+Infos[1][3][7]+Infos[1][3][8]+Infos[1][3][9],
                int(Infos[1][0][2])*8+int(Infos[1][1][2])*8+int(Infos[1][2][2])*8+int(Infos[1][3][2])*8,
                Infos[1][0][4]+Infos[1][0][5]+Infos[1][0][6]+Infos[1][0][7]+Infos[1][0][8]+Infos[1][0][9]+Infos[1][1][4]+Infos[1][1][5]+Infos[1][1][6]+Infos[1][1][7]+Infos[1][1][8]+Infos[1][1][9]+ Infos[1][2][4]+Infos[1][2][5]+Infos[1][2][6]+Infos[1][2][7]+Infos[1][2][8]+Infos[1][2][9]+Infos[1][3][4]+Infos[1][3][5]+Infos[1][3][6]+Infos[1][3][7]+Infos[1][3][8]+Infos[1][3][9],'','',''],
                
                ['Sous domaine des sciences de la vie et de la terre','', '','', '','', '','','','','','', '','', '','', '','','',''],
                [Infos[1][4][1],int(Infos[1][4][2]),Infos[1][4][4],Infos[1][4][5], Infos[1][4][3],Infos[1][4][6],int(Infos[1][4][2])*4,Infos[1][4][4]+Infos[1][4][5]+Infos[1][4][6],Infos[1][4][2],Infos[1][4][7],Infos[1][4][8],Infos[1][4][3],Infos[1][4][9], int(Infos[1][4][2])*4, Infos[1][4][7]+Infos[1][4][8]+Infos[1][4][9],int(Infos[1][4][2])*8,Infos[1][4][4]+Infos[1][4][5]+Infos[1][4][6]+Infos[1][4][7]+Infos[1][4][8]+Infos[1][4][9],'','',''],
                [Infos[1][5][1],int(Infos[1][5][2]),Infos[1][5][4],Infos[1][5][5], Infos[1][5][3],Infos[1][5][6],int(Infos[1][5][2])*4,Infos[1][5][4]+Infos[1][5][5]+Infos[1][5][6],Infos[1][5][2],Infos[1][5][7],Infos[1][5][8],Infos[1][5][3],Infos[1][5][9],int(Infos[1][5][2])*4,Infos[1][5][7]+Infos[1][5][8]+Infos[1][5][9],int(Infos[1][5][2])*8, Infos[1][5][4]+Infos[1][5][5]+Infos[1][5][6]+Infos[1][5][7]+Infos[1][5][8]+Infos[1][5][9],'','',''],
                [Infos[1][6][1],int(Infos[1][6][2]),Infos[1][6][4],Infos[1][6][5], Infos[1][6][3],Infos[1][6][6],int(Infos[1][6][2])*4,Infos[1][6][4]+Infos[1][6][5]+Infos[1][6][6],Infos[1][6][2],Infos[1][6][7],Infos[1][6][8],Infos[1][6][3],Infos[1][6][9],int(Infos[1][6][2])*4, Infos[1][6][7]+Infos[1][6][8]+Infos[1][6][9],int(Infos[1][6][2])*8, Infos[1][6][4]+Infos[1][6][5]+Infos[1][6][6]+Infos[1][6][7]+Infos[1][6][8]+Infos[1][6][9],'','',''],
                ['Sous Total',int(Infos[1][4][2])+int(Infos[1][5][2])+int(Infos[1][6][2]),
                int(Infos[1][4][4])+int(Infos[1][5][4])+int(Infos[1][6][4]),
                int(Infos[1][4][5])+int(Infos[1][5][5])+int(Infos[1][6][5]),
                int(Infos[1][4][3])+int(Infos[1][5][3])+int(Infos[1][6][3]),
                int(Infos[1][4][6])+int(Infos[1][5][6])+int(Infos[1][6][6]),
                int(Infos[1][4][2])*4+int(Infos[1][5][2])*4+int(Infos[1][6][2])*4,
                Infos[1][4][4]+Infos[1][4][5]+Infos[1][4][6]+Infos[1][5][4]+Infos[1][5][5]+Infos[1][5][6]+Infos[1][6][4]+Infos[1][6][5]+Infos[1][6][6],
                int(Infos[1][4][2])+int(Infos[1][5][2])+int(Infos[1][6][2]),
                int(Infos[1][4][7])+int(Infos[1][5][7])+int(Infos[1][6][7]),
                int(Infos[1][4][8])+int(Infos[1][5][8])+int(Infos[1][6][8]),
                int(Infos[1][4][3])+int(Infos[1][5][3])+int(Infos[1][6][3]),
                int(Infos[1][4][9])+int(Infos[1][5][9])+int(Infos[1][6][9]),
                int(Infos[1][4][2])*4+int(Infos[1][5][2])*4+int(Infos[1][6][2])*4,
                Infos[1][4][7]+Infos[1][4][8]+Infos[1][4][9]+Infos[1][5][7]+Infos[1][5][8]+Infos[1][5][9]+Infos[1][6][7]+Infos[1][6][8]+Infos[1][6][9],
                int(Infos[1][4][2])*8+int(Infos[1][5][2])*8+int(Infos[1][6][2])*8,
                Infos[1][4][4]+Infos[1][4][5]+Infos[1][4][6]+Infos[1][4][7]+Infos[1][4][8]+Infos[1][4][9]+ Infos[1][5][4]+Infos[1][5][5]+Infos[1][5][6]+Infos[1][5][7]+Infos[1][5][8]+Infos[1][5][9]+Infos[1][6][4]+Infos[1][6][5]+Infos[1][6][6]+Infos[1][6][7]+Infos[1][6][8]+Infos[1][6][9],'','',''],
                
                ['Sous domaines des Sciences Physique, Technologie et TIC','', '','', '','', '','','','','','', '','', '','', '','','',''],
                [Infos[1][7][1],int(Infos[1][7][2]),Infos[1][7][4],Infos[1][7][5], Infos[1][7][3],Infos[1][7][6],int(Infos[1][7][2])*4,Infos[1][7][4]+Infos[1][7][5]+Infos[1][7][6],Infos[1][7][2],Infos[1][7][7],Infos[1][7][8],Infos[1][7][3],Infos[1][7][9],int(Infos[1][7][2])*4,Infos[1][7][7]+Infos[1][7][8]+Infos[1][7][9],int(Infos[1][7][2])*8,Infos[1][7][4]+Infos[1][7][5]+Infos[1][7][6]+Infos[1][7][7]+Infos[1][7][8]+Infos[1][7][9],'','',''],
                [Infos[1][8][1],int(Infos[1][8][2]),Infos[1][8][4],Infos[1][8][5], Infos[1][8][3],Infos[1][8][6],int(Infos[1][8][2])*4,Infos[1][8][4]+Infos[1][8][5]+Infos[1][8][6],Infos[1][8][2],Infos[1][8][7],Infos[1][8][8],Infos[1][8][3],Infos[1][8][9],int(Infos[1][8][2])*4,Infos[1][8][7]+Infos[1][8][8]+Infos[1][8][9],int(Infos[1][8][2])*8,Infos[1][8][4]+Infos[1][8][5]+Infos[1][8][6]+Infos[1][8][7]+Infos[1][8][8]+Infos[1][8][9],'','',''],
                [Infos[1][9][1],int(Infos[1][9][2]),Infos[1][9][4],Infos[1][9][5], Infos[1][9][3],Infos[1][9][6],int(Infos[1][9][2])*4,Infos[1][9][4]+Infos[1][9][5]+Infos[1][9][6],Infos[1][9][2],Infos[1][9][7],Infos[1][9][8],Infos[1][9][3],Infos[1][9][9],int(Infos[1][9][2])*4, Infos[1][9][7]+Infos[1][9][8]+Infos[1][9][9],int(Infos[1][9][2])*8,Infos[1][9][4]+Infos[1][9][5]+Infos[1][9][6]+Infos[1][9][7]+Infos[1][9][8]+Infos[1][9][9],'','',''],
                ['Sous Total',int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2]),
                int(Infos[1][7][4])+int(Infos[1][8][4])+int(Infos[1][9][4]),
                int(Infos[1][7][5])+int(Infos[1][8][5])+int(Infos[1][9][5]),
                int(Infos[1][7][3])+int(Infos[1][8][3])+int(Infos[1][9][3]),
                int(Infos[1][7][6])+int(Infos[1][8][6])+int(Infos[1][9][6]),
                int(Infos[1][7][2])*4+int(Infos[1][8][2])*4+int(Infos[1][9][2])*4,
                Infos[1][7][4]+Infos[1][7][5]+Infos[1][7][6]+Infos[1][8][4]+Infos[1][8][5]+Infos[1][8][6]+Infos[1][9][4]+Infos[1][9][5]+Infos[1][9][6],
                int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2]),
                int(Infos[1][7][7])+int(Infos[1][8][7])+int(Infos[1][9][7]),
                int(Infos[1][7][8])+int(Infos[1][8][8])+int(Infos[1][9][8]),
                int(Infos[1][7][3])+int(Infos[1][8][3])+int(Infos[1][9][3]),
                int(Infos[1][7][9])+int(Infos[1][8][9])+int(Infos[1][9][9]),
                int(Infos[1][7][2])*4+int(Infos[1][8][2])*4+int(Infos[1][9][2])*4,
                Infos[1][7][7]+Infos[1][7][8]+Infos[1][7][9]+Infos[1][8][7]+Infos[1][8][8]+Infos[1][8][9]+Infos[1][9][7]+Infos[1][9][8]+Infos[1][9][9],
                int(Infos[1][7][2])*8+int(Infos[1][8][2])*8+int(Infos[1][9][2])*8,
                Infos[1][7][4]+Infos[1][7][5]+Infos[1][7][6]+Infos[1][7][7]+Infos[1][7][8]+Infos[1][7][9]+ Infos[1][8][4]+Infos[1][8][5]+Infos[1][8][6]+Infos[1][8][7]+Infos[1][8][8]+Infos[1][8][9]+Infos[1][9][4]+Infos[1][9][5]+Infos[1][9][6]+Infos[1][9][7]+Infos[1][9][8]+Infos[1][9][9],'','',''],
                
                ['DOMAINES DES LANGUES','', '','', '','', '','','','','','', '','', '','', '','','',''],
                [Infos[1][10][1],int(Infos[1][10][2]),Infos[1][10][4],Infos[1][10][5], Infos[1][10][3],Infos[1][10][6],int(Infos[1][10][2])*4,Infos[1][10][4]+Infos[1][10][5]+Infos[1][10][6],Infos[1][10][2],Infos[1][10][7],Infos[1][10][8],Infos[1][10][3],Infos[1][10][9],int(Infos[1][10][2])*4,Infos[1][10][7]+Infos[1][10][8]+Infos[1][10][9],int(Infos[1][10][2])*8,Infos[1][10][4]+Infos[1][10][5]+Infos[1][10][6]+Infos[1][10][7]+Infos[1][10][8]+Infos[1][10][9],'','',''],
                [Infos[1][11][1],int(Infos[1][11][2]),Infos[1][11][4],Infos[1][11][5], Infos[1][11][3],Infos[1][11][6],int(Infos[1][11][2])*4,Infos[1][11][4]+Infos[1][11][5]+Infos[1][11][6],Infos[1][11][2],Infos[1][11][7],Infos[1][11][8],Infos[1][11][3],Infos[1][11][9],int(Infos[1][11][2])*4,Infos[1][11][7]+Infos[1][11][8]+Infos[1][11][9],int(Infos[1][11][2])*8,Infos[1][11][4]+Infos[1][11][5]+Infos[1][11][6]+Infos[1][11][7]+Infos[1][11][8]+Infos[1][11][9],'','',''],
                ['Sous Total',int(Infos[1][10][2])+int(Infos[1][11][2]),
                int(Infos[1][10][4])+int(Infos[1][11][4]),int(Infos[1][10][5])+int(Infos[1][11][5]),
                int(Infos[1][10][3])+int(Infos[1][11][3]),int(Infos[1][10][6])+int(Infos[1][11][6]),
                int(Infos[1][10][2])*4+int(Infos[1][11][2])*4,Infos[1][10][4]+Infos[1][10][5]+Infos[1][10][6]+Infos[1][11][4]+Infos[1][11][5]+Infos[1][11][6],
                int(Infos[1][10][2])+int(Infos[1][11][2]),
                int(Infos[1][10][7])+int(Infos[1][11][7]),
                int(Infos[1][10][8])+int(Infos[1][11][8]),
                int(Infos[1][10][3])+int(Infos[1][11][3]),
                int(Infos[1][10][9])+int(Infos[1][11][9]),
                int(Infos[1][10][2])*4+int(Infos[1][11][2])*4,
                Infos[1][10][8]+Infos[1][10][9]+Infos[1][10][7]+Infos[1][11][7]+Infos[1][11][8]+Infos[1][11][9],
                int(Infos[1][10][2])*8+int(Infos[1][11][2])*8,
                Infos[1][10][4]+Infos[1][10][5]+Infos[1][10][6]+Infos[1][10][7]+Infos[1][10][8]+Infos[1][10][9]+Infos[1][11][4]+Infos[1][11][5]+Infos[1][11][6]+Infos[1][11][7]+Infos[1][11][8]+Infos[1][11][9],'','',''],
                
                ['DOMAINE DE L\'UNIVERS SOCIAL ET ENVIRONNEMENT','', '','', '','', '','','','','','', '','', '','', '','','',''],
                [Infos[1][12][1],int(Infos[1][12][2]),Infos[1][12][4],Infos[1][12][5], Infos[1][12][3],Infos[1][12][6],int(Infos[1][12][2])*4,Infos[1][12][4]+Infos[1][12][5]+Infos[1][12][6],Infos[1][12][2],Infos[1][12][7],Infos[1][12][8],Infos[1][12][3],Infos[1][12][9],int(Infos[1][12][2])*4,Infos[1][12][7]+Infos[1][12][8]+Infos[1][12][9],int(Infos[1][12][2])*8,Infos[1][12][4]+Infos[1][12][5]+Infos[1][12][6]+Infos[1][12][7]+Infos[1][12][8]+Infos[1][12][9],'','',''],
                [Infos[1][13][1],int(Infos[1][13][2]),Infos[1][13][4],Infos[1][13][5], Infos[1][13][3],Infos[1][13][6],int(Infos[1][13][2])*4,Infos[1][13][4]+Infos[1][13][5]+Infos[1][13][6],Infos[1][13][2],Infos[1][13][7],Infos[1][13][8],Infos[1][13][3],Infos[1][13][9], int(Infos[1][13][2])*4, Infos[1][13][7]+Infos[1][13][8]+Infos[1][13][9],int(Infos[1][13][2])*8,Infos[1][13][4]+Infos[1][13][5]+Infos[1][13][6]+Infos[1][13][7]+Infos[1][13][8]+Infos[1][13][9],'','',''],
                [Infos[1][14][1],int(Infos[1][14][2]),Infos[1][14][4],Infos[1][14][5], Infos[1][14][3],Infos[1][14][6],int(Infos[1][14][2])*4,Infos[1][14][4]+Infos[1][14][5]+Infos[1][14][6],Infos[1][14][2],Infos[1][14][7],Infos[1][14][8],Infos[1][14][3],Infos[1][14][9], int(Infos[1][14][2])*4, Infos[1][14][7]+Infos[1][14][8]+Infos[1][14][9],int(Infos[1][14][2])*8,Infos[1][14][4]+Infos[1][14][5]+Infos[1][14][6]+Infos[1][14][7]+Infos[1][14][8]+Infos[1][14][9],'','',''],
                [Infos[1][15][1],int(Infos[1][15][2]),Infos[1][15][4],Infos[1][15][5], Infos[1][15][3],Infos[1][15][6],int(Infos[1][15][2])*4,Infos[1][15][4]+Infos[1][15][5]+Infos[1][15][6],Infos[1][15][2],Infos[1][15][7],Infos[1][15][8],Infos[1][15][3],Infos[1][15][9], int(Infos[1][15][2])*4, Infos[1][15][7]+Infos[1][15][8]+Infos[1][15][9],int(Infos[1][15][2])*8,Infos[1][15][4]+Infos[1][15][5]+Infos[1][15][6]+Infos[1][15][7]+Infos[1][15][8]+Infos[1][15][9],'','',''],
                [Infos[1][16][1],int(Infos[1][16][2]),Infos[1][16][4],Infos[1][16][5], Infos[1][16][3],Infos[1][16][6],int(Infos[1][16][2])*4,Infos[1][16][4]+Infos[1][16][5]+Infos[1][16][6],Infos[1][16][2],Infos[1][16][7],Infos[1][16][8],Infos[1][16][3],Infos[1][16][9],int(Infos[1][16][2])*4, Infos[1][16][7]+Infos[1][16][8]+Infos[1][16][9],int(Infos[1][16][2])*8, Infos[1][16][4]+Infos[1][16][5]+Infos[1][16][6]+Infos[1][16][7]+Infos[1][16][8]+Infos[1][16][9],'','',''],
                ['Sous Total',int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+int(Infos[1][16][2]),
                int(Infos[1][12][4])+int(Infos[1][13][4])+int(Infos[1][14][4])+int(Infos[1][15][4])+int(Infos[1][16][4]),
                int(Infos[1][12][5])+int(Infos[1][13][5])+int(Infos[1][14][5])+int(Infos[1][15][5])+int(Infos[1][16][5]),
                 int(Infos[1][12][3])+int(Infos[1][13][3])+int(Infos[1][14][3])+int(Infos[1][15][3])+int(Infos[1][16][3]),
                int(Infos[1][12][6])+int(Infos[1][13][6])+int(Infos[1][14][6])+int(Infos[1][15][6])+int(Infos[1][16][6]),
                int(Infos[1][12][2])*4+int(Infos[1][13][2])*4+int(Infos[1][14][2])*4+int(Infos[1][15][2])*4+int(Infos[1][16][2])*4,
                int(Infos[1][12][4])+int(Infos[1][13][4])+int(Infos[1][14][4])+int(Infos[1][15][4])+int(Infos[1][16][4])+int(Infos[1][12][5])+int(Infos[1][13][5])+int(Infos[1][14][5])+int(Infos[1][15][5])+int(Infos[1][16][5])+int(Infos[1][12][6])+int(Infos[1][13][6])+int(Infos[1][14][6])+int(Infos[1][15][6])+int(Infos[1][16][6]),int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+int(Infos[1][16][2]),
                int(Infos[1][12][7])+int(Infos[1][13][7])+int(Infos[1][14][7])+int(Infos[1][15][7])+int(Infos[1][16][7]),
                int(Infos[1][12][8])+int(Infos[1][13][8])+int(Infos[1][14][8])+int(Infos[1][15][8])+int(Infos[1][16][8]),
                int(Infos[1][12][3])+int(Infos[1][13][3])+int(Infos[1][14][3])+int(Infos[1][15][3])+int(Infos[1][16][3]),
                int(Infos[1][12][9])+int(Infos[1][13][9])+int(Infos[1][14][9])+int(Infos[1][15][9])+int(Infos[1][16][9]),
                int(Infos[1][12][2])*4+int(Infos[1][13][2])*4+int(Infos[1][14][2])*4+int(Infos[1][15][2])*4+int(Infos[1][16][2])*4,
                int(Infos[1][12][8])+int(Infos[1][13][8])+int(Infos[1][14][8])+int(Infos[1][15][8])+int(Infos[1][16][8])+int(Infos[1][12][9])+int(Infos[1][13][9])+int(Infos[1][14][9])+int(Infos[1][15][9])+int(Infos[1][16][9])+int(Infos[1][12][7])+int(Infos[1][13][7])+int(Infos[1][14][7])+int(Infos[1][15][7])+int(Infos[1][16][7]),
                int(Infos[1][12][2])*8+int(Infos[1][13][2])*8+int(Infos[1][14][2])*8+int(Infos[1][15][2])*8+int(Infos[1][16][2])*8,
                int(Infos[1][12][4])+int(Infos[1][13][4])+int(Infos[1][14][4])+int(Infos[1][15][4])+int(Infos[1][16][4])+int(Infos[1][12][5])+int(Infos[1][13][5])+int(Infos[1][14][5])+int(Infos[1][15][5])+int(Infos[1][16][5])+int(Infos[1][12][6])+int(Infos[1][13][6])+int(Infos[1][14][6])+int(Infos[1][15][6])+int(Infos[1][16][6])+int(Infos[1][12][8])+int(Infos[1][13][8])+int(Infos[1][14][8])+int(Infos[1][15][8])+int(Infos[1][16][8])+int(Infos[1][12][9])+int(Infos[1][13][9])+int(Infos[1][14][9])+int(Infos[1][15][9])+int(Infos[1][16][9])+int(Infos[1][12][7])+int(Infos[1][13][7])+int(Infos[1][14][7])+int(Infos[1][15][7])+int(Infos[1][16][7]),'','',''],


                ['DOMAINE DES ARTS','', '','', '','', '','','','','','', '','', '','', '','','',''],
                [Infos[1][17][1],int(Infos[1][17][2]),Infos[1][17][4],Infos[1][17][5], Infos[1][17][3],Infos[1][17][6],int(Infos[1][17][2])*4,Infos[1][17][4]+Infos[1][17][5]+Infos[1][17][6],Infos[1][17][2],Infos[1][17][7],Infos[1][17][8],Infos[1][17][3],Infos[1][17][9],int(Infos[1][17][2])*4,Infos[1][17][7]+Infos[1][17][8]+Infos[1][17][9],int(Infos[1][17][2])*8,Infos[1][17][4]+Infos[1][17][5]+Infos[1][17][6]+Infos[1][17][7]+Infos[1][17][8]+Infos[1][17][9],'','',''],
                [Infos[1][18][1],int(Infos[1][18][2]),Infos[1][18][4],Infos[1][18][5], Infos[1][18][3],Infos[1][18][6],int(Infos[1][18][2])*4,Infos[1][18][4]+Infos[1][18][5]+Infos[1][18][6],Infos[1][18][2],Infos[1][18][7],Infos[1][18][8],Infos[1][18][3],Infos[1][18][9],int(Infos[1][18][2])*4,Infos[1][18][7]+Infos[1][18][8]+Infos[1][18][9],int(Infos[1][18][2])*8,Infos[1][18][4]+Infos[1][18][5]+Infos[1][18][6]+Infos[1][18][7]+Infos[1][18][8]+Infos[1][18][9],'','',''],
                ['Sous Total',int(Infos[1][17][2])+int(Infos[1][18][2]),
                int(Infos[1][17][4])+int(Infos[1][18][4]),
                int(Infos[1][17][5])+int(Infos[1][18][5]),
                int(Infos[1][17][3])+int(Infos[1][18][3]),
                int(Infos[1][17][6])+int(Infos[1][18][6]),
                int(Infos[1][17][2])*4+int(Infos[1][18][2])*4,
                Infos[1][17][4]+Infos[1][18][5]+Infos[1][17][6]+Infos[1][18][4]+Infos[1][18][5]+Infos[1][18][6],
                int(Infos[1][17][2])+int(Infos[1][18][2]),
                int(Infos[1][17][7])+int(Infos[1][18][7]),
                int(Infos[1][17][8])+int(Infos[1][18][8]),
                int(Infos[1][17][3])+int(Infos[1][18][3]),
                int(Infos[1][17][9])+int(Infos[1][18][9]),
                int(Infos[1][17][2])*4+int(Infos[1][18][2])*4,
                Infos[1][17][8]+Infos[1][17][9]+Infos[1][17][7]+Infos[1][18][7]+Infos[1][18][8]+Infos[1][18][9],
                int(Infos[1][17][2])*8+int(Infos[1][18][2])*8,
                Infos[1][17][4]+Infos[1][17][5]+Infos[1][17][6]+Infos[1][17][7]+Infos[1][17][8]+Infos[1][17][9]+Infos[1][18][4]+Infos[1][18][5]+Infos[1][18][6]+Infos[1][18][7]+Infos[1][18][8]+Infos[1][18][9],'','',''],
                
                ['DOMAINE DU DEVELOPPEMENT PERSONNEL','', '','', '','', '','','','','','', '','', '','', '','','',''],
                [Infos[1][19][1],int(Infos[1][19][2]),Infos[1][19][4],Infos[1][19][5], Infos[1][19][3],Infos[1][19][6],int(Infos[1][19][2])*4,Infos[1][19][4]+Infos[1][19][5]+Infos[1][19][6],Infos[1][19][2],Infos[1][19][7],Infos[1][19][8],Infos[1][19][3],Infos[1][19][9],int(Infos[1][19][2])*4,Infos[1][19][7]+Infos[1][19][8]+Infos[1][19][9],int(Infos[1][19][2])*8,Infos[1][19][4]+Infos[1][19][5]+Infos[1][19][6]+Infos[1][19][7]+Infos[1][19][8]+Infos[1][19][9],'','',''],
                ['Sous Total',int(Infos[1][19][2]),
                int(Infos[1][19][4]),
                Infos[1][19][5], 
                int(Infos[1][19][3]),
                Infos[1][19][6],
                int(Infos[1][19][2])*4,
                Infos[1][19][4]+Infos[1][19][5]+Infos[1][19][6],
                int(Infos[1][19][2]),
                int(Infos[1][19][7]),
                int(Infos[1][19][8]),
                int(Infos[1][19][3]),
                int(Infos[1][19][9]),
                int(Infos[1][19][2])*4,
                Infos[1][19][8]+Infos[1][19][9]+Infos[1][19][7],
                int(Infos[1][19][2])*8,
                Infos[1][19][4]+Infos[1][19][5]+Infos[1][19][6]+Infos[1][19][7]+Infos[1][19][8]+Infos[1][19][9],'','',''],

                ['MAXIMA GEN',int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]), 

                int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]),

                int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]),
                
                (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*2, 

                (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*2,  

                 (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*4,
            
                 (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*4,
                
                int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]), 

                int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]),

                int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]),
                
                (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*2, 

                (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*2,  

                 (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*4,
            
                 (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*4,

                (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*8, 
                
                (int(Infos[1][0][2])+int(Infos[1][1][2])+int(Infos[1][2][2])+
                int(Infos[1][3][2])+int(Infos[1][4][2])+int(Infos[1][5][2])+
                int(Infos[1][6][2])+int(Infos[1][7][2])+int(Infos[1][8][2])+int(Infos[1][9][2])+
                int(Infos[1][10][2])+int(Infos[1][11][2])+
                int(Infos[1][12][2])+int(Infos[1][13][2])+int(Infos[1][14][2])+int(Infos[1][15][2])+
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*8,'','',''],

                ['TOTAUX','',
                 int(Infos[1][0][4])+int(Infos[1][1][4])+int(Infos[1][2][4])+
                int(Infos[1][3][4])+int(Infos[1][4][4])+int(Infos[1][5][4])+
                int(Infos[1][6][4])+int(Infos[1][7][4])+int(Infos[1][8][4])+int(Infos[1][9][4])+
                int(Infos[1][10][4])+int(Infos[1][11][4])+
                int(Infos[1][12][4])+int(Infos[1][13][4])+int(Infos[1][14][4])+int(Infos[1][15][4])+
                int(Infos[1][16][4])+int(Infos[1][17][4])+int(Infos[1][18][4])+int(Infos[1][19][4]),

                int(Infos[1][0][5])+int(Infos[1][1][5])+int(Infos[1][2][5])+
                int(Infos[1][3][5])+int(Infos[1][4][5])+int(Infos[1][5][5])+
                int(Infos[1][6][5])+int(Infos[1][7][5])+int(Infos[1][8][5])+int(Infos[1][9][5])+
                int(Infos[1][10][5])+int(Infos[1][11][5])+
                int(Infos[1][12][5])+int(Infos[1][13][5])+int(Infos[1][14][5])+int(Infos[1][15][5])+
                int(Infos[1][16][5])+int(Infos[1][17][5])+int(Infos[1][18][5])+int(Infos[1][19][5]),
                '',
                
                int(Infos[1][0][6])+int(Infos[1][1][6])+int(Infos[1][2][6])+
                int(Infos[1][3][6])+int(Infos[1][4][6])+int(Infos[1][5][6])+
                int(Infos[1][6][6])+int(Infos[1][7][6])+int(Infos[1][8][6])+int(Infos[1][9][6])+
                int(Infos[1][10][6])+int(Infos[1][11][6])+
                int(Infos[1][12][6])+int(Infos[1][13][6])+int(Infos[1][14][6])+int(Infos[1][15][6])+
                int(Infos[1][16][6])+int(Infos[1][17][6])+int(Infos[1][18][6])+int(Infos[1][19][6]), '',

                (int(Infos[1][0][4])+int(Infos[1][1][4])+int(Infos[1][2][4])+
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
                int(Infos[1][16][6])+int(Infos[1][17][6])+int(Infos[1][18][6])+int(Infos[1][19][6])),
                '',
                int(Infos[1][0][7])+int(Infos[1][1][7])+int(Infos[1][2][7])+
                int(Infos[1][3][7])+int(Infos[1][4][7])+int(Infos[1][5][7])+
                int(Infos[1][6][7])+int(Infos[1][7][7])+int(Infos[1][8][7])+int(Infos[1][9][7])+
                int(Infos[1][10][7])+int(Infos[1][11][7])+
                int(Infos[1][12][7])+int(Infos[1][13][7])+int(Infos[1][14][7])+int(Infos[1][15][7])+
                int(Infos[1][16][7])+int(Infos[1][17][7])+int(Infos[1][18][7])+int(Infos[1][19][7]),

                int(Infos[1][0][8])+int(Infos[1][1][8])+int(Infos[1][2][8])+
                int(Infos[1][3][8])+int(Infos[1][4][8])+int(Infos[1][5][8])+
                int(Infos[1][6][8])+int(Infos[1][7][8])+int(Infos[1][8][8])+int(Infos[1][9][8])+
                int(Infos[1][10][8])+int(Infos[1][11][8])+
                int(Infos[1][12][8])+int(Infos[1][13][8])+int(Infos[1][14][8])+int(Infos[1][15][8])+
                int(Infos[1][16][8])+int(Infos[1][17][8])+int(Infos[1][18][8])+int(Infos[1][19][8])
                ,'',
                int(Infos[1][0][9])+int(Infos[1][1][9])+int(Infos[1][2][9])+
                int(Infos[1][3][9])+int(Infos[1][4][9])+int(Infos[1][5][9])+
                int(Infos[1][6][9])+int(Infos[1][7][9])+int(Infos[1][8][9])+int(Infos[1][9][9])+
                int(Infos[1][10][9])+int(Infos[1][11][9])+
                int(Infos[1][12][9])+int(Infos[1][13][9])+int(Infos[1][14][9])+int(Infos[1][15][9])+
                int(Infos[1][16][9])+int(Infos[1][17][9])+int(Infos[1][18][9])+int(Infos[1][19][9]),
                '', 
                (int(Infos[1][0][7])+int(Infos[1][1][7])+int(Infos[1][2][7])+
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
                int(Infos[1][16][9])+int(Infos[1][17][9])+int(Infos[1][18][9])+int(Infos[1][19][9])),'',
                
                 ((int(Infos[1][0][4])+int(Infos[1][1][4])+int(Infos[1][2][4])+
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
                int(Infos[1][16][9])+int(Infos[1][17][9])+int(Infos[1][18][9])+int(Infos[1][19][9]))),'','-PASSE (1) \n-Double (1)\n\nLE CHEF D\'ET.\nSceau de l\'école',''],
                
                ['POURCENTAGE','',
                 round(((int(Infos[1][0][4])+int(Infos[1][1][4])+int(Infos[1][2][4])+
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
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))),1),

                round((int(Infos[1][0][5])+int(Infos[1][1][5])+int(Infos[1][2][5])+
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
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2])),1) ,'',

                round((int(Infos[1][0][6])+int(Infos[1][1][6])+int(Infos[1][2][6])+
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
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*2),1) , '',
                
                round(((int(Infos[1][0][4])+int(Infos[1][1][4])+int(Infos[1][2][4])+
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
                ,'',
                round((int(Infos[1][0][7])+int(Infos[1][1][7])+int(Infos[1][2][7])+
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
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2])),1) ,
                
                round((int(Infos[1][0][8])+int(Infos[1][1][8])+int(Infos[1][2][8])+
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
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2])),1) ,'', 
                
                round((int(Infos[1][0][9])+int(Infos[1][1][9])+int(Infos[1][2][9])+
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
                int(Infos[1][16][2])+int(Infos[1][17][2])+int(Infos[1][18][2])+int(Infos[1][19][2]))*2),1) ,'', 
                
                #Pourcentage deuxime semestre
                round(((int(Infos[1][0][7])+int(Infos[1][1][7])+int(Infos[1][2][7])+
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
                ,'',
                
                #Pourcentage fin d'annee de l'eleve
                round( (((int(Infos[1][0][4])+int(Infos[1][1][4])+int(Infos[1][2][4])+
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
               ,'','',''],
                ['PLACE / Nbr Elè ','',str(place[1])+"e/"+str(len(self.Data)),str(place[2])+"e/"+str(len(self.Data)), '',str(place[3])+"e/"+str(len(self.Data)), '',str(place[4])+"e/"+str(len(self.Data)),'',str(place[5])+"e/"+str(len(self.Data)),str(place[6])+"e/"+str(len(self.Data)),'',str(place[7])+"e/"+str(len(self.Data)),'',str(place[8])+"e/"+str(len(self.Data)),'',str(place[9])+"e/"+str(len(self.Data)),'','',''],
                ['APPLICATION','', '','', '','', '','','','','','', '','', '','', '','','',''],
                ['CONDUITE','', '','', '','', '','','','','','', '','', '','', '','','',''],
                ['SIGNAT. RESP.','', '','', '','', '','','','','','', '','', '','', '','','',''],
                [PiedTable,'', '','', '','', '','','','','','', '','', '','', '','','',''],

            ]

            #Definitions des largeurs de colonnes
            taille =[80,25,25,25,25,25,25,25,25,25,25 ,25 ,25 ,25 ,25 ,25 ,25,25,25,60]

            # Définition des styles de cellule pour les fusions
            HeightRow =[60,12,12,55,15,11,12,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,100]
            style = TableStyle([   # Renvoie à la ligne
                                
                                ('ROWHEIGHTS', (0, 0), (0,0),100),
                                
                                # ligne en tete
                                ('SPAN', (0, 0), (19,0)),
                                ('SPAN', (0, 1), (19,1)),

                                ('SPAN', (0, 2), (19,2)),
                                ('VALIGN', (0, 2), (0,2),'MIDDLE'),
                                ('FONTSIZE', (0, 2), (0,2),9),
                            
                                # ligne infos eleves 
                                ('SPAN', (0, 3), (7, 3)),
                                ('ALIGN', (0,3), (0,3),'RIGHT'),
                                ('ALIGN', (1,5), (1,5),'CENTER'),

                                ('SPAN', (8, 3), (19, 3)),

                                # ligne classe et annee scolaire
                                ('SPAN', (0, 4), (19,4)),
                                # ligne Branche
                                ('SPAN', (0, 5), (0,8)),
                                #Premier semestre
                                ('SPAN', (1, 5), (7,5)),
                                #Max
                                ('SPAN', (1, 6), (1,8)),
                                ('ALIGN',  (1,6), (1,6),'CENTER'),
                                #Travaux journ
                                ('SPAN', (2, 6), (3,6)),
                                ('WORDWRAP',(2,6), (2,6),1),
                                ('ALIGN', (2,6), (2,6),'CENTER'),
                                ('SPAN', (2, 6), (3,7)),
                                #Exament
                                ('SPAN', (4, 6), (5,6)),
                                ('ALIGN', (4,6), (4,6),'CENTER'),
                                ('SPAN', (4, 6), (5,8)),
                                #TotalGeneral
                                ('SPAN', (6, 6), (7,6)),
                                ('ALIGN', (6,6), (6,6),'CENTER'),
                                ('SPAN', (6, 6), (7,8)),

                                #Second semestre
                                ('SPAN', (8, 5), (14,5)),
                                ('ALIGN', (8,5), (8,5),'CENTER'),

                                #Max
                                ('SPAN', (8, 6), (8,8)),
                                ('ALIGN', (8,6), (8,6),'CENTER'),
                                #TravauxJournalier
                                ('SPAN', (9, 6), (10,6)),
                                ('SPAN', (9, 6), (10,7)),
                                ('ALIGN', (9,6), (9,6),'CENTER'),

                                #TravauxJournalier
                                ('SPAN', (11, 6), (12,6)),
                                
                                ('SPAN', (11, 6), (12,8)),
                                ('ALIGN', (10,6), (10,6),'CENTER'),
                                #TotalGen
                                ('SPAN', (13, 6), (14,6)),
                                ('SPAN', (13, 6), (14,8)),
                                ('ALIGN', (13,6), (13,6),'CENTER'),
                                #TotGeneral
                                ('SPAN', (15, 5), (16,5)),
                                ('SPAN', (15, 5), (16,8)),
                                ('ALIGN', (15,5), (15,5),'CENTER'),

                                #LigneVide
                                ('SPAN', (17, 5), (17,50)),
                                ('BACKGROUND', (17, 5), (17,5),colors.black),

                                #Exament de repechage
                                ('SPAN', (18, 5), (19,5)),
                                ('ALIGN', (18,5), (18,5),'CENTER'),
                                ('SPAN', (18, 5), (19,7)),
                

                                
                                
                                
                                #('GRID', (0, 0), (-1,-1),0,(0,0,0,0)),
                                #Trav Journalier
                                # ajout de l'alignement pour chaque lignes
                                ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
                                ('FONTSIZE', (0, 0), (-1,-1),8),

                                #Corps du bulletins

                                #Colonnes 19 et 20
                                ('ALIGN', (18,6), (18,6),'CENTER'),
                                ('SPAN', (18, 9), (19,9)),
                                ('SPAN', (18, 9), (19,10)),
                                ('BACKGROUND', (18, 9), (18,9),colors.black),
                                #Domaines1
                                ('SPAN', (0, 9), (16,9)),
                                ('ALIGN', (0,9), (0,9),'CENTER'),
                                ('FONTWEIGHT', (0,9), (0,9),'BOLD'),
                                ('BACKGROUND', (0, 9), (0,9),'#f0efec'),
                                ('SPAN', (0, 10), (16,10)),
                                ('ALIGN', (0,10), (0,10),'CENTER'),
                                ('BACKGROUND', (0, 10), (0,10),'#f0efec'),

                                #Domaines2
                                ('SPAN', (0, 16), (16,16)),
                                ('SPAN', (18, 16), (19,16)),
                                ('ALIGN', (0,16), (0,16),'CENTER'),
                                ('BACKGROUND', (0, 16), (0,16),'#f0efec'),
                                ('BACKGROUND', (18, 16), (18,16),'#f0efec'),

                                #Domaines3
                                ('SPAN', (0, 21), (16,21)),
                                ('SPAN', (18, 21), (19,21)),
                                ('ALIGN', (0, 21), (0,21),'CENTER'),
                                ('BACKGROUND',(0, 21), (0,21),'#f0efec'),
                                ('BACKGROUND', (18, 21), (18,21),'#f0efec'),

                                #Domaines4
                                ('SPAN', (0, 26), (16,26)),
                                ('SPAN', (18, 26), (19,26)),
                                ('ALIGN', (0, 26), (0,26),'CENTER'),
                                ('BACKGROUND',(0, 26), (0,26),'#f0efec'),
                                ('BACKGROUND', (18, 26), (18,26),'#f0efec'),

                                #Domaines5
                                ('SPAN', (0, 30), (16,30)),
                                ('SPAN', (18, 30), (19,30)),
                                ('ALIGN', (0, 30), (0,30),'CENTER'),
                                ('BACKGROUND',(0, 30), (0,30),'#f0efec'),
                                ('BACKGROUND', (18, 30), (18,30),'#f0efec'),
                                #Domaines6
                                ('SPAN', (0, 37), (16,37)),
                                ('SPAN', (18, 37), (19,37)),
                                ('ALIGN', (0, 37), (0,37),'CENTER'),
                                ('BACKGROUND',(0, 37), (0,37),'#f0efec'),
                                ('BACKGROUND', (18, 37), (18,37),'#f0efec'),

                                #Domaines7
                                ('SPAN', (0, 41), (16,41)),
                                ('SPAN', (18, 41), (19,41)),
                                ('ALIGN', (0, 41), (0,41),'CENTER'),
                                ('BACKGROUND',(0, 41), (0,41),'#f0efec'),
                                ('BACKGROUND', (18, 41), (18,41),'#f0efec'),

                                #PIED DES PAGES NOIR
                                ('SPAN', (1, 45), (1,49)),
                                ('BACKGROUND',(1, 45), (1,49),colors.black),
                                ('SPAN', (1, 50), (2,50)),
                                ('SPAN', (3, 50), (7,50)),
                                ('SPAN', (8, 50), (9,50)),
                                ('SPAN', (10, 50), (16,50)),

                                ('BACKGROUND',(4, 49), (8,49),colors.black),
                                ('BACKGROUND',(4, 48), (8,48),colors.black),
                                ('BACKGROUND',(4, 48), (4,44),colors.black),
                                ('BACKGROUND',(6, 48), (6,44),colors.black),
                                ('BACKGROUND',(8, 48), (8,44),colors.black),

                                ('BACKGROUND',(11, 48), (17,48),colors.black),
                                ('BACKGROUND',(11, 49), (17,49),colors.black),
                                ('BACKGROUND',(11, 48), (11,44),colors.black),
                                ('BACKGROUND',(13, 48), (13,44),colors.black),
                                ('BACKGROUND',(15, 48), (15,44),colors.black),

                                #Decision
                                ('SPAN', (18, 50), (19,50)),
                                ('SPAN', (18, 50), (19,45)),
                                ('SPAN', (18, 44), (19,44)),
                                ('BACKGROUND',(18, 44),(18, 44),'#f0efec'),

                                #pied de page
                                ('SPAN', (0, 51), (19,51)),

                        
                                ],)

            # Création du tableau
            table = Table(data, colWidths=taille, rowHeights=HeightRow, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])

           
            # Application du style de fusion
            table.setStyle(style)
            self.bull.append(table)

            #Donnees d'orientation des eleves 
            d1= ((Infos[1][0][4]+Infos[1][0][5]+Infos[1][0][6]+Infos[1][0][7]+Infos[1][0][8]+Infos[1][0][9]+Infos[1][1][4]+Infos[1][1][5]+Infos[1][1][6]+Infos[1][1][7]+Infos[1][1][8]+Infos[1][1][9]+ Infos[1][2][4]+Infos[1][2][5]+Infos[1][2][6]+Infos[1][2][7]+Infos[1][2][8]+Infos[1][2][9]+Infos[1][3][4]+Infos[1][3][5]+Infos[1][3][6]+Infos[1][3][7]+Infos[1][3][8]+Infos[1][3][9])*100)/(int(Infos[1][0][2])*8+int(Infos[1][1][2])*8+int(Infos[1][2][2])*8+int(Infos[1][3][2])*8)
            d1=round(d1,2)
            print('Domaine',d1)
            d2=((Infos[1][4][4]+Infos[1][4][5]+Infos[1][4][6]+Infos[1][4][7]+Infos[1][4][8]+Infos[1][4][9]+ Infos[1][5][4]+Infos[1][5][5]+Infos[1][5][6]+Infos[1][5][7]+Infos[1][5][8]+Infos[1][5][9]+Infos[1][6][4]+Infos[1][6][5]+Infos[1][6][6]+Infos[1][6][7]+Infos[1][6][8]+Infos[1][6][9])*100)/(int(Infos[1][4][2])*8+int(Infos[1][5][2])*8+int(Infos[1][6][2])*8)
            d2=round(d2,2)
            d3=((Infos[1][7][4]+Infos[1][7][5]+Infos[1][7][6]+Infos[1][7][7]+Infos[1][7][8]+Infos[1][7][9]+ Infos[1][8][4]+Infos[1][8][5]+Infos[1][8][6]+Infos[1][8][7]+Infos[1][8][8]+Infos[1][8][9]+Infos[1][9][4]+Infos[1][9][5]+Infos[1][9][6]+Infos[1][9][7]+Infos[1][9][8]+Infos[1][9][9])*100)/(int(Infos[1][7][2])*8+int(Infos[1][8][2])*8+int(Infos[1][9][2])*8)
            d3=round(d3,2)
            d4=((Infos[1][10][4]+Infos[1][10][5]+Infos[1][10][6]+Infos[1][10][7]+Infos[1][10][8]+Infos[1][10][9]+Infos[1][11][4]+Infos[1][11][5]+Infos[1][11][6]+Infos[1][11][7]+Infos[1][11][8]+Infos[1][11][9])*100)/(int(Infos[1][10][2])*8+int(Infos[1][11][2])*8)
            d4=round(d4,2)
            d5=((int(Infos[1][12][4])+int(Infos[1][13][4])+int(Infos[1][14][4])+int(Infos[1][15][4])+int(Infos[1][16][4])+int(Infos[1][12][5])+int(Infos[1][13][5])+int(Infos[1][14][5])+int(Infos[1][15][5])+int(Infos[1][16][5])+int(Infos[1][12][6])+int(Infos[1][13][6])+int(Infos[1][14][6])+int(Infos[1][15][6])+int(Infos[1][16][6])+int(Infos[1][12][8])+int(Infos[1][13][8])+int(Infos[1][14][8])+int(Infos[1][15][8])+int(Infos[1][16][8])+int(Infos[1][12][9])+int(Infos[1][13][9])+int(Infos[1][14][9])+int(Infos[1][15][9])+int(Infos[1][16][9])+int(Infos[1][12][7])+int(Infos[1][13][7])+int(Infos[1][14][7])+int(Infos[1][15][7])+int(Infos[1][16][7]))*100)/(int(Infos[1][12][2])*8+int(Infos[1][13][2])*8+int(Infos[1][14][2])*8+int(Infos[1][15][2])*8+int(Infos[1][16][2])*8)
            d5=round(d5,2)
            d6=((Infos[1][17][4]+Infos[1][17][5]+Infos[1][17][6]+Infos[1][17][7]+Infos[1][17][8]+Infos[1][17][9]+Infos[1][18][4]+Infos[1][18][5]+Infos[1][18][6]+Infos[1][18][7]+Infos[1][18][8]+Infos[1][18][9])*100)/(int(Infos[1][17][2])*8+int(Infos[1][18][2])*8)
            d6=round(d6,2)
            d7=((Infos[1][19][4]+Infos[1][19][5]+Infos[1][19][6]+Infos[1][19][7]+Infos[1][19][8]+Infos[1][19][9])*100)/(int(Infos[1][19][2])*8)
            d7=round(d7,2)

            DomaineInfos=[Infos[0][0][1],d1,d2,d3,d4,d5,d6,d7]
            self.DataOrientation.append(DomaineInfos)
        # Création du document PDF
    def getBulletinPDF (self,filname):
        if len(self.data[0][1])==20:
            self.GenererBulletins()
            
            doc = SimpleDocTemplate(filname, pagesize=letter,
            leftMargin=self.left,
            rightMargin=self.right,
            topMargin=self.top,
            bottomMargin=self.bottom)
            doc.build(self.bull)
            showinfo('GEST-NOTES','Enregistrement reussi')

        else:
            showwarning('GEST- NOTES','Veuillez terminer la configuration des cours pour cette classe')

    #la methode de la Creation de la fiche d'orientation des eleves
    def getRapportOrientation(self,filename):
        if len(self.data[0][1])==20:
            self.GenererBulletins()
            doc = SimpleDocTemplate(filename, pagesize=letter)
            elements = []
            styles = ParagraphStyle(name="Centered", Parent=getSampleStyleSheet()['Heading1'], fontSize=13, alignement=1) 

            #Tableau d'oreintation
            orientationTable=[['N°','NOMS ET POST - NOMS','Domaine1','Domaine2','Domaine3','Domaine4','Domaine5','Domaine6','Domaine7','Orientation']]
            c=1
            orient=''
            for item in (self.DataOrientation):
                if item[1]>item[2] and item[1]>item[3] and item[1]>item[4] and item[1]>item[5] and item[1]>item[6] and item[1]>item[7]:
                    Orient="Scientifique"
                elif item[2]>item[1] and item[2]>item[3] and item[2]>item[4] and item[2]>item[5] and item[2]>item[6] and item[2]>item[7]:
                    Orient="Construction"
                elif item[3]>item[1] and item[3]>item[2] and item[3]>item[4] and item[3]>item[5] and item[3]>item[6] and item[3]>item[7]:
                    Orient='Commercial'
                elif item[4]>item[1] and item[4]>item[2] and item[4]>item[3] and item[4]>item[5] and item[4]>item[6] and item[4]>item[7]:
                    Orient='Litteraire'
                elif item[5]>item[1] and item[5]>item[2] and item[5]>item[3] and item[5]>item[4] and item[5]>item[6] and item[5]>item[7]:
                    Orient='Social'
                elif item[6]>item[1] and item[6]>item[2] and item[6]>item[3] and item[6]>item[4] and item[6]>item[5] and item[6]>item[7]:
                    Orient='Art'
                else:
                    Orient='Art'
            
                t=[c,item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],Orient]
                orientationTable.append(t)
                c+=1

            L=[20,150,45,45,45,45,45,45,45,70]
            Orintation=Table( orientationTable,colWidths=L,style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
            style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),8),
            ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
            ('PADDING', (0, 0), (-1,-1),2),
        
            ])
            Orintation.setStyle(style)

            # Entête de la de la fiche 
            Data=[["COMPLEXE SCOLAIRE ESPOIR 1 "],["FICHE D'ORIENTATION DES ELEVES DE LA "+self.data[0][0][0][5]+" "+self.annee],['']]
            L=[500]
            H=[30,30,30]
            Header=Table(Data,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.white)])
            style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),15),
            ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
            ('PADDING', (0, 0), (-1,-1),2),
            ])
            Header.setStyle(style)
            elements.append(Header)
        
            espace = Paragraph(" ",styles)
            elements.append(espace)

            #ajout de tableau d'orientation à la liste de rendu
            elements.append(Orintation)
            doc.build(elements)
            showinfo('GEST-NOTES','Enregistrement reussi')
        else:
            showwarning('GEST- NOTES','Veuillez terminer la configuration des cours pour cette classe')



    def getFicheCote(self,filename,data):
        doc = SimpleDocTemplate(filename, pagesize=letter)
        elements = []
        styles = ParagraphStyle(name="Centered", Parent=getSampleStyleSheet()['Heading1'], fontSize=13, alignement=1) 

        #Tableau d'oreintation
        orientationTable=[['N°','NOMS ET POST - NOMS','P1','P2','E1','TOT1','P3','P4','E2','TOT2','TOT GEN']]
        c=1
        orient=''
        for item in (data[2]):
            t=[c,item[1],item[2],item[3],item[6],item[6]+item[3]+item[2],item[4],item[5],item[7],item[4]+item[5]+item[7],item[4]+item[5]+item[7]+item[6]+item[3]+item[2]]
            orientationTable.append(t)
            c+=1



        L=[20,150,40,40,40,40,40,40,40,40,60]
        Orintation=Table( orientationTable,colWidths=L,style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
        style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),8),
        ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
        ('PADDING', (0, 0), (-1,-1),2),
     
        ])
        Orintation.setStyle(style)

        # Entête de la de la fiche 
        Data=[["COMPLEXE SCOLAIRE ESPOIR 1 ","FICHE DE COTE ","ANNEE SCOLAIRE :"+self.annee],["CLASSE :"+self.data[0][0][0][5],data[0],"TITULAIRE : "+data[1]]]

        L=[180,200,180]
        H=[20,30]
        Header=Table(Data,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.white)])
        style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),10),
        ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
        ('ALIGN', (0, 0), (-1,-1),'LEFT'),
        ('PADDING', (0, 0), (-1,-1),2),
        ])
        Header.setStyle(style)
        elements.append(Header)
    
        espace = Paragraph(" ",styles)
        elements.append(espace)

        #ajout de tableau d'orientation à la liste de rendu
        elements.append(Orintation)
        doc.build(elements)

