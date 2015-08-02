init -999 python:
    # TODO:
    """
    """
    
    
    ##################### Import Modules #####################
    import os
    import sys
    import re
    import pygame
    import time
    import threading
    import string
    import logging
    import fnmatch
    import json
    import math
    from math import sin, cos, radians
    import random
    from random import randrange, randint, choice, shuffle
    import copy
    from copy import deepcopy, copy as shallowcopy
    import itertools
    from itertools import chain, izip_longest
    import operator
    from operator import attrgetter, itemgetter
    import collections
    from collections import OrderedDict
    import xml.etree.ElementTree as ET
    sys.path.append(renpy.loader.transfn("library"))
                
    ############## Settings and other useful stuff ###############
    # absolute path to the pytfall/game directory, which is formatted according
    # to the conventions of the local OS
    gamedir = os.path.normpath(config.gamedir)
    
    # enable logging via the 'logging' module
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s %(name)-15s %(message)s')
    devlog = logging.getLogger(" ".join([config.name, config.version]))
    devlogfile = logging.FileHandler(os.path.join(gamedir, "devlog.txt"))
    devlogfile.setLevel(logging.DEBUG)
    devlog.addHandler(devlogfile)
    devlog.critical("\n--- launch game ---")
    fm = logging.Formatter('%(levelname)-8s %(name)-15s %(message)s')
    devlogfile.setFormatter(fm)
    del fm
    devlog.info("game directory: %s" % str(gamedir)) # Added str() call to avoid cp850 encoding
    
    class TimeLog(_object):
        '''
        Uses Devlog log to time execustion time between the two points.
        Failed to use RenPy log, switching to dev.
        '''
        def __init__(self):
            self.log = dict()
            
        def timer(self, msg="default"):
            if config.developer:
                if msg in self.log:
                    devlog.info("%s took %s secs to run!"%(msg, time.time() - self.log[msg]))
                    del(self.log[msg])
                else:
                    self.log[msg] = time.time()
                    devlog.info("Starting timer: %s"%msg)
                    
    tl = TimeLog()
    tl.timer("Ren'Py User Init!")

    # setting the window on center
    # useful if game is launched in the window mode
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Best I can tell, does nothing, but looks kinda nice :)
    sys.setdefaultencoding('utf-8')
    
    # Getting rid of Ren'Py's containers since we don't require rollback.
    dict = _dict
    set = _set
    list = _list
    object = _object
    _rollback = False
    
    # Regestration of extra music channels:
    renpy.music.register_channel("events", "sfx", False, file_prefix="content/sfx/sound/")
    renpy.music.register_channel("events2", "sfx", False,  file_prefix="content/sfx/sound/")
    renpy.music.register_channel("world", "music", True, file_prefix="content/sfx/music/world/")
    renpy.music.register_channel("gamemusic", "music", True, file_prefix="content/sfx/music/")
    
    ######################## Classes/Functions ###################################
    # Auto Animation from a folder:
    def animate(path, delay=0.25, function=None, transition=None):
        # Build a list of all images:
        dirs = os.listdir("".join([gamedir, path]))
        images = list("".join([path[1:], "/", fn]) for fn in dirs if fn.endswith(('.png', '.gif')))
        # Build a list of arguments
        args = list()
        # for image in images:
            # args.extend([image, delay, transition])
        # return anim.TransitionAnimation(*args)
        for image in images:
            args.append([image, delay])
        return AnimateFromList(args)

    class Flags(object):
        """
        TODO: Needs to be reviewed/Updated
        """
        def set_flag(self, flag, value=True):
            setattr(self, flag, value)
            
        def mod_flag(self, flag, value):
            # This is used for flags that are counters, otherwise just use set flag method again.
            # Will write to dev log if flag doesn't exist.
            if isinstance(value, int) and hasattr(self, flag):
                setattr(self, flag, getattr(self, flag) + value)
            else:
                devlog.warning("%s flag doesn't exist or value is not an integer!" % flag)
                
        def flag(self, flag):
            if hasattr(self, flag):
                return getattr(self, flag)
            else:
                return False
                
        def del_flag(self, flag):
            if hasattr(self, flag):
                delattr(self, flag)
                
        def has_flag(self, flag):
            """
            Check if flag exists at all (not just set to false).
            """
            return hasattr(self, flag)
            
        
    def dice(value):
        """Randomly generated percentage chance to return a bool"""
        return (value / 100.0) > random.random()
    
    # "wrapper" around the notify
    def notify(message, style=False):
        if config.developer:
            if style:
                msg = "{=%s}%s"%(style, str(message))
                renpy.notify(u"%s"%msg) 
            else:
                renpy.notify(u"{size=+10}%s"%str(message))

    # Safe jump, if label doesn't exists, game will notify about it
    def jump(labelname):
        if renpy.has_label(labelname):
            notify("jump %s" % labelname)
            renpy.jump(labelname)
        else:
            notify(u"Label '%s' does not exist." % labelname)

    # Useful methods for path @ Will not work in Android, so use only for debugging.     
    def listdir(dir):
        return os.listdir(os.path.join(gamedir, dir))

    def exist(path):
        return os.path.exists(os.path.join(gamedir, path))

    # Analizis of strings and turning them into int, float or bool.
    # Useful for importing data from xml.
    def parse(string):
        try:
            value = int(string)
        except TypeError:
            value = string
        except AttributeError:
            value = string
        except ValueError:
            try:
                value = float(string)
            except ValueError:
                if string.lower() in ['true', 'yes', 'on']:
                    value = True
                elif string.lower() in ['false', 'no', 'off', 'none']:
                    value = False
                else:
                    value = string
        return value
        
    # Returns the position of cursor if show cursorPosition is called
    # show cursorPosition on bottom
    def cursorPositionFunction(st, at):
        x,y = pygame.mouse.get_pos()
        return Text("{size=-5}%d - %d"%(x,y)), .1
        # -------------------------------------------------------------------------------------------------------- Ends here    
    
    ########################## Images ##########################
    renpy.image('bg black', Solid((0, 0, 0, 255)))
    renpy.image('bg blood', Solid((150, 6, 7, 255)))
    # Colors are defined in colors.rpy


    ##################### Autoassociation #####################
    # Backrounds are automatically registered in the game and set to width/height of the default screen
    # displayed by "show bg <filename>" or similar commands
    # file name without the extention
    
label _instant_exit:
    $ renpy.quit()

# Adds a number of useful development tools to the left buttom corner
# X - Instant Exit, surpassing the confirmation diologue
# R - Restart
# Also shows mouse coordinates
screen debug_tools():
    zorder 5
    vbox:
        xalign 0.02
        yalign 0.98
        hbox:
            xalign 0
            button:
                text "X"
                action ui.callsinnewcontext("_instant_exit")
            button:
                text "R"
                action ui.callsinnewcontext("_save_reload_game")

        add (DynamicDisplayable(cursorPositionFunction)) xpos 10
        text("{size=10}[last_label]") xpos 10



init -1 python: # Constants:
    pass

init 999 python:
    # ensure that all initialization debug messages have been written to disk
    devlogfile.flush()
    tl.timer("Ren'Py User Init!")
