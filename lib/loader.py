# -*- coding: utf-8 -*-

# *** THIS CLASS IS PUBLIC DOMAIN ***
# Made by John Eriksson in 2009
# http://arainyday.se

import pygame
from pygame.locals import *

from os import path
class Loader(object):
    def __init__(self):
        pass

    def load_sound(self,filename):
        filepath = path.join("data","snd",filename)
        return pygame.mixer.Sound(filepath)

    def load_image(self,filename,alpha=False):
        filepath = path.join("data","img",filename)
        img = pygame.image.load(filepath)
        if alpha:
            img = img.convert_alpha()
        else:
            img = img.convert()
        return img        

    def load_font(self,filename,size):
        filepath = path.join("data","fnt",filename)
        fnt = pygame.font.Font(filepath, size)
        return fnt  
