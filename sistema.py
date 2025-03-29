from materia import Materia
from usuario import Usuario
from registro_matricula import RegistroMatricula
import numpy as np

#Creamos la clase sistema  
class Sistema:
    def __init__(self, materias_capacity: int, usuarios_capacity: int, registros_capacity: int):
        self.__materias = np.empty(shape = materias_capacity, dtype = Materia ) # Arreglo materias
        self.__materias_count = 0
        self.__usuarios = np.empty(shape = usuarios_capacity, dtype = Usuario) # Arreglo usuarios
        self.__usuarios_count = 0
        self.__registros = np.empty(shape = registros_capacity, dtype = RegistroMatricula) # Arreglo registros
        self.__registros_count = 0
        
    # Metodos agregar materia, usuario y registro    
    def agregar_materia(self, materia: Materia):
        if (self.__materias_count <= self.__materias.size):
            self.__materias[self.__materias_count] = materia
            self.__materias_count += 1
            print(self.__materias)
        else:
            print("Suficientes materias")
            
        
    def agregar_usuario(self, usuario: Usuario):
        if (self.__usuarios_count <= self.__usuarios.size):
            self.__usuarios[self.__usuarios_count] = usuario
            self.__usuarios_count += 1
        else:
            print("Suficientes usuarios")
                
    def agregar_registro(self, registro_matricula: RegistroMatricula):
        if (self.__registros_count <= self.__registros.size):
            self.__registros[self.__registros_count] = registro_matricula
            self.__registros_count += 1
        else:
            print("Suficientes usuarios")
            
                 
    # Metodos buscar objetos  
    def buscar_usuario(self, id: str): # Aqui se busca el usuario por medio de su cedula
        for i in range(0, self.__usuarios_count):
            if (self.__usuarios[i].id == id):
                print (f"El usuario buscado es: {self.__usuarios}")
            else:
                print("Usuario no encontrado")
        
    def buscar_materia(self, id: str): # Aqui se busca la materia por su id
        for i in range(0, self.__materias_count):
            if (self.__materias[i].id == id):
                print(f"La materia buscada es: {self.__materias}")
            else:
                print("Materia no encontrada")
    
    def buscar_registro_id(self, id: str): # Aqui se busca el registro por su id
        for i in range(0, self.__registros_count):
            if (self.__registros[i].id == id):
                print(f"El registro es: {self.__registros}")
            else:
                print("Registro no encontrado")
       
    def buscar_registro_data (self, periodo: str, cc_estudiante, cc_docente, id_materia):
        for i in range(0, self.__registros_count):
            if (self.__registros_count[i].periodo == periodo) and (self.__registros_count[i].cc.estudiante == cc_estudiante) and (self.__registros_count[i].cc_docente == cc_docente) and (self.__registros_count[i].id.materia == id_materia):
                print(f"El registro es: {self.__registros}")
            else:
                print("Registro no encontrado")