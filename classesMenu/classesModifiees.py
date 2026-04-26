# -*- coding: utf-8 -*-

##################################
#Classes principales pour le jeu #
##################################

#importations
#############
import platform
from tkinter import Tk, Toplevel, Label, FALSE, TOP
from constantes import geometrieFenetre, geometriePetite

#classes fenêtres
#################
class FenetreGrande(Tk):
    def __init__(self, **Arguments):
        Tk.__init__(self, **Arguments)
        self.geometry(geometrieFenetre)
        self.resizable(width=FALSE, height=FALSE)
        self.tk_setPalette(background="light sky blue", foreground="black")
        if platform.system() == 'Linux':
            self.overrideredirect(True)

class FenetrePetite(Toplevel):
    def __init__(self, parent, titre, gridOuPack, **Arguments):
        Toplevel.__init__(self, parent, **Arguments)
        self.geometry(geometriePetite)
        self.resizable(width=FALSE, height=FALSE)
        if platform.system() == 'Linux':
            self.overrideredirect(True)

        self.protocol('WM_DELETE_WINDOW', self.quitter)

        self.parent = parent
        self.bind('<b>', self.quitter)


        if gridOuPack == "g":
            Label(self, text=titre, font=("Helvetica", 20)).grid(column=1, row=1, columnspan=2)
        else:
            Label(self, text=titre, font=("Helvetica", 20)).pack(side=TOP, pady=10)

    def quitter(self, event=None):
        """fonction destroy modifiée pour remettre peutOuvrir à true quand on ferme une fenêtre satellite"""
        self.parent.peutOuvrir = True
        self.destroy()
        self.parent.focus_force()
        self.parent.lift()
