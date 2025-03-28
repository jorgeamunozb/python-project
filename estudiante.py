from usuario import Usuario
from datetime import date

#Se crea la clase estudiante, heredando todos los atributos de la clase Usuario
class Estudiante(Usuario):
    
    def __init__(self, id:str, cc:str, nombre_completo:str, email:str, fecha_nacimiento:date, carrera:str, activo:bool):
        super().__init__(id, cc, nombre_completo, email, fecha_nacimiento)

        self.__carrera = carrera
        self.__activo = activo
    
    # Getters y setters   
    @property
    def carrera(self):
        return self.__carrera
    
    @carrera.setter
    def carrera(self, carrera):
        self.__carrera = carrera

    @property
    def activo(self):
        return self.__activo
    
    @activo.setter
    def activo(self, activo):
        self.__activo = activo
    
    #Se crea el metodo toString
    def __str__(self):
        return f"{self.__id}, {self.__cc}, {self.__nombre_completo}, {self.__email}, {self.__fecha_nacimiento}, {self.__carrera}, {self.__activo}"