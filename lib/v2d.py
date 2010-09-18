# -*- coding: utf-8 -*-

# *** THIS CLASS IS PUBLIC DOMAIN ***
# Made by John Eriksson in 2009
# http://arainyday.se

import operator
import math
class v2d(object):
    def __init__(self, x, y=None):
        if x is not None and y is not None:
            self.x = float(x)
            self.y = float(y)  
        elif type(x) == v2d:
            self.x = x.x
            self.y = x.y
        elif type(x) == list or type(x) == tuple:
            self.x = x[0]
            self.y = x[1]
        else:
            raise TypeError()
    
    # Position
    def get_pos(self):
        return (self.x,self.y)
    def set_pos(self,pos):
        self.x = float(x)
        self.y = float(y)
    pos = property(get_pos, set_pos)

    def get_int_pos(self):
        return(int(round(self.x)),int(round(self.y)))        
    ipos = property(get_int_pos, set_pos)

    # Length
    def get_length(self):
        return math.sqrt(self.x**2 + self.y**2)        
    def set_length(self, len):
        l = self.get_length()
        if l: 
            self.x /= l
            self.y /= l
        self.x *= len
        self.y *= len 
    length = property(get_length, set_length)

    # Angle
    def get_angle(self):
        if ((self.x**2 + self.y**2) == 0):
            return 0
        return math.degrees(math.atan2(self.y, self.x)) 
    def set_angle(self, angle):
        self.x = self.get_length()
        self.y = 0
        r = math.radians(angle)
        c = math.cos(r)
        s = math.sin(r)
        nx = self.x*c - self.y*s
        ny = self.x*s + self.y*c
        self.x = nx
        self.y = ny        
    angle = property(get_angle, set_angle)
    
    # Operators
    def __add__(self, other): 
        return v2d(self.x+other.x,self.y+other.y)
    def __sub__(self, other):
        return v2d(self.x-other.x,self.y-other.y)
    