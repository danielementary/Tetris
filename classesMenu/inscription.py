# -*- coding: utf-8 -*-

#####################
#Inscription du jeu #
#####################

from tkinter import *
from tkinter.messagebox import *

from classesModifiees import FenetrePetite

import sys
sys.path.insert(0, "..")

from constantes import *
from fonctionsConnexion import *
from requetes import *

class Inscription(FenetrePetite):

    def __init__(self, parent, geometryPetite, titre, gridOuPack, **Arguments):
        FenetrePetite.__init__(self, parent, geometryPetite, titre, gridOuPack, **Arguments)

        self.parent = parent

        self.pseudoLabel = Label(self, text="Pseudo ", font=("Helvetica", 10)).pack(side=TOP)
        self.pseudoChamps = Entry(self, font=("Helvetica", 10))
        self.pseudoChamps.pack(side=TOP)

        self.motDePasseLabel = Label(self, text="Mot de passe", font=("Helvetica", 10)).pack(side=TOP)
        self.motDePasseChamps = Entry(self, show="*", font=("Helvetica", 10))
        self.motDePasseChamps.pack(side=TOP)

        self.ConfMotDePasseLabel = Label(self, text="Confirmer mot de passe", font=("Helvetica", 10)).pack(side=TOP)
        self.ConfMotDePasseChamps = Entry(self, show="*", font=("Helvetica", 10))
        self.ConfMotDePasseChamps.pack(side=TOP)

        self.inscrireBtn = Button(self, text="S'inscrire", command=self.inscription, font=("Helvetica", 10))
        self.inscrireBtn.pack(side=TOP, pady=30)

        self.bind('<Return>', self.inscription)


    def mdpDifferents(self):
        """vérifie la cohérence entre les deux mots de passe"""
        self.mdpUn = self.motDePasseChamps.get()
        self.mdpDeux = self.ConfMotDePasseChamps.get()

        if self.mdpUn == self.mdpDeux:
            return False
        else:
            return True

    def pseudoDejaPris(self, pseudo):
        """vérifie la disponibilité du pseudo"""
        reqPseudoPris = """SELECT PlayerID FROM Player WHERE Pseudo = '{}'""".format(pseudo)

        conn, cur = connexionDB(fichierDB)
        executeurDeRequetes(cur, [reqPseudoPris], 2)
        if len(cur.fetchall()) == 1:
            deconnexionDB(conn, cur)
            return True

    def formulaireNonValide(self):
        """vérifie si les caractères rentrés sont valides"""
        aParcourir = self.pseudoChamps.get()

        for car in aParcourir:
            if ord(car) >= 97 and ord(car) <= 122:
                continue
            elif ord(car) >= 65 and ord(car) <= 90:
                continue
            else:
                return True

        return False

    def ChampsVide(self, nomChamps):
        """vérifie si le champs est rempli"""
        if nomChamps.get() == "":
            return True
        return False

    def tropLong(self, nomChamps):
        """vérifie si le champs est trop long"""
        aParcourir = nomChamps.get()

        if len(aParcourir) > 10:
            return True

    def inscription(self, event=None):
        """inscrit le jouer et le connecte puis ferme la fenetre satellite"""
        if self.ChampsVide(self.pseudoChamps):
            showwarning("Pseudo", "Veuillez saisir un pseudo !")
        elif self.tropLong(self.pseudoChamps):
            showwarning("Pseudo", "Votre pseudo doit faire moins de 10 caractères !")
        elif self.ChampsVide(self.motDePasseChamps):
            showwarning("Mots de passe", "Veuillez saisir un mot de passe !")
        elif self.tropLong(self.motDePasseChamps):
            showwarning("Pseudo", "Votre mot de passe doit faire moins de 25 caractères !")
        elif self.ChampsVide(self.ConfMotDePasseChamps):
            showwarning("Mots de passe", "Veuillez confirmer votre mot de passe !")
        elif self.mdpDifferents():
            showwarning("Mots de passe", "Les mots de passent ne correspondent pas !")
        elif self.pseudoDejaPris(self.pseudoChamps.get()):
            showwarning("Pseudo", "Le pseudo est déjà pris !")
        elif self.formulaireNonValide():
            showwarning("Champs", "Vous avez saisi des caractères non supportés pour votre pseudo !")
        else:
            self.pseudo = self.pseudoChamps.get()
            self.motDePasse = self.motDePasseChamps.get()

            reqCreerPlayer = """INSERT INTO Player(Pseudo, Password, CreationDate)
                                VALUES('{}', '{}', date())""".format(self.pseudo, self.motDePasse)

            conn, cur = connexionDB(fichierDB)
            executeurDeRequetes(cur, [reqCreerPlayer], 0)
            deconnexionDB(conn, cur)

            connexion(fichierJoueur, self.pseudo)

            showinfo("Compte", "Votre compte a été créé !\nBonjour {} !".format(self.pseudo))

            self.parent.majContenu()

            self.parent.peutOuvrir = True

            self.destroy()
