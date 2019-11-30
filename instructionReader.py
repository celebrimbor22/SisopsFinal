import os
import sys

def parse_instructions():
    #lista de instrucciones
    list_instrucions = []
    # archivo de instrucciones
    print('EL ARCHIVO DEBE DE ESTAR EN LA MISMA CARPETA')
    archivo = input('Dame el nombre del archivo: ')
    archivo +='.txt'
    #direccion de archivo de instrucciones
    arch_path = archivo.rstrip('\r')

    # verificar que el archivo existe
    if not os.path.isfile(arch_path):
        print('No se encontro el archivo, saliendo.')

        exit()

    with open(arch_path.rstrip('\r')) as file:
        # lee todas las líneas del archivo y las almacena en un arreglo con nombre lines
        instruccion = file.read().splitlines()

        for i, instruccion in enumerate(instruccion):
            # separa las líneas de instrucción en sus parámetros
            accion = instruccion.split(' ')
            # procesamiento de la instrucción dependiendo del comando proporcionado por la primera letra
            if accion[0] == 'A':
                # revisa que la instrucción cuente con el número de parámetros requeridos
                if(len(accion) < 4):
                    print('El comando de la línea ', i+1, 'requiere 4 parámetros.')
                    print('El programa finaliza su ejecución por encontrar un comando inválido.')
                    exit()
                instr_list = [accion[0]]
                # convierte a entero los parámetros del comando
                try:
                    instr_list.append(int(accion[1]))
                    instr_list.append(int(accion[2]))
                    instr_list.append(int(accion[3]))
                except ValueError:
                    print('Hay uno o más parámetros incorrectos en la instrucción que está en la línea', i+1)
                    print('El programa finaliza su ejecución por encontrar un parámetro inválido.')
                    exit()
            elif accion[0] == 'L':
                # revisa que la instrucción cuente con el número de parámetros requeridos
                if(len(accion) < 2):
                    print('El comando de la línea ', i+1, 'requiere 2 parámetros.')
                    print('El programa finaliza su ejecución por encontrar un comando inválido.')
                    exit()
                instr_list = [accion[0]]
                # convierte a entero los parámetros del comando
                try:
                    instr_list.append(int(accion[1]))
                except ValueError:
                    print('Hay uno o más parámetros incorrectos en la instrucción que está en la línea', i+1)
                    print('El programa finaliza su ejecución por encontrar un parámetro inválido.')
                    exit()
            elif accion[0] == 'C':
                instr_list = [accion[0]]
                # vuelve a juntar el arreglo de parámetros para imprimir el comentario como salida
                instr_list.append(' '.join(accion[1::]))
            elif accion[0] == 'F':
                instr_list = [accion[0]]
            elif accion[0] == 'P':
                # revisa que la instrucción cuente con el número de parámetros requeridos
                if(len(accion) < 3):
                    print('El comando de la línea ', i+1, 'requiere 3 parámetros.')
                    print('El programa finaliza su ejecución por encontrar un comando inválido.')
                    exit()
                instr_list = [accion[0]]
                # convierte a entero los parámetros del comando
                try:
                    instr_list.append(int(accion[1]))
                    instr_list.append(int(accion[2]))
                except ValueError:
                    print('Hay uno o más parámetros incorrectos en la instrucción que está en la línea', i+1)
                    print('El programa finaliza su ejecución por encontrar un parámetro inválido.')
                    exit()
            elif accion[0]== 'E':
                instr_list = [accion[0]]
            else:
                # instrucción inválida
                print("Instrucción desconocida en la línea ", i+1)
                print('El programa finaliza su ejecución por encontrar un comando desconocido.')
                exit()
            list_instrucions.append(instr_list)
        return list_instrucions