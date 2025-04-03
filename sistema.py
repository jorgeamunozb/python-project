from materia import Materia
from usuario import Usuario
from estudiante import Estudiante
from calificacion import Calificacion
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
            #print(self.__materias)
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
                return self.__usuarios[i]
        
    def buscar_materia(self, id: str): # Aqui se busca la materia por su id
        for i in range(0, self.__materias_count):
            if (self.__materias[i].id == id):
                return self.__materias[i]
    
    def buscar_registro_id(self, id: str): # Aqui se busca el registro por su id
        for i in range(0, self.__registros_count):
            if (self.__registros[i].id == id):
                return self.__registros[i]
       
    def buscar_registro_data (self, periodo: str, cc_estudiante, cc_docente, id_materia):
        for i in range(0, self.__registros_count):
            if (self.__registros_count[i].periodo == periodo) and (self.__registros_count[i].cc.estudiante == cc_estudiante) and (self.__registros_count[i].cc_docente == cc_docente) and (self.__registros_count[i].id.materia == id_materia):
                return self.__registros[i]
            else:
                print("Registro no encontrado")

    def toReportByEstudiante(self, id_estudiante: str,estudiante: Estudiante, materia: Materia, periodo: str, calificaciones: Calificacion, registro: RegistroMatricula):
        for i in range(self.__usuarios):
            if (self.__usuarios[i].id_estudiante == id_estudiante):
                nombre = self.__usuarios[i].usuario.nombre_completo
                cedula = self.__usuarios[i].usuario.cc
                email = self.__usuarios[i].usuario.email
                carrera = self.__usuarios[i].estudiante.carrera
                print("Nombre: " + nombre + " Cédula: " + cedula + " Email: " + email + " Carrera: " + carrera) 
                
                try:
                    with open("reporte_estudiante.txt", "a") as reporteEst:
                        reporteEst.write(f"{nombre}, {cedula}, {email}\n")
                except Exception as e:
                    print("Error al escribir en el archivo reporte estudiante " , e)
                    
                finally:
                    reporteEst.close()
                   
    def toReportByMateriaPeriodo(self, registro: RegistroMatricula):       
        materia_nombre = registro.materia.nombre
        creditos = registro.materia.creditos
        nombre_estudiante = registro.estudiante.nombre_completo
        cc_estudiante = registro.estudiante.cc
        periodo = registro.periodo
        nota_final = registro.calcular_nota_final()

        if float(nota_final) >= 3.0:
            estado_final = "Aprobo"
        else:
            estado_final = "Reprobo"
            
        try: 
            with open("reporte_periodo.txt", "a") as reportePer:
                reportePer.write(f"{materia_nombre}, {creditos}, {nombre_estudiante}, {cc_estudiante}, {periodo}, {nota_final}, {estado_final}\n")
        except Exception as e:
            print("Error al escribir en el archivo reporte periodo", e)
                   
                    