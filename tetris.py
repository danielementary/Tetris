# -*- coding: utf-8 -*-

###############################
# Fichier de lancement du jeu #
###############################

#importations
#############

import os
import platform
import threading
from constantes import *
from classesMenu.accueil import Accueil

if platform.system() == 'Linux':
    def start_gamepad():
        try:
            import evdev
            import tkinter as tk
            from evdev import ecodes as e

            def find_device(name):
                for path in evdev.list_devices():
                    d = evdev.InputDevice(path)
                    if d.name == name:
                        return d
                return None

            def listen():
                device = find_device('Microsoft X-Box 360 pad')
                if not device:
                    return
                for event in device.read_loop():
                    app = tk._default_root
                    if not app:
                        continue
                    if event.type == e.EV_ABS:
                        if event.code == e.ABS_HAT0X:
                            if event.value == -1:
                                app.after(0, lambda: app.event_generate('<Left>'))
                            elif event.value == 1:
                                app.after(0, lambda: app.event_generate('<Right>'))
                        elif event.code == e.ABS_HAT0Y:
                            if event.value == -1:
                                app.after(0, lambda: app.event_generate('<Up>'))
                            elif event.value == 1:
                                app.after(0, lambda: app.event_generate('<Down>'))
                            elif event.value == 0:
                                app.after(0, lambda: app.event_generate('<KeyRelease-Down>'))
                    elif event.type == e.EV_KEY:
                        if event.value == 1:
                            if event.code == e.BTN_NORTH:
                                app.after(0, lambda: app.event_generate('x'))
                            elif event.code == e.BTN_WEST:
                                app.after(0, lambda: app.event_generate('y'))
                            elif event.code == e.BTN_SOUTH:
                                app.after(0, lambda: app.event_generate('a'))
                            elif event.code == e.BTN_EAST:
                                app.after(0, lambda: app.event_generate('b'))
                            elif event.code == e.BTN_SELECT:
                                app.after(0, lambda: app.event_generate('<Select>'))
                            elif event.code == e.BTN_START:
                                app.after(0, lambda: app.event_generate('<Start>'))

            thread = threading.Thread(target=listen, daemon=True)
            thread.start()
        except ImportError:
            pass

    start_gamepad()

#création de la base de données
###############################

if not os.path.isfile(fichierDB):                       #création s'il n'éxiste pas du fichier de BD
    conn, cur = connexionDB(fichierDB)                  #connexion à la BD
    executeurDeRequetes(cur, [reqPlayer, reqScore], 0)  #remplissage de la BD
    deconnexionDB(conn, cur)                            #déconnexion de la BD

#création de l'accueil
######################

deconnexion(fichierJoueur)                              #déconnexion du joueur éventuellement connectée avant le lancement du jeu

jouerDeLaMusique()                                      #jouer de la musique

Accueil(geometry=geometry,texteMenus=majListe(None),    #création de l'Accueil
        pseudoJoueur=majEntete(None)).mainloop()
