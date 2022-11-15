import os
import tkinter.font as font
from tkinter import *
import sys
import demande 

##----- Création de la fenêtre -----##
fen = Tk()
fen.title('Cartes des distributeurs de billet')


choix_banque = IntVar()
solde = IntVar()
historique = IntVar()
retrait = IntVar()

    
##----- Création du canevas -----##
dessin = Canvas(fen, width = 1900, height = 1790, bg = 'white')
dessin.grid(row = 0, column = 0, columnspan = 2, padx = 3, pady = 3)


#Chemin absolu vers image
path_map= os.path.abspath('banque/mapboubou.gif')
path_populaire = os.path.abspath('banque/populaire.gif')
path_cic = os.path.abspath('banque/cic.gif')
path_societegenerale = os.path.abspath('banque/societegenerale.gif')
path_postale = os.path.abspath('banque/LaBanquePostale.gif')

#chemin absolu vers fond 


##----- Dessiner dans le canevas -----##
im = PhotoImage(file = path_map, master=fen)
im2 = PhotoImage(file = path_populaire, master=fen)
im3 = PhotoImage(file = path_cic, master=fen)
im4 = PhotoImage(file = path_societegenerale, master=fen)
im5 = PhotoImage(file = path_postale, master=fen)
logo1 = dessin.create_image(650, 400, image = im )
logo2 = dessin.create_image(1600, 150, image = im2 )
logo3 = dessin.create_image(1600, 420, image = im3 )
logo4 = dessin.create_image(1600, 620, image = im4 )
logo5 = dessin.create_image(1600, 820, image = im5 )
ligne1 = dessin.create_line(1460, 225, 650, 400, width=4, fill='#000000')
ligne2 = dessin.create_line(1490, 425, 750, 500, width=4, fill='#000000')
ligne3 = dessin.create_line(1490, 625, 700, 585, width=4, fill='#000000')
ligne4 = dessin.create_line(1490, 825, 520, 685, width=4, fill='#000000')










def afficher_informations():
    


def afficher_solde(id):
    pass

def afficher_historique():
    pass

def afficher_retrait():
    pass
#copier coller la fonction createnewfen et changer nom des boutons
#simuler fctionnelment DAB en mettant les differents retraits possible
#genre 20€, 40,50,70,80 et autre(autre permet de choisir un montant au choix 
#cependant prix doit etre rond pas possible de retirer moins 20€ ou genre 15€)

def afficher_depot():
    pass
def choix_fond():
    return path_fond


def effectuer_transfert():
    pass


def Quitter():
    sys.exit()


def CreateNewFen():
    
#destruction de l'ancienne image de fond, du texte et du bouton
    dessin.delete(ALL)
    Bouton_valider.destroy()
    banque4.destroy()
    banque1.destroy()
    banque3.destroy()
    banque2.destroy()

    
    path_fond = os.path.abspath('banque/ecrandistributeur.gif')
#création d'une nouvelle fenêtre avec une nouvelle taille
    fen.title("Bienvenue sur le distributeur")
    fen.geometry("1900x1563")
    fen.resizable(width=True,height=True)
    

    bg = PhotoImage(file = path_fond, master = fen)
    dessin.create_image(0,0,image = bg,anchor ='nw')
    dessin.create_text(500,25,text="Bienvenue sur ce distributeur",\
                                 font=("Arial",50, "bold"),anchor='nw')
    dessin.create_text(30,125,text="Retrait",\
                                 font=("Arial",25, "bold"),anchor='nw')
    dessin.create_text(560,125,text="Dépot :",\
                                 font=("Arial",25, "bold"),anchor='nw')
    dessin.create_text(30,300,text="Solde :",\
                                 font=("Arial",25, "bold"),anchor='nw')
    dessin.create_text(560,300,text="Historique :",\
                                 font=("Arial",25, "bold"),anchor='nw')
#caractéristiques des options du theme solde
    case_theme1_option1 = Button(fen,text ='solde',bg='#FADF8F',\
                        fg='black',font=("Arial",15),activeforeground='white',\
                        activebackground='#048B9A',command= afficher_solde)

#caractéristiques des options du theme 2
    case_theme2_option1 = Button(fen,text ='historique',bg='#FADF8F',\
                        fg='black',font=("Arial",15),activeforeground='white',\
                        activebackground='#048B9A',command=afficher_historique)
#caractéristiques des options du theme 3
    case_theme3_option1 = Button(fen,text ='Mineur',bg='#FADF8F',\
                        fg='black',font=("Arial",15),activeforeground='white',\
                        activebackground='#048B9A',command=afficher_retrait)

#caractéristiques des options du theme 4
    case_theme4_option1 = Button(fen,text ='Oui',bg='#FADF8F',fg='black',\
                        font=("Arial",15),activeforeground='white',
                        activebackground='#048B9A',command= afficher_depot)
#caractéristiques des options du theme 4
    case_theme4_option1 = Button(fen,text ='Oui',bg='#FADF8F',fg='black',\
                        font=("Arial",15),activeforeground='white',
                        activebackground='#048B9A',command= effectuer_transfert)
        

#placements des options du theme 1
    case_theme1_option1.place(x=50,y=180)

#placements des options du theme 2
    case_theme2_option1.place(x=580,y=180)
#placements des options du theme 3
    case_theme3_option1.place(x=50,y=360)

#placements des options du theme 4
    case_theme4_option1.place(x=580,y=360)


 #utiliser pour la deuxieme fenetre apres choix du distributeur
    menu_bar = Menu(fen)
    menu_fill = Menu(menu_bar, tearoff=0)
    menu_fill.add_command(label = 'Votre solde', command= afficher_solde)
    menu_fill.add_command(label = 'Historique', command= afficher_historique)
    menu_fill.add_command(label='Quitter', command= Quitter)
    menu_bar.add_cascade (label="Votre compte", menu=menu_fill)
    fen.config(menu=menu_bar)


banque1 = Radiobutton (fen,text= 'Banque Populaire', bg = '#3933FF' ,fg = 'black',\
            activeforeground='white',\
            activebackground='#3933FF', variable = choix_banque, value = 0)

banque2 = Radiobutton (fen,text= 'CIC', bg = '#5CC355' ,fg = 'black',\
            activeforeground='white',\
            activebackground='#3933FF', variable = choix_banque, value = 1)

banque3 = Radiobutton (fen,text= 'Société Générale', bg = '#FF0303' ,fg = 'black',\
            activeforeground='white',\
            activebackground='#3933FF', variable = choix_banque, value = 2)

banque4 = Radiobutton (fen,text= 'Banque Postale', bg = '#F9F902' ,fg = 'black',\
            activeforeground='white',\
            activebackground='#3933FF', variable = choix_banque, value = 3)


Bouton_valider = Button (fen,text= 'Valider votre choix',bg ='#FFFFFF',\
                fg = 'black', activeforeground= 'white',\
                    activebackground='#000000',command= CreateNewFen)


f = font.Font(size = 24)
Bouton_valider['font'] = f
banque1.place(x = 640, y = 400)
banque2.place(x = 750, y = 500)
banque3.place(x = 700, y = 585)
banque4.place(x = 520,y = 685)
Bouton_valider.place(x = 600, y = 900)



fen.mainloop() 
