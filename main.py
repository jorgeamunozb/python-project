# INTEGRANTES: Darlink Aguilar Graciano y Andres David Villa Marin 
from registro_matricula import RegistroMatricula
from sistema import Sistema
import numpy as np

sistema = Sistema(materias_capacity=20, usuarios_capacity=100, registros_capacity=200)

try:
    file1 = open("materias.txt", "r")
    lineas = file1.readlines() 
    print(lineas) 
except:
    print("Error al abrir el archivo")
    
file1.close()