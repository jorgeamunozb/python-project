# INTEGRANTES: Darlink Aguilar Graciano y Andres David Villa Marin 
from registro_matricula import RegistroMatricula
from sistema import Sistema
from materia import Materia
from usuario import Usuario
from calificacion import Calificacion
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
            registro_matricula = RegistroMatricula(id_reg, id_docente, id_estudiante, id_materia, periodo, 5)# Objeto implementado----
            sistema.agregar_registro(registro_matricula)
            # print("Id registro: " + id_reg + " Id docente: " + id_docente + " Id estudiante: " + id_estudiante + " Id materia: "
            #      + id_materia + " Periodo: " + periodo)

except Exception as e:
    print("Archivo no encontrado", e)
finally:
    file_registros_academicos.close()

try:
    file_calificaionesAc = open("calificaciones_academicas.txt", "r")
    lineas_calificacionesAc = file_calificaionesAc.readlines()
    
    for i in range(len(lineas_calificacionesAc)):
        if (i != 0):
            lineas_calificaciones = lineas_calificacionesAc[i].strip()
            
            por_nota = lineas_calificaciones.split(",")[1]
            #reg = sistema.buscar_registro_id(id_reg)
            #print("reg", reg) 
            #Primero for con guiones y el segundo con los puntos
            listado_notas = por_nota.split("-")
            for j in range(len(listado_notas)):
                porc = listado_notas[j].split(":")[0]
                nota = listado_notas[j].split(":")[1]
                calificacion = Calificacion(porc, nota)
                registro_matricula.agregar_calificacion(calificacion) 
                #print("Porcentaje: "+ porc + " nota: "+ nota) 
                print("Prueba: "+ porc + "Nota: " + nota)               
                
            #print(lineas_calificaciones)
           
except Exception as e:
    print("Error al abrir el archivo")
    
finally:
    file_calificaionesAc.close()


#sistema.toReportByEstudiante("U001")


