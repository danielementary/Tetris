# -*- coding: utf-8 -*-

################
#Règles du jeu #
################

#importations
#############
from tkinter import Label
from .classesModifiees import FenetrePetite

class Regles(FenetrePetite):
    def __init__(self, parent, **Arguments):
        FenetrePetite.__init__(self, parent, "RÈGLES", **Arguments)
        Label(self, text="Tout le monde connaît les règles de Tetris!", wraplength=250, font=('Helvetica', 20)).pack(pady=10)
