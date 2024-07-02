import mysql.connector
from tkinter.messagebox import showerror,showwarning

class LoginBackend :
    def __init__(self,user,password):
        self.user=user
        self.password=password
        self.connexion =''

    def login(self):

        try:
            db = mysql.connector.connect(
            host = "localhost" ,
            user =self.user,
            password =self.password,
            database = "gestorientation",
            autocommit = True
            )
            if db.is_connected():
                self.connexion=db 
                return True
        except Exception as e :
            showerror('GEST-NOTES',f'Erreur de connexion {e}...')
    def get_curseur(self):
        return self.connexion.cursor()

    def getUsers(self,curseur,nom):
            try:
                # Verification si l'enseignant est titulaire pour l'annee scolaire encours
                self.connexion.start_transaction()

                sql = 'SELECT * FROM tb_anneescolaires where active=1'
                curseur.execute(sql)
                resultat1= curseur.fetchall()
                
                sql = 'SELECT * from enseignantstitu WHERE nomTut=%s'
                val=[nom,]
                curseur.execute(sql,val)
                resultat2= curseur.fetchall()

                if (len(resultat1)!=0 and len(resultat2)!=0 ):
                    sql = 'SELECT * from tb_titulaire where tb_titulaire.id_anneeSco=%s and tb_titulaire.idtut=%s '
                    val=[resultat1[0][0],resultat2[0][0]]
                    curseur.execute(sql,val)
                    resultat3=curseur.fetchall()
                    return [resultat3,resultat2[0]]
                else :
                    return []
                  

                self.connexion.commit()
            except Exception as exp :
                showerror('Erreur', str(exp))
    def get_conn(self):
        return self.connexion