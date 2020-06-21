#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 20:10:42 2020

Function: Print()
@author: David-Castellanos
"""

# end=
print("Mi nombre es", "Python." , end="")
print("Monty Python.")
print()
print("Mi nombre es", "Python." , end="\n")
print("Monty Python.")
print()

# sep=
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")
print()
print("Mi", "nombre", "es", "Monty", "Python.", sep="")
print()

#Combinación end= y sep=
print()
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="+", end="2\n")
print()
print()

'''
Modifica la primera línea de código en el editor, utilizando las palabras 
clave sep y end, para que coincida con el resultado esperado. 
Recuerda, utilizar dos funciones print().

Resultado esperado:
    Fundamentos***Programación***en...Python

No cambies nada en la segunda invocación de print().
Funciones a cambiar:
    print("Fundamentos","Programación","en")
    print("Python")
'''
print('LABORATORIO')
print("Fundamentos","Programación","en", sep='***', end='...')
print("Python")