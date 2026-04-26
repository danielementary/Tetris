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
        self.focus_force()
        self.lift()

class FenetrePetite(Toplevel):
    def __init__(self, parent, titre, **Arguments):
        Toplevel.__init__(self, parent, **Arguments)
        self.geometry(geometriePetite)
        self.resizable(width=FALSE, height=FALSE)
        self.configure(bd=5, relief="solid")
        if platform.system() == 'Linux':
            self.overrideredirect(True)
        self.focus_force()
        self.lift()

        Label(self, text=titre, font=("Helvetica", 30)).pack(side=TOP, pady=10)

        self.parent = parent
        self.parent.peutOuvrir = False
        self.protocol('WM_DELETE_WINDOW', self.quitter)
        self.bind('<b>', self.quitter)

    def quitter(self, event=None):
        """fonction destroy modifiée pour remettre peutOuvrir à true quand on ferme une fenêtre satellite"""
        self.parent.peutOuvrir = True
        self.destroy()
        self.parent.focus_force()
        self.parent.lift()
