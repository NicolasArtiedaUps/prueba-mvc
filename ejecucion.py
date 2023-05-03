# -*- coding: utf-8 -*-
"""
Created on Tue May  2 23:02:27 2023

@author: Nicolas
"""

from model import robotModel
from view import robotView
from controller import robotController

modelo=robotModel()
vista=robotView()
controlador=robotController(modelo,vista)

controlador.compilar()
    