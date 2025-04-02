# INTEGRANTES: Darlink Aguilar Graciano y Andres David Villa Marin 
from registro_matricula import RegistroMatricula
from sistema import Sistema
from materia import Materia
from usuario import Usuario
from calificacion import Calificacion
import numpy as np

#1. Cree un objeto de Sistema con capacidad de 20 para las materias, 100 para los usuarios y 200 para los registros.
sistema = Sistema(materias_capacity = 20, usuarios_capacity = 100, registros_capacity = 200)


#2. Lea el archivo materias.txt y rellene el arreglo de materias con la información del archivo
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
            #print("materia:", materia.__str__())

except Exception as e:
    print("Error al abrir el archivo:", e)

finally:
    file1.close()  # Cierra el archivo


#3. Lea el archivo usuarios.txt y rellene el arreglo de usuarios con la información del archivo.
try:
    file_usuario = open("usuarios.txt", "r")
    lineas2 = file_usuario.readlines()
    
    for i in range(len(lineas2)):
        if (i != 0):
            linea_usuario = lineas2[i].strip();
            
            id = linea_usuario.split(",")[0]
            nombre_completo = linea_usuario.split(",")[1]
            cc = linea_usuario.split(",")[2]
            email = linea_usuario.split(",")[3]
            fecha_nacimiento = linea_usuario.split(",")[4]
            usuario = Usuario(id, nombre_completo, cc, email, fecha_nacimiento)
            sistema.agregar_usuario(usuario)
            #print(f"ID: {id}, Nombre Completo: {nombre_completo}, CC: {cc}, Email: {email}, Fecha de Nacimiento: {fecha_nacimiento}")
            
except Exception as e:
    print("Erros al abrir el archivo", e)

finally:
    file_usuario.close()
       

#4. Lea el archivo registros_academicos.txt y rellene el arreglo de registros de matricula con la información del archivo.
try:
    file_registros_academicos = open("registros_academicos.txt" , "r")
    lineas_registro = file_registros_academicos.readlines()
    cantidad_registros = len(lineas_registro)
    for i in range(cantidad_registros):
        if (i != 0):
            lineas_reg = lineas_registro[i].strip(); 
            #REG001,U098,U048,CAL16,2023-2
            id_reg = lineas_reg.split(",")[0]
            id_docente = lineas_reg.split(",")[1]
            id_estudiante = lineas_reg.split(",")[2]
            id_materia = lineas_reg.split(",")[3]
            periodo = lineas_reg.split(",")[4]
            registro_matricula = RegistroMatricula(id_reg, id_docente, id_estudiante, id_materia, periodo, cantidad_registros)
            sistema.agregar_registro(registro_matricula)
            #print(f"Id registro: {id_reg}, Id docente: {id_docente}, Id estudiante: {id_estudiante}, Id materia: {id_materia}, Periodo: {periodo}")

except Exception as e:
    print("Archivo no encontrado", e)
finally:
    file_registros_academicos.close()

#5. Lea el archivo calificaciones_academicas.txt y rellene el arreglo de calificaciones de cada registro de matrícula con la información del archivo.
try:
    file_calificaionesAc = open("calificaciones_academicas.txt", "r")
    lineas_calificacionesAc = file_calificaionesAc.readlines()
    
    for i in range(len(lineas_calificacionesAc)):
        if (i != 0):
            lineas_calificaciones = lineas_calificacionesAc[i].strip()
            #REG001,15:3.85-27:0.06-20:1.86-22:3.34-16:4.76
            reg_id = lineas_calificaciones.split(",")[0]
            print(f"\n{reg_id}:")
            porcentaje_notas = lineas_calificaciones.split(",")[1]
            listado_notas = porcentaje_notas.split("-")
            for j in range(len(listado_notas)):
                porc = listado_notas[j].split(":")[0]
                nota = listado_notas[j].split(":")[1]
                calificacion = Calificacion(int(porc), float(nota))
                registro_matricula.agregar_calificacion(calificacion) 
                #print(f"pos{j} > nota:{nota} - {porc}%")
           
except Exception as e:
    print("Error al abrir el archivo calificaciones_academicas.txt")
    
finally:
    file_calificaionesAc.close()


#6. Lea el archivo calificaciones_2024_2.txt y rellene el arreglo de calificaciones de cada registro de matrícula con la información del archivo.
try:
    print("\n ___________________________")
    print("| calificaciones_2024_2.txt |")
    print(" ---------------------------")
    file_calificaciones_semestre = open("calificaciones_2024_2.txt", "r")
    lineas_calificaciones_semestre = file_calificaciones_semestre.readlines()
    
    for i in range(len(lineas_calificaciones_semestre)):
        if (i != 0):
            lineas_calificaciones = lineas_calificaciones_semestre[i].strip()
            #2024-2,12345678,MAT001,13579135,10:2.7-10:1.8-10:1.86-10:4.11-10:2.73-10:2.24-10:1.58-10:0.75-10:2.38-10:1.44
            porcentaje_notas = lineas_calificaciones.split(",")[4]
            listado_notas = porcentaje_notas.split("-")
            for j in range(len(listado_notas)):
                porc = listado_notas[j].split(":")[0]
                nota = listado_notas[j].split(":")[1]
                calificacion = Calificacion(int(porc), float(nota))
                registro_matricula.agregar_calificacion(calificacion) 
                #print(f"pos{j} > nota:{nota} - {porc}%")
           
except Exception as e:
    print(f"Error al abrir el archivo calificaciones_2024_2.txt: {e}")
    
finally:
    file_calificaciones_semestre.close()

#7. Utilice el método toReportByEstudiante() y genere un reporte del estudiante con el historial de notas. El archivo debe tener la información ilustrada en 
# la tabla, donde Nota Final debe ser calculada utilizando el valor y la ponderación de las calificaciones. Y el campo Estado Final debe ser “Aprobó” si la 
# nota final es mayor o igual a 3.0, y “Reprobó” si la nota final es menor a 3.0. Además, el archivo debe estar ordenado por el periodo (menor a mayor). El valor 
# de la Nota Final tiene que estar formateado para que no registre más de 2 decimales.
sistema.toReportByEstudiante("42313135")

