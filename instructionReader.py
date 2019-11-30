import os

def parse_instructions():
    instructions = []
    # archivo de instrucciones
    user_input = input('Ingresa el archivo de instrucciones: ')
    file_path = user_input.rstrip('\r')

    # verificar que el archivo existe
    if not os.path.isfile(file_path):
        print('El archivo especificado no se encontró en el directorio.')
        print('El programa finaliza su ejecución tras no encontrar el archivo de entrada.')

        exit()
    
    with open(file_path.rstrip('\r')) as file:
        # lee todas las líneas del archivo y las almacena en un arreglo con nombre lines
        lines = file.read().splitlines()
        
        for i, line in enumerate(lines):
            # separa las líneas de instrucción en sus parámetros
            words = line.split(' ')
            # procesamiento de la instrucción dependiendo del comando proporcionado por la primera letra
            if words[0] == 'A':
                # revisa que la instrucción cuente con el número de parámetros requeridos
                if(len(words) < 4):
                    print('El comando de la línea ', i+1, 'requiere 4 parámetros.')
                    print('El programa finaliza su ejecución por encontrar un comando inválido.')
                    exit()
                instruction = [words[0]]
                # convierte a entero los parámetros del comando
                try:
                    instruction.append(int(words[1]))
                    instruction.append(int(words[2]))
                    instruction.append(int(words[3]))
                except ValueError:
                    print('Hay uno o más parámetros incorrectos en la instrucción que está en la línea', i+1)
                    print('El programa finaliza su ejecución por encontrar un parámetro inválido.')
                    exit()
            elif words[0] == 'P':
                # revisa que la instrucción cuente con el número de parámetros requeridos
                if(len(words) < 3):
                    print('El comando de la línea ', i+1, 'requiere 3 parámetros.')
                    print('El programa finaliza su ejecución por encontrar un comando inválido.')
                    exit()
                instruction = [words[0]]
                # convierte a entero los parámetros del comando
                try:
                    instruction.append(int(words[1]))
                    instruction.append(int(words[2]))
                except ValueError:
                    print('Hay uno o más parámetros incorrectos en la instrucción que está en la línea', i+1)
                    print('El programa finaliza su ejecución por encontrar un parámetro inválido.')
                    exit()
            elif words[0] == 'L':
                # revisa que la instrucción cuente con el número de parámetros requeridos
                if(len(words) < 2):
                    print('El comando de la línea ', i+1, 'requiere 2 parámetros.')
                    print('El programa finaliza su ejecución por encontrar un comando inválido.')
                    exit()
                instruction = [words[0]]
                # convierte a entero los parámetros del comando
                try:
                    instruction.append(int(words[1]))
                except ValueError:
                    print('Hay uno o más parámetros incorrectos en la instrucción que está en la línea', i+1)
                    print('El programa finaliza su ejecución por encontrar un parámetro inválido.')
                    exit()
            elif words[0] == 'C':
                instruction = [words[0]]
                # vuelve a juntar el arreglo de parámetros para imprimir el comentario como salida
                instruction.append(' '.join(words[1::]))
            elif words[0]== 'E':
                instruction = [words[0]]
            elif words[0] == 'F':
                instruction = [words[0]]
            else: 
                # instrucción inválida
                print("Instrucción desconocida en la línea ", i+1)
                print('El programa finaliza su ejecución por encontrar un comando desconocido.')
                exit()
            instructions.append(instruction)
        return instructions
