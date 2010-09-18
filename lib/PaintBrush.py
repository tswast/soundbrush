# -*- coding: utf-8 -*-

# *** THIS CLASS IS PUBLIC DOMAIN ***
# Made by John Eriksson in 2009
# http://arainyday.se

import pygame
from pygame.locals import *

from lib.v2d import v2d
        
class PaintBrush(object):
    def __init__(self,surface):
        """
        Creates a new PaintBrush class to paint on the specified surface. 
        """
        self.last_pos = None
        self.dest = surface
        self.draw_angle = None
        self.rest = 0.0
        
        self.org_brush = None
        self.brush = None
        self.brush_rect = None

        self.space = 1.0
        self.follow_angle = False
        self.line_pattern = None
        self.pattern_index = 0
        self.pattern_cnt = 0 
        self.image_brush = False
        
        self.color = None
                        
    def _blit(self,pos):
        if self.brush is None:
            return
        
        if self.pattern is not None:
            self.pattern_cnt += 1            
            if self.pattern_cnt > self.pattern[self.pattern_index]:
                self.pattern_index = (self.pattern_index+1)%len(self.pattern)
                self.pattern_cnt = 0
                self.pattern_on = not self.pattern_on 
            if not self.pattern_on:
                return
        
        if self.follow_angle and self.draw_angle is not None:
            bimg = pygame.transform.rotozoom(self.brush,-self.draw_angle.get_angle(),1.0) 
            brect = bimg.get_rect()
        else:
            bimg = self.brush
            brect = self.brush_rect
                    
        brect.center = pos.ipos
        self.dest.blit(bimg,brect.topleft)

    def _blit_line(self,from_pos,to_pos):
                
        draw_vect = to_pos-from_pos
        
        if self.draw_angle is None:
            self.draw_angle = v2d(draw_vect)
            self.draw_angle.length = 20.0
        else:
            self.draw_angle+=draw_vect
            self.draw_angle.length = 20.0
           
        len = draw_vect.length      
        
        if len < self.rest:
            self.rest-=len
            return
        
        if self.rest>0.0:
            draw_vect.length = self.rest
            cur_pos = from_pos+draw_vect
        else:
            cur_pos = v2d(from_pos)
        
        len-=self.rest
        self.rest = 0.0
        self._blit(cur_pos)
        
        draw_vect.length = self.space
        while len > self.space:
            cur_pos += draw_vect
            self._blit(cur_pos)
            len-=self.space
            
        self.rest = self.space-len
        
    def set_brush(self,brush,image_brush=False):
        """
        Sets the surface to be used as a brush. 
        If image_brush is True the brush will not be affected by color changes.
        """
        self.org_brush = brush.copy()
        self.brush = brush.copy()
        self.brush_rect = brush.get_rect()
        self.space = 1.0
        self.follow_angle = False
                
        self.image_brush = image_brush
        
        self.pattern = None
        self.pattern_index = 0
        self.pattern_cnt = 0 
        self.pattern_on = True
     
    def set_space(self,space):
        """
        Sets the distance between the individual blits. Default value is 1.0.
        """
        self.space = float(space)

    def set_follow_angle(self,follow_angle):
        """
        If follow_angle is True then the brush will rotate along with the drawing angle.
        """
        self.follow_angle = follow_angle
                
    def set_pattern(self,pattern):
        """
        Sets the current line pattern. 
        The pattern attribute must be a list or a tuple containing integers or None to draw continuous lines.
        Ex: pattern=[30,20,8,10]
        This mean: 30 blits, 20 blanks, 8 blits, 10 blanks   
        """
        self.pattern = pattern
        self.pattern_index = 0
        self.pattern_cnt = 0 
        self.pattern_on = True
        
    def set_color(self,color):
        """
        Color must be a pygame.Color object.
        Sets the color of all pixels in the brush. Will not affect the per pixel alpha values.
        This will have no effect if the brush is set as an image brush.
        """
        if not self.brush or self.image_brush:
            return
        self.color = color
        for x in range(self.brush_rect.width):
            for y in range(self.brush_rect.height):
                c = self.brush.get_at((x, y))
                color.a = c.a
                self.brush.set_at((x,y),color)
        
    def set_alpha(self,alpha):
        """
        Modify the current per pixel alpha values.
        Alpha value can be 0.0 to 1.0
        """
        if not self.brush:
            return
        for x in range(self.brush_rect.width):
            for y in range(self.brush_rect.height):
                c = self.org_brush.get_at((x, y))
                if self.color is not None and not self.image_brush:
                    c.r = self.color.r
                    c.g = self.color.g
                    c.b = self.color.b
                c.a = int(round(float(c.a)*alpha))
                self.brush.set_at((x,y),c)        
        
    def paint_line(self,from_pos,to_pos):
        """
        Paints a line.
        Ex: paint_line((30,40),(210,113))
        """
        if not self.brush:
            return
        self.paint_from(from_pos)
        self.paint_to(to_pos)    
        
    def paint_from(self,pos):
        """
        Starts to paint at the given position.
        Ex: paint_from((30,40))
        """
        if not self.brush:
            return        
        self.rest = 0.0
        self.last_pos = v2d(pos)
        if not self.follow_angle:            
            self._blit_line(self.last_pos,v2d(pos))
        else:
            self.draw_angle = None
        self.pattern_index = 0
        self.pattern_cnt = 0
        self.pattern_on = True 

    def paint_to(self,pos):
        """
        Paint from the last position to the given one.
        Ex: paint_to((210,113))
        """
        if not self.brush:
            return        
        if pos and self.last_pos:
            pos = v2d(pos)
            self._blit_line(self.last_pos,pos)
            self.last_pos = pos
