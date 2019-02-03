# -*- coding: utf-8 -*-

###################
#Connexion du jeu #
###################

from tkinter import *
from tkinter.messagebox import *

from classesModifiees import FenetrePetite

import sys
sys.path.insert(0, "..")

from requetes import *
from constantes import *

class Connexion(FenetrePetite):

    def __init__(self, parent, geometryPetite, titre, gridOuPack, **Arguments):
        FenetrePetite.__init__(self, parent, geometryPetite, titre, gridOuPack, **Arguments)

        self.pseudoLabel = Label(self, text="Pseudo ", font=("Helvetica", 10)).pack(side=TOP)
        self.pseudoChamps = Entry(self, font=("Helvetica", 10))
        self.pseudoChamps.pack(side=TOP)

        self.motDePasseLabel = Label(self, text="Mot de passe", font=("Helvetica", 10)).pack(side=TOP)
        self.motDePasseChamps = Entry(self, show="*", font=("Helvetica", 10))
        self.motDePasseChamps.pack(side=TOP)

        self.connexioneBtn = Button(self, text="Se connecter", command=self.connexion, font=("Helvetica", 10)).pack(side=TOP, pady=30)

        self.bind('<Return>', self.connexion)

    def estVide(self, nomChamps):
        if nomChamps.get() == "":
            return True

    def connexion(self, event=None):
        if self.estVide(self.pseudoChamps):
            showwarning("Pseudo", "Veuillez saisir un pseudo !")
        elif self.estVide(self.motDePasseChamps):
            showwarning("Mot de passe ", "Veuillez saisir un mot de passe !")
        else:
            self.pseudo = self.pseudoChamps.get()
            self.motDePasse = self.motDePasseChamps.get()

            reqChercherPlayer = """SELECT * FROM Player
                                WHERE Pseudo = '{}'
                                AND Password = '{}'""".format(self.pseudo, self.motDePasse)

            conn, cur = connexionDB(fichierDB)
            peutSeConnecter = executeurDeRequetes(cur, [reqChercherPlayer], 1)
            deconnexionDB(conn, cur)

            if peutSeConnecter:
                connexion(fichierJoueur, self.pseudo)

                showinfo("Compte", "Vous êtes connecté !\nBonjour {} !".format(self.pseudo))

                self.parent.majContenu()

                self.parent.peutOuvrir = True

                self.destroy()
            else:
                reqChercherPlayer = """SELECT * FROM Player
                                    WHERE Pseudo = '{}'""".format(self.pseudo)

                conn, cur = connexionDB(fichierDB)
                pseudoExiste = executeurDeRequetes(cur, [reqChercherPlayer], 1)
                deconnexionDB(conn, cur)

                if pseudoExiste:
                    showinfo("Compte", "Ce mot de passe ne correspond pas à ce pseudo !")
                else:
                    showinfo("Compte", "Ce compte n'existe pas !")
