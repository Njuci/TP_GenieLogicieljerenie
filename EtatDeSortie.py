from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph,Image
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.pdfgen import canvas
import datetime

class DocumentsScolaire:

    def __init__(self):
        # Données du tableau avec des fusions
        self.DataOrientation=[]
        self.Infoseleve=0
        self.annee=""
        
    def getListeEleve(self,filename,data,annee):
        doc = SimpleDocTemplate(filename, pagesize=letter)
        elements = []
        styles = ParagraphStyle(name="Centered", Parent=getSampleStyleSheet()['Heading1'], fontSize=13, alignement=1) 

        #Tableau d'oreintation
        orientationTable=[['N°','NOMS ET POST - NOMS','SEXE']]
        c=1
        orient=''

        for item in (data):
            t=[c,item[1],item[2]]
            orientationTable.append(t)
            c+=1

        L=[20,200,200]
        Orintation=Table( orientationTable,colWidths=L,style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
        style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),9),
        ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
        ('PADDING', (0, 0), (-1,-1),2),
     
        ])
        Orintation.setStyle(style)

        # Date du document
        today = datetime.datetime.today().strftime('%d-%m-%Y')
      

        # Entête de la de la fiche e
        Data=[["COMPLEXE SCOLAIRE ESPOIR 1 ",f"Bukavu,le {today}"],["LISTE DES ELEVES DE LA "+data[0][4]+' '+annee,'']]

        L=[250,150]
        H=[20,30]
        Header=Table(Data,colWidths=L, rowHeights=H,style=[('GRID', (0, 0), (-1, -1), 1, colors.white)])
        style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),10),
        ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
        ('ALIGN', (0, 0), (-1,-1),'LEFT'),
        ('PADDING', (0, 0), (-1,-1),2),
        ])
        Header.setStyle(style)
        elements.append(Header)
    
        #ajout de tableau d'orientation à la liste de rendu
        elements.append(Orintation)


        #Construction des PDF
        doc.build(elements)


