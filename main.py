# INTEGRANTES: Darlink Aguilar Graciano y Andres David Villa Marin 
from registro_matricula import RegistroMatricula
from sistema import Sistema
from materia import Materia
import numpy as np

sistema = Sistema(materias_capacity=20, usuarios_capacity=100, registros_capacity=200)

try:
    file1 = open("materias.txt", "r")
    lineas = file1.readlines() 
    
    # Imprimir cada línea con un salto de línea adicional
    for i in range(len(lineas)):
        print(i)
        if (i != 0):
            linea_materia = lineas[i].strip();
        
            id = linea_materia.split(",")[0]
            nombre = linea_materia.split(",")[1]
            creditos = linea_materia.split(",")[2]
            materia = Materia(id, nombre, creditos)
            sistema.agregar_materia(materia)
            #print(materia)
            
        
        #print(linea.strip())  # .strip() para eliminar el salto de línea original

except Exception as e:
    print("Error al abrir el archivo:", e)

finally:
    file1.close()  # Asegúrate de cerrar el archivo
