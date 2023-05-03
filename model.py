# -*- coding: utf-8 -*-
"""
Created on Tue May  2 09:53:14 2023

@author: lab
"""

class robotModel:
    def __init__(self):
        self.elevacion=0
        self.rotacion=0
        self.longitud=0
        self.movimiento=0
    def move_elevation(self,valor):
        self.elevacion+=valor
    def move_rotation(self,valor):
        self.rotacion+=valor
    def move_longitud(self,valor):
        self.longitud+=valor
    def stop_movement(self,valor):
        self.movimiento=False