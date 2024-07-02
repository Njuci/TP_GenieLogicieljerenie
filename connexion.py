from tkinter import *
from connexion_Backend import LoginBackend
from MenuPrincipale import MenuPrincipaleFrontend
from MenuPrincipaleUser import MenuPrincipaleUserFrontend
from tkinter.messagebox import showerror,showwarning

class Connexion_Frontend:
    def __init__(self):
        self.fen = Tk()
        self.fen.title("GESTION DES NOTES ")
        self.fen.geometry("800x600")
        self.fen.resizable(width=False,height=False)
        self.conteneurTitle=Frame(self.fen,height=80,width=660,bg='white')
        self.conteneurTitle.place(x=90,y=40)
        self.titre = Label(self.conteneurTitle, text = "AUTHENTIFICATION", font = "Arial 19 bold",bg='white',fg='#6666b9').place(x=200, y=10)

        self.form=Frame(self.fen,height=300,width=300)
        self.form.place(x=110,y=100)

        self.titre1 = Label(  self.form, text = "ADMINISTRATION", font = "Arial 14",fg='#6666b9',width=28,anchor='c').place(x=0, y=10)
        self.idLab = Label(self.form, text='Nom utilisateur',font='20')
        self.idLab.place(x=20,y=50, height=30)
        self.mdpLab = Label(self.form, text='Mot de passe',font='20')
        self.mdpLab.place(x=20,y=120, height=30)
        
        self.idEnt=Entry(self.form,relief='flat', font=('arial',12))
        self.idEnt.place(x=20,y=80,width=250, height=30)
        self.mdEnt=Entry(self.form,show='*',relief='flat', font=('arial',12))
        self.mdEnt.place(x=20,y=150,width=250, height=30)
        
        self.bouton= Button(self.form,bg='#6666b9',text='Connexion',relief='flat', font=('arial',12),fg='white',command=self.login)
        self.bouton.place(x=20,y=210, width=250,height=50)
        self.curseur= None

        self.formUser=Frame(self.fen,height=300,width=300)
        self.formUser.place(x=430,y=100)

        self.titre1 = Label(  self.formUser, text = "TITULAIRE", font = "Arial 14",fg='#6666b9',width=28,anchor='c').place(x=0, y=10)
        self.idLab = Label(self.formUser, text='Nom utilisateur',font='20')
        self.idLab.place(x=20,y=50, height=30)
        self.mdpLab = Label(self.formUser, text='Mot de passe',font='20')
        self.mdpLab.place(x=20,y=120, height=30)
        
        self.NomUserTitu=Entry(self.formUser,relief='flat', font=('arial',12))
        self.NomUserTitu.place(x=20,y=80,width=250, height=30)
        self.PasswordTitu=Entry(self.formUser,show='*',relief='flat', font=('arial',12))
        self.PasswordTitu.place(x=20,y=150,width=250, height=30)
        
        self.bouton= Button(self.formUser,text='Connexion',relief="groove", font=('arial',12),fg='#6666b9',command=self.loginUser)
        self.bouton.place(x=20,y=210, width=250,height=50)
        self.curseur= None

    def fenetre(self):
        return self.fen

    def login (self):
        login=LoginBackend(self.idEnt.get(),self.mdEnt.get())
        if login.login() :
           self.curseur=login.get_curseur()
           self.con=login.get_conn()
           Fenetre=self.fen
           Menu=MenuPrincipaleFrontend(self.curseur,self.con,'admin','ET001')
           self.fen.destroy()
           Menu.fenetre().mainloop()

    def loginUser (self):
        login=LoginBackend('root','')
        if login.login() :
            self.curseur=login.get_curseur()
            self.con=login.get_conn()
            data=login.getUsers(self.curseur,self.NomUserTitu.get())
            if self.NomUserTitu.get()!='' and self.PasswordTitu.get()!='':
                    if(len(data)!=0):
                        if(self.NomUserTitu.get()==data[1][2] and self.PasswordTitu.get()==data[1][1] ):
                            Menu=MenuPrincipaleUserFrontend(self.curseur,self.con,'user',data[0][0][2],self.NomUserTitu.get())
                            self.fen.destroy()
                            Menu.fenetre().mainloop()
                        else:
                            showerror('Erreur', "Vous avez entré des mauvaises identifiants")

                    else:
                        showwarning('Warning', "Vous n'êtes pas titulaire pour cette année")
            else:
                showwarning('Warning', "Vueillez renseigner tout les champs")


      

if __name__ == '__main__' :
    fen =Connexion_Frontend()
    fen.fenetre().mainloop()