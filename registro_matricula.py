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
        
    # Metodo agregar califiacon
    def agregar_calificacion(self, calificacion: Calificacion):
        if(self.__calificaciones_count < self.__calificaciones.size):
            self.__calificaciones[self.__calificaciones_count] = calificacion
            self.__calificaciones_count += 1

    
    #Se debe crear el metodo calcular nota final 
    """
    def calcular_nota_final(self):
        nota_final = 0
        for i in range(len(self.__calificaciones)):
            if (self.__calificaciones[i] is not None):
                contador_nota = (25 * self.__calificaciones[i].porcentaje/ 100 * self.__calificaciones[i].nota/5)
                nota_final += contador_nota
        nota_final = nota_final/5
        return "{:.2f}".format(nota_final)
    """
    def calcular_nota_final(self):
        nota_final = 0
        for i in range(len(self.__calificaciones)):  
            if self.__calificaciones[i] is not None:
                contador_nota = (self.__calificaciones[i].porcentaje / 100) * (self.__calificaciones[i].nota / 5) * 25
                nota_final += contador_nota
        return "{:.2f}".format(nota_final)

    
    #Creamos el metodo toString
    def __str__(self):
        return f"{self.__id}, {self.__materia}, {self.__periodo}, {self.__docente}, {self.__estudiante}"
    
    
    
