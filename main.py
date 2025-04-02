# INTEGRANTES: Darlink Aguilar Graciano y Andres David Villa Marin 
from registro_matricula import RegistroMatricula
from sistema import Sistema
from materia import Materia
from usuario import Usuario
from calificacion import Calificacion
from docente import Docente
from estudiante import Estudiante
import numpy as np

sistema = Sistema(materias_capacity = 20, usuarios_capacity = 100, registros_capacity = 200)

try:
    file1 = open("materias.txt", "r")
    lineas = file1.readlines() 
    
    for i in range(len(lineas)):
        if (i != 0):
            linea_materia = lineas[i].strip(); # Salto de linea
        
            id = linea_materia.split(",")[0]
            nombre = linea_materia.split(",")[1]
            creditos = linea_materia.split(",")[2]
            materia = Materia(id, nombre, creditos)
            sistema.agregar_materia(materia)
            #print(materia.__str__())
                  
        #print(linea.strip())  # .strip() para eliminar el salto de línea original

except Exception as e:
    print("Error al abrir el archivo:", e)

finally:
    file1.close()  # Asegúrate de cerrar el archivo


try:
    file_usuario = open("usuarios.txt", "r")
    lineas2 = file_usuario.readlines()
    
    for i in range(len(lineas2)):
        if (i != 0):
            linea_usuario = lineas2[i].strip();
            
            
            id = linea_usuario.split(",")[0]
            cc = linea_usuario.split(",")[1]
            nombre_completo = linea_usuario.split(",")[2]
            email = linea_usuario.split(",")[3]
            fecha_nacimiento = linea_usuario.split(",")[4]
            
            usuario = Usuario(id, cc, nombre_completo, email, fecha_nacimiento)
            persona = linea_usuario.split(",")[5] 
            if (persona == "Docente"):
                departamento = linea_usuario.split(",")[6]
                fecha_contratacion = linea_usuario.split(",")[7]
                facultad = linea_usuario.split(",")[8]
                docente = Docente(id, cc, nombre_completo, email, fecha_nacimiento, departamento, fecha_contratacion, facultad)  
            else:
                carrera = linea_usuario.split(",")[6]
                activo = linea_usuario.split(",")[7]
                estudiante = Estudiante(id, cc, nombre_completo, email, fecha_nacimiento, carrera, activo)
            sistema.agregar_usuario(usuario)
            #print("id: " + id + "cc: "+ cc + "nombre completo:" + nombre_completo+ "email: "+ email + "fecha de nacimiento:"+ fecha_nacimiento)
            
            
except Exception as e:
    print("Erros al abrir el archivo", e)

finally:
    file_usuario.close()

try:
    file_registros_academicos = open("registros_academicos.txt" , "r")
    lineas_registro = file_registros_academicos.readlines()

    for i in range(len(lineas_registro)):
        if (i != 0):
            lineas_reg = lineas_registro[i].strip(); 
            id_reg = lineas_reg.split(",")[0]
            id_docente = lineas_reg.split(",")[1]
            id_estudiante = lineas_reg.split(",")[2]
            id_materia = lineas_reg.split(",")[3]
            periodo = lineas_reg.split(",")[4]
            estudiante = sistema.buscar_usuario(id_estudiante)
            docente = sistema.buscar_usuario(id_docente)
            materia = sistema.buscar_materia(id_materia)
            registro_matricula = RegistroMatricula(id = id_reg, materia = materia, docente = docente, estudiante = estudiante, periodo = periodo, array_capacity = 5) # Pregunta----------- 
            sistema.agregar_registro(registro_matricula)
            # print("Id registro: " + id_reg + " Id docente: " + id_docente + " Id estudiante: " + id_estudiante + " Id materia: "
            #      + id_materia + " Periodo: " + periodo)

except Exception as e:
    print("Archivo no encontrado", e)
finally:
    file_registros_academicos.close()

try:
    file_calificaionesAc = open("calificaciones_academicas.txt", "r")
    lineas_calificacionesAc = file_calificaionesAc.readlines()[1:]
    for linea in lineas_calificacionesAc:
        id_reg, notas_porcentajes = linea.strip().split(",")
        partes_notas = notas_porcentajes.split("-")
        registro = sistema.buscar_registro_id(id = id_reg)
        for parte in partes_notas:
            porcentaje, nota = parte.split(":")
            porcentaje = int(porcentaje)
            nota = float(nota)
            calificacion = Calificacion(porcentaje = porcentaje, nota = nota)
            registro.agregar_calificacion(calificacion = calificacion) 
    print("Leido")
except Exception as e:
    print("Error al leer el archivo calificaciones")
finally:
    file_calificaionesAc.close()
#sistema.toReportByEstudiante

sistema.toReportByMateriaPeriodo(id_materia, periodo)
