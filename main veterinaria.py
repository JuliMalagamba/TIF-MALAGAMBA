

# Deberá crear una aplicación de consola que simulara un “sistema de gestión de
# pacientes de una veterinaria”, que permita:
# - Registrar un paciente detallando su nombre, sexo, edad aproximada, 
# especie(canino/felino), rasgos, enfermedad, nombre dueño, 
# numero de contacto.
# - Consultas de registros.
# - Modificar el registro de un paciente.
# - Eliminar el registro de un paciente.
# - Al finalizar, el programa deberá mostrar reportes de la cantidad de pacientes 
# registrados y eliminados

from recursos.modulos.funciones import registrarPaciente, mostrarRegistros, eliminarRegistro

def main():
    registrosVeterinarios={} #agenda
    identificador=0 #inicia el contador para crear los ID
    registrosEliminados=0 #inicia el contador para los ID eliminados

    print("BIENVENIDO AL SISTEMA DE PACIENTES DE LA CLÍNICA VETERINARIA")

    while True: # mientras sea verdadero mostrara el menu de opciones, recibe un numero entero
        opcionIngresada= int(input("""
OPCIONES:
                          
1) REGISTRAR UN NUEVO PACIENTE
2) CONSULTAR EL REGISTRO DE PACIENTE/S
3) MODIFICAR UN REGISTRO
4) ELIMINAR UN REGISTRO
5) SALIR Y MOSTRAR EL REPORTE FINAL DE PACIENTES

¿ QUÉ DESEA HACER ? :  """))
        
        match opcionIngresada:
            case 1:
                print("""
REGISTRAR NUEVO PACIENTE
                      """)
                datosPaciente={} #crea un diccionario nuevo con los datos del paciente
                datosPaciente["nombre"]= input("Nombre del paciente: ")
                datosPaciente["edad"]=input("Edad: ")
                datosPaciente["sexo"]=input("Sexo: ")
                datosPaciente["especie"]=input("Especie: ")
                datosPaciente["rasgos"]=input("Rasgos: ")
                datosPaciente["enfermedad"]=input("Enfermedad o motivo de consulta: ")
                datosPaciente["dueño"]=input("Nombre del dueño: ")
                datosPaciente["telefono"]=input("Teléfono de contacto: ")
                identificador=identificador+1 #se incrementa el contador en 1 para cada nuevo registro ingresado
                print(registrarPaciente(identificador, datosPaciente, registrosVeterinarios)) #invoca la funcion

            case 2:
                opcionConsultar=input("""
CONSULTAR REGISTRO DE PACIENTE/S
                                  
Ingrese (1) si quiere consultar por un registro en especial, 
Ingrese (2) si quiere consultar el registro general de pacientes.

¿ QUÉ DESEA HACER ? :  """)
                if opcionConsultar=="1":
                    idConsultar=int(input("""
Ingrese el ID del registro que quiere consultar: """))
                    if idConsultar in registrosVeterinarios:
                        paciente=registrosVeterinarios[idConsultar]
                        print(mostrarRegistros(idConsultar, paciente)) #invoca funcion
                    else: print("""
ID NO ENCONTRADO.""")
                elif opcionConsultar=="2":
                    for identificador in registrosVeterinarios: #bucle para recorrer agenda
                        paciente=registrosVeterinarios[identificador]
                        print(mostrarRegistros(identificador,paciente)) #invoca funcion
                    if len(registrosVeterinarios)==0:
                        print("""
REGISTRO DE PACIENTES VACIO.""")
                else: print("""
OPCIÓN INGRESADA INVÁLIDA. """)
            case 3:
                opcionModificar=int(input("""
MODIFICAR REGISTRO DE PACIENTE

Ingrese el ID del registro que desea modificar: """))
                if opcionModificar in registrosVeterinarios:
                    paciente=registrosVeterinarios[opcionModificar]
                    print("""
Ingrese las modificaciones 
                  """)
                    paciente["nombre"]= input("Nombre del paciente: ")
                    paciente["edad"]= input("Edad: ")
                    paciente["sexo"]= input("Sexo: ")
                    paciente["especie"]=input("Especie: ")
                    paciente["rasgos"]=input("Rasgos: ")
                    paciente["enfermedad"]= input("Enfermedad o motivo de consulta: ")
                    paciente["dueño"]=input("Nombre del dueño: ")
                    paciente["telefono"]=input("Teléfono de contacto: ")
                    print("""
REGISTRO MODIFICADO CON ÉXITO. """)
                     
                else: print("""
ID NO ENCONTRADO.""")
            case 4:
                idIngresado= int(input("""
ELIMINAR REGISTRO DE PACIENTE
                               
Ingrese el ID del registro que desea eliminar: """))
                if idIngresado in registrosVeterinarios:
                    registrosEliminados= registrosEliminados+1
                    print(eliminarRegistro(registrosVeterinarios, idIngresado))
                else: print("""
ID NO ENCONTRADO""")
            case 5:
                print(f"""
REPORTE FINAL

CANTIDAD DE REGISTROS VIGENTES: {len(registrosVeterinarios)}
CANTIDAD DE REGISTROS ELIMINADOS: {registrosEliminados} 
                  """)
                break
            case _: print("""
OPCIÓN INGRESADA INVÁLIDA, INTENTE NUEVAMENTE""")
        
    print("GRACIAS POR UTILIZAR EL REGISTRO VIRTUAL DE PACIENTES VETERINARIOS")


if __name__=="__main__":
    main()
