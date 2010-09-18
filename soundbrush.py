# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from lib.loader import Loader

from lib.PaintBrush import PaintBrush

import math
#import stroke

def length(tup):
	return math.sqrt(tup[0]**2 + tup[1]**2)
	

class Canvas(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.normalizer = length((width, height))

	def normalize(self, val):
		return float(val)*self.normalizer

class MusicStroke(object):
	def stop(s): pass
	def __init__(a,b,c): pass
	def tick(a,b,c,d): pass

class BrushStroke(object):
	def __init__(self, color, pos, canvas):
		self.color = color
		self.canvas = canvas
		self.music_stroke = MusicStroke(self.canvas, self.color)
		self.last_pos = pos

	def move_to(self, pos):
		delta = (abs(pos[0] - self.last_pos[0]), abs(pos[1] - self.last_pos[1]))
		arclen = math.sqrt(delta[0]**2 + delta[1]**2)
		normal_arclen = self.canvas.normalize(arclen)
		self.music_stroke.tick(self.color, normal_arclen, self.canvas.normalize(pos[1]))
		self.last_pos = pos

	def end(self):
		self.music_stroke.stop()


class Application(object):
	def __init__(self):
		self.screen = pygame.display.set_mode((800, 600),1)
		pygame.display.set_caption("Music Painter")
		pygame.init()
		loader = Loader()
		self.canvas = Canvas(800, 600)				
		self.brush = PaintBrush(self.screen)
		self.brush.set_brush(loader.load_image("brush_6.png", True))
		self.brush.set_follow_angle(True)
		self.brush.set_color(pygame.Color("Blue"))
		self.brush.set_alpha(0.2)

		self.screen.fill((255,255,255))

	def main_loop(self):                    
		next_update = pygame.time.get_ticks()
		brush_stroke = None
		color = (1.0, 0,0)
		while 1:
			for event in pygame.event.get():
				if event.type == QUIT:
					return
				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						return                    
					elif event.key == K_SPACE:
						self.screen.fill((255,255,255))
				elif event.type == MOUSEBUTTONDOWN:
					if event.button == 1:
						brush_stroke = BrushStroke(color, event.pos, self.canvas)
						self.brush.paint_from(event.pos)
				elif event.type == MOUSEMOTION:
					if event.buttons[0]:
						self.brush.paint_to(event.pos) 
						brush_stroke.move_to(event.pos)
				elif event.type == MOUSEBUTTONUP:
					brush_stroke.end()
			if pygame.time.get_ticks() >= next_update:
				next_update = next_update + 33                
				pygame.display.flip() 

def main():
	a = Application()
	a.main_loop()

	
if __name__ == '__main__': 
	main()


