# -*- coding: utf-8 -*-

#################
#Fenetre de jeu #
#################

#importations
#############
from tkinter import Canvas, ALL
from tkinter.messagebox import askquestion, showinfo
from random import randint
import time
from .classesModifiees import FenetreGrande
from constantes import hauteur_canevas, largeur_canevas, hauteurCanPieces, largeurCanPieces, largeurEcran
from joueur import joueurConnecte
from pieces.grille import Grille
from pieces.pieces import dico_pieces

from sgbd import sauvegarderPartie

class Jeu(FenetreGrande):
    def __init__(self, **Arguments):
        FenetreGrande.__init__(self, **Arguments)

        self.grille_jeu = Grille()
        self.flag= 1

        self.timer = 600
        self.oldTimer = self.timer

        self.flagEvent = 0
        self.appuye = False

        self.grille_piece_nulle = Grille()

        largeurOptions = largeurEcran - largeur_canevas - 45  # remaining space

        self.can_jeu = Canvas(self, bg='black', height=hauteur_canevas, width=largeur_canevas)
        self.can_jeu.grid(column=0, row=0, padx=10, pady=10)

        self.can_option = Canvas(self, height=hauteur_canevas, width=largeurOptions)
        self.can_option.grid(column=1, row=0, padx=10, pady=10)

        self.can_piece = Canvas(self.can_option, bg='black', height=hauteurCanPieces, width=largeurCanPieces)
        self.can_piece.grid(column=0, row=0, padx=5, pady=5)

        self.canNiveau = Canvas(self.can_option, height=80, width=largeurOptions-10)
        self.txtNiveau = self.canNiveau.create_text(largeurOptions//2, 40, text=f"Niveau\n{self.grille_jeu.niveau}", justify="center")
        self.canNiveau.grid(column=0, row=1, pady=5)

        self.canLignes = Canvas(self.can_option, height=80, width=largeurOptions-10)
        self.txtLignes = self.canLignes.create_text(largeurOptions//2, 40, text=f"Lignes\n{self.grille_jeu.lignes}", justify="center")
        self.canLignes.grid(column=0, row=2, pady=5)

        self.canScore = Canvas(self.can_option, height=80, width=largeurOptions-10)
        self.txtScore = self.canScore.create_text(largeurOptions//2, 40, text=f"Score\n{self.grille_jeu.score}", justify="center")
        self.canScore.grid(column=0, row=3, pady=5)

        self.bind('<KeyPress-Down>', self.descendreAppui)
        self.bind('<KeyRelease-Down>', self.descendreRelache)
        self.bind('<Right>', self.laterald)
        self.bind('<Left>', self.lateralg)
        self.bind('<a>', self.tourner)
        self.bind('<b>', self.tourner_antihoraire)
        self.bind('<x>', self.descenteDirecte)
        self.bind('<Start>', self.pause)

        self.protocol('WM_DELETE_WINDOW', self.quitter)

        self.piece_suivante=randint(1, 7)
        self.piece=eval(dico_pieces[self.piece_suivante])(self.can_jeu, self.grille_jeu)
        self.piece_suivante=randint(1, 7)
        self.piece_attente=eval(dico_pieces[self.piece_suivante])(self.can_piece, self.grille_piece_nulle)

        for i in range(2):
            self.piece_attente.lateral('g')

        for i in range(2):
            self.piece_attente.descente()

        self.jeu()

    def descendreAppui(self,event):
        if self.flag == 1:
            if self.flagEvent == 0:
                self.flagEvent = 1
                self.timer = 40

        if not self.appuye:
            self.tempsPourScore = time.time()

        self.appuye = True

    def descendreRelache(self,event):
        if self.flag == 1 and self.appuye:
            self.flagEvent = 0
            self.timer = self.oldTimer

            if (time.time()-self.tempsPourScore)*(15/2)>16:
                self.grille_jeu.score+=16
            else:
                self.grille_jeu.score+=int((time.time()-self.tempsPourScore)*(15/2))

            self.majChamps()
            self.appuye = False

    def laterald(self, event):
        if self.flag == 1:
            self.piece.lateral('d')

    def lateralg(self, event):
        if self.flag == 1:
            self.piece.lateral('g')

    def tourner(self, event):
        if self.flag == 1:
            self.piece.tourner()

    def tourner_antihoraire(self, event):
        if self.flag == 1:
            self.piece.tourner_antihoraire()

    def pause(self, event):
        if self.flag==1:
            self.cacheGrand = self.can_jeu.create_rectangle(1,1, largeur_canevas+2, hauteur_canevas+2, fill="black")
            self.cachePetit = self.can_piece.create_rectangle(1,1, largeurCanPieces+2, hauteurCanPieces+2, fill="black")
            self.pauseI = self.can_jeu.create_rectangle(100, 250, 120, 300, fill="light grey")
            self.pauseII = self.can_jeu.create_rectangle(130, 250, 150, 300, fill="light grey")
            self.flag=0

        elif self.flag==0:
            self.can_jeu.delete(self.cacheGrand)
            self.can_piece.delete(self.cachePetit)
            self.can_jeu.delete(self.pauseI)
            self.can_jeu.delete(self.pauseII)
            self.flag=1
            self.jeu()

    def quitter(self):
        if self.flag == 1:
            self.pause('<Escape>')

            self.reponse = askquestion("Partie", "Voulez-vous vraiment quitter ?!")
            if self.reponse == "yes":
                self.destroy()
            else:
                showinfo("Partie", "Alors continuons !")
                self.pause('<Escape>')
        else:
            showinfo("Partie", "Retour à l'accueil !")
            self.destroy()

    def majChamps(self):
        self.canNiveau.delete(ALL)
        self.txtNiveau = self.canNiveau.create_text(75, 50, text="Niveau\n{}".format(self.grille_jeu.niveau), justify="center")

        self.canLignes.delete(ALL)
        self.txtLignes = self.canLignes.create_text(75, 50, text="Lignes\n{}".format(self.grille_jeu.lignes), justify="center")

        self.canScore.delete(ALL)
        self.txtScore = self.canScore.create_text(75, 50, text="Score\n{}".format(self.grille_jeu.score), justify="center")

    def gameOver(self):
        self.gameOver = self.can_jeu.create_rectangle(1,1, largeur_canevas+2, 150, fill="black")
        self.txtGameOver = self.can_jeu.create_text(largeur_canevas//2, 75, text="GAME OVER", justify="center", font=('Helvetica', 20), fill="white")

    def majCanevas(self):
        self.piece.fixer()
        self.grille_jeu.enleve_ligne_pleine()

        self.can_jeu.delete(ALL)
        self.can_piece.delete(ALL)

        while self.grille_jeu.score >= 800*self.grille_jeu.niveau*self.grille_jeu.niveau:
            self.grille_jeu.niveau += 1
            if self.timer==40:
                self.timer=self.oldTimer
                self.timer *= (7/10)
                self.timer = int(self.timer)
                self.oldTimer = self.timer
                self.timer=40
            else:
                self.timer *= (7/10)
                self.timer = int(self.timer)
                self.oldTimer = self.timer


        self.grille_jeu.afficher(self.can_jeu)
        self.piece=eval(dico_pieces[self.piece_suivante])(self.can_jeu,self.grille_jeu)

        self.majChamps()

    def derniereLigneOccupee(self):
        for nbre in self.grille_jeu.grille[0]:
            if nbre != 0:
                return True

    def enregistrerPartie(self):
        sauvegarderPartie(
            self.grille_jeu.niveau,
            self.grille_jeu.score,
            self.grille_jeu.lignes,
            joueurConnecte()
        )

    def partiFinie(self):
        self.flag = 0

        self.gameOver()
        if self.grille_jeu.lignes == 0:
            self.negALarrache = "n'"
            self.txtALarrache = "aucune ligne"
        elif self.grille_jeu.lignes == 1:
            self.negALarrache = "n'"
            self.txtALarrache = "qu'1 ligne"
        else:
            self.negALarrache = ""
            self.txtALarrache = "{} lignes".format(self.grille_jeu.lignes)

        showinfo("Partie", "Votre partie est finie !\nVotre score est de {} et vous {}avez abattu {} !".format(self.grille_jeu.score,
                                                    self.negALarrache,
                                                    self.txtALarrache
                                                    ))

        self.enregistrerPartie()

        self.reponse = askquestion("Partie", "Voulez-vous rejouer ?!")

        if self.reponse == "yes":
            self.destroy()

            newJeu = Jeu(geometry=geometry, pseudoJoueur=majEntete(nomJoueur(fichierJoueur)))
            newJeu.focus_force()
            newJeu.mainloop()
        else:
            showinfo("Partie", "Retour à l'accueil !")
            self.destroy()

    def pieceSuivante(self):
        self.piece_suivante=randint(1,7)
        self.piece_attente=eval(dico_pieces[self.piece_suivante])(self.can_piece, self.grille_piece_nulle)

        for i in range(2):
            self.piece_attente.lateral('g')

        for i in range(2):
            self.piece_attente.descente()

    def descenteDirecte(self, event):
        while self.piece.check_descente():
            self.piece.descente_noview()

        self.grille_jeu.score += 10
        self.majCanevas()
        self.pieceSuivante()


    def jeu(self):
        if self.flag == 1:
            if self.derniereLigneOccupee():
                self.partiFinie()
                return None

            if self.piece.check_descente():
                self.piece.descente()

                self.after(self.timer, self.jeu)

            else:
                self.majCanevas()

                self.pieceSuivante()

                self.jeu()
