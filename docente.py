from usuario import Usuario
from datetime import date

#Se crea la clase docente, heredando todos los atributos de la clase Usuario
class Docente(Usuario):
    def __init__(self, id:str, cc:str, nombre_completo:str, email:str, fecha_nacimiento: date, departamento:str, fecha_contratacion:date, facultad:str):
        super().__init__(id, cc, nombre_completo, email, fecha_nacimiento)

        self.__departamento = departamento
        self.__fecha_contratacion = fecha_contratacion
        self.__facultad = facultad

    # Getters y setters
    @property
    def fecha_contratacion(self):
        return self.__fecha_contratacion
    
    @fecha_contratacion.setter
    def fecha_contratacion(self, fecha_contratacion):
        self.__fecha_contratacion = fecha_contratacion
    
    @property
    def facultad(self):
        return self.__facultad
    
    @facultad.setter
    def facultad(self, facultad):
        self.__facultad = facultad
    
    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento
    
    #Se crea el metodo toString
    def __str__(self):
        return f"{self.__id}, {self.__cc}, {self.__nombre_completo}, {self.__email}, {self.__fecha_nacimiento}, {self.__departamento}, {self.__facultad}, {self.__fecha_contratacion}"    