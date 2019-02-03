# -*- coding: utf-8 -*-

from piece import *

dico_pieces = ["", "Te", "Barre", "Lambda", "Carre", "Gamma", "S", "Z"]

class Te(Piece):
    def __init__(self, canevas, grille):
        Piece.__init__(self, grille)

        self.pos=2
        self.positions=[
                        [[0,1,0],[1,1,1],[0,0,0]],
                        [[0,1,0],[0,1,1],[0,1,0]],
                        [[0,0,0],[1,1,1],[0,1,0]],
                        [[0,1,0],[1,1,0],[0,1,0]]
                        ]
        self.blocs=[
                    Bloc(couleur_te, self.carre_ref_ligne, self.carre_ref_colonne-1, canevas, self.grille),
                    Bloc(couleur_te, self.carre_ref_ligne, self.carre_ref_colonne  , canevas, self.grille),
                    Bloc(couleur_te, self.carre_ref_ligne, self.carre_ref_colonne+1 , canevas, self.grille),
                    Bloc(couleur_te, self.carre_ref_ligne +1, self.carre_ref_colonne  , canevas, self.grille)
                    ]

class Barre(Piece):
    def __init__(self, canevas, grille):
        Piece.__init__(self, grille)

        self.pos=1
        self.positions=[
                        [[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]],
                        [[1,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                        ]
        self.blocs=[
                    Bloc(couleur_barre, self.carre_ref_ligne  , self.carre_ref_colonne-1, canevas, self.grille),
                    Bloc(couleur_barre, self.carre_ref_ligne, self.carre_ref_colonne , canevas, self.grille),
                    Bloc(couleur_barre, self.carre_ref_ligne, self.carre_ref_colonne+1 , canevas, self.grille),
                    Bloc(couleur_barre, self.carre_ref_ligne, self.carre_ref_colonne+2 , canevas, self.grille)
                    ]

class Lambda(Piece):
    def __init__(self, canevas, grille):
        Piece.__init__(self, grille)

        self.pos=0
        self.positions=[
                        [[1,1,1],[1,0,0],[0,0,0]],
                        [[0,1,0],[0,1,0],[0,1,1]],
                        [[0,0,1],[1,1,1],[0,0,0]],
                        [[1,1,0],[0,1,0],[0,1,0]]
                        ]
        self.blocs=[
                    Bloc(couleur_lambda, self.carre_ref_ligne , self.carre_ref_colonne-1, canevas, self.grille),
                    Bloc(couleur_lambda, self.carre_ref_ligne, self.carre_ref_colonne , canevas, self.grille),
                    Bloc(couleur_lambda, self.carre_ref_ligne , self.carre_ref_colonne+1 , canevas, self.grille),
                    Bloc(couleur_lambda, self.carre_ref_ligne+1, self.carre_ref_colonne-1 , canevas, self.grille)
                    ]

class Carre(Piece):
    def __init__(self, canevas, grille):
        Piece.__init__(self, grille)

        self.blocs=[
                    Bloc(couleur_carre, self.carre_ref_ligne  , self.carre_ref_colonne+1, canevas, self.grille),
                    Bloc(couleur_carre, self.carre_ref_ligne, self.carre_ref_colonne  , canevas, self.grille),
                    Bloc(couleur_carre, self.carre_ref_ligne+1, self.carre_ref_colonne+1 , canevas, self.grille),
                    Bloc(couleur_carre, self.carre_ref_ligne+1, self.carre_ref_colonne  , canevas, self.grille)
                    ]

    def tourner(self):
        return None

class Gamma(Piece):

    def __init__(self, canevas, grille):
        Piece.__init__(self, grille)

        self.pos=0
        self.positions=[
                        [[0,0,0],[1,1,1],[0,0,1]],
                        [[0,1,1],[0,1,0],[0,1,0]],
                        [[1,0,0],[1,1,1],[0,0,0]],
                        [[0,1,0],[0,1,0],[1,1,0]]
                        ]
        self.blocs=[
                    Bloc(couleur_gamma, self.carre_ref_ligne  , self.carre_ref_colonne-1, canevas, self.grille),
                    Bloc(couleur_gamma, self.carre_ref_ligne, self.carre_ref_colonne  , canevas, self.grille),
                    Bloc(couleur_gamma, self.carre_ref_ligne, self.carre_ref_colonne+1 , canevas, self.grille),
                    Bloc(couleur_gamma, self.carre_ref_ligne+1, self.carre_ref_colonne+1  , canevas, self.grille)
                    ]

class S(Piece):
    def __init__(self, canevas, grille):
        Piece.__init__(self, grille)

        self.pos=0
        self.positions=[
                        [[0,0,0],[0,1,1],[1,1,0]],
                        [[0,1,0],[0,1,1],[0,0,1]],
                        [[0,1,1],[1,1,0],[0,0,0]],
                        [[1,0,0],[1,1,0],[0,1,0]]
                        ]
        self.blocs=[
                    Bloc(couleur_S, self.carre_ref_ligne  , self.carre_ref_colonne, canevas, self.grille),
                    Bloc(couleur_S, self.carre_ref_ligne, self.carre_ref_colonne+1 , canevas, self.grille),
                    Bloc(couleur_S, self.carre_ref_ligne+1, self.carre_ref_colonne-1 , canevas, self.grille),
                    Bloc(couleur_S, self.carre_ref_ligne+1, self.carre_ref_colonne  , canevas, self.grille)
                    ]

class Z(Piece):
    def __init__(self, canevas, grille):
        Piece.__init__(self, grille)

        self.pos=0
        self.positions=[
                        [[0,0,0],[1,1,0],[0,1,1]],
                        [[0,0,1],[0,1,1],[0,1,0]],
                        [[1,1,0],[0,1,1],[0,0,0]],
                        [[0,1,0],[1,1,0],[1,0,0]]
                        ]
        self.blocs=[
                    Bloc(couleur_Z, self.carre_ref_ligne , self.carre_ref_colonne, canevas, self.grille),
                    Bloc(couleur_Z, self.carre_ref_ligne, self.carre_ref_colonne-1 , canevas, self.grille),
                    Bloc(couleur_Z, self.carre_ref_ligne+1, self.carre_ref_colonne , canevas, self.grille),
                    Bloc(couleur_Z, self.carre_ref_ligne+1, self.carre_ref_colonne+1 , canevas, self.grille)
                    ]
