from datetime import date

#Se crea la clase usuario
class Usuario:

    def __init__(self, id:str, cc:str, nombre_completo:str, email:str, fecha_nacimiento:date):
        self.__id = id
        self.__cc = cc
        self.__nombre_completo = nombre_completo
        self.__email = email
        self.__fecha_nacimiento = fecha_nacimiento

    # Getters y setters
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def cc(self):
        return self.__cc

    @cc.setter
    def cc(self, cc):
        self.__cc = cc

    @property
    def nombre_completo(self):
        return self.__nombre_completo
    
    @nombre_completo.setter
    def nombre_completo(self, nombre_completo):
        self.__nombre_completo = nombre_completo

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento