from materia import Materia
from docente import Docente
from estudiante import Estudiante
from calificacion import Calificacion
import numpy as np

class RegistroMatricula:
    def __init__(self, id:str, materia:Materia, docente:Docente, estudiante:Estudiante, periodo:str, array_capacity:int):
        self.__id = id
        self.__materia = materia
        self.__periodo = periodo
        self.__docente = docente
        self.__estudiante = estudiante
        self.__calificaciones_count = 0

        # Crear arreglo...
        self.__calificaciones = np.empty(shape = array_capacity, dtype= Calificacion) # Capacidad es igual a leer el archivo "array_capacity"      
        
    # Getters y setters
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def materia(self):
        return self.__materia

    @materia.setter
    def materia(self, materia):
        self.__materia = materia
    
    @property
    def periodo(self):
        return self.__periodo

    @periodo.setter
    def periodo(self, periodo):
        self.__periodo = periodo

    @property
    def docente(self):
        return self.__docente

    @docente.setter
    def docente(self, docente):
        self.__docente = docente

    @property
    def estudiante(self):
        return self.__estudiante
    
    @estudiante.setter
    def estudiante(self, estudiante):
        self.__estudiante = estudiante
        
    def agregar_calificacion(self, calificacion: Calificacion):
        if(self.__calificaciones_count < self.__calificaciones.size):
            self.__calificaciones[self.__calificaciones_count] = calificacion
            self.__calificaciones_count += 1
        else:
            print("el 100% de las calificaciones estan digitadas")
            
    #Se debe crear el metodo calcular nota final 
    
    
    #Creamos el metodo toString
    def __str__(self):
        return f"{self.__id}, {self.__materia}, {self.__periodo}, {self.__docente}, {self.__estudiante}"
    
    
    
