from docente import Docente
from estudiante import Estudiante

class Materia:
    def __init__(self, id:str, nombre:str, creditos:int):

        self.__id = id
        self.__nombre = nombre
        self.__creditos = creditos
 
    # Getters y setters   
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def creditos(self):
        return self.__creditos

    @creditos.setter
    def creditos(self, creditos):
        self.__creditos = creditos
        
    #Se crea el metodo toString
    def __str__(self):
        return f"{self.__id}, {self.__nombre}, {self.__creditos}"