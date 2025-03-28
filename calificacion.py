
class Calificacion:

    def __init__(self, porcentaje:int, nota:float):
        self.__porcentaje = porcentaje
        self.__nota = nota
    
    # Getters y setters
    @property
    def porcentaje(self):
        return self.__porcentaje
    
    @porcentaje.setter
    def porcentaje(self, porcentaje):
        self.__porcentaje = porcentaje
    
    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, nota):
        self.__nota = nota