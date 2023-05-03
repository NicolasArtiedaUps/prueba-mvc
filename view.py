# -*- coding: utf-8 -*-
"""
Created on Tue May  2 09:59:18 2023

@author: lab
"""

class robotView:
    def oracion(self,mensaje):
        print(mensaje)
        print("")
    def get_user_input(self):
        elevacion=float(input("ingrese la elevacion "))
        rotacion=float(input("ingrese el giro "))
        longitud=float(input("ingrese la longuitud "))
        return elevacion,rotacion,longitud
    def mostrarValores(self,elevacion,rotacion,longitud,movimiento):
        print("")
        print(f"la elevacion es {elevacion}")
        print(f"el giro  es {rotacion}")
        print(f"la longitud es {longitud}")
        if movimiento==True:
            print("el robot se esta moviendo ")
        else:
            print("el robot esta apagado")
    
        
        
  

    
    

    