# -*- coding: utf-8 -*-

#####################################
# Utilitaires pour le projet Tetris #
#####################################

#importations
#############
import platform
import pygame
import threading
import time

def jouerDeLaMusique():
    pygame.mixer.init()
    pygame.mixer.music.load("ressources/tetris.wav")
    pygame.mixer.music.play(-1)

def demarrerManette():
    if platform.system() != 'Linux':
        return
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

        # Tracks which directions are held
        held = {'left': False, 'right': False}

        def repeat(direction, key):
            """Re-emits key every 80ms while direction is held"""
            time.sleep(0.2)
            while held[direction]:
                app = tk._default_root
                if app:
                    app.after(0, lambda k=key: app.event_generate(k))
                time.sleep(0.08)

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
                            held['left'] = True
                            held['right'] = False
                            app.after(0, lambda: app.event_generate('<Left>'))
                            threading.Thread(target=repeat, args=('left', '<Left>'), daemon=True).start()
                        elif event.value == 1:
                            held['right'] = True
                            held['left'] = False
                            app.after(0, lambda: app.event_generate('<Right>'))
                            threading.Thread(target=repeat, args=('right', '<Right>'), daemon=True).start()
                        elif event.value == 0:
                            held['left'] = False
                            held['right'] = False
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
