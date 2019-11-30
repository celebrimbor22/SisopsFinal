import sys
import os
import instructions

def read_instructions():
    #lista de instrucciones
    list_instrucions = []
    # archivo de instrucciones
    print('EL ARCHIVO DEBE DE ESTAR EN LA MISMA CARPETA')
    archivo = input('Dame el nombre del archivo: ')
    archivo +='.txt'
    #direccion de archivo de instrucciones
    arch_path = archivo.rstrip('\r')

    if not os.path.isfile(arch_path):
        print('No se encontro el archivo')
        sys.exit()

    with open(arch_path.rstrip('\r')) as file:
        # lee todas las líneas del archivo y las almacena en un arreglo con nombre lines
        instruccion = file.read().splitlines()
        for instruccion in enumerate(instruccion):
            # separa las líneas de instrucción en sus parámetros
            accion = instruccion.split(' ')
            com = accion[0]
            if com == 'A':
                # revisa que la instrucción cuente con el número de parámetros requeridos
                instr_list = [accion[0]]
                # convierte a entero los parámetros del comando
                try:
                    instr_list.append(int(accion[1]))
                    instr_list.append(int(accion[2]))
                    instr_list.append(int(accion[3]))
                except ValueError:
                    print('ERROR revisar archivo !!!!')
                    sys.exit()
            elif com == 'L':
                instr_list = [accion[0]]
                # convierte a entero los parámetros del comando
                try:
                    instr_list.append(int(accion[1]))
                except ValueError:
                    print('ERROR revisar archivo !!!!')
                    sys.exit()
            elif com == 'C':
                instr_list = [accion[0]]
                instr_list.append(' '.join(accion[1::]))
            elif com == 'F':
                instr_list = [accion[0]]
            elif com == 'P':
                instr_list = [accion[0]]
                try:
                    instr_list.append(int(accion[1]))
                    instr_list.append(int(accion[2]))
                except ValueError:
                    print('ERROR revisar archivo !!!!')
                    sys.exit()
            elif com== 'E':
                instr_list = [accion[0]]
            else:
                print('ERROR revisar archivo !!!!')
                sys.exit()
            list_instrucions.append(instr_list)
        return list_instrucions


print('******************************')
print('******************************')
print('******************************')
print('* Manejador de Memoria V 1.0 *')
print('******************************')
print('******************************')
print('******************************')

var = input('Dame la estrategia (fifo o lru): ')
while( var != 'fifo' and var != 'lru' ):
    print('Solo existe fifo o lru en este manejador')
    var = input('Dame la estrategia (fifo o lru): ')
print('La estrategia a urilizar es', var)

# Sets strategy on instructions
instructions.STRATEGY = True if var == 'fifo' else False
parsed_instructions = read_instructions()
for instruction in parsed_instructions:
    print("\n", ' '.join(str(x) for x in instruction), sep="")
# Add calls to each instruction
    if instruction[0] == 'P':
        instructions.P(instruction[1], instruction[2])
    elif instruction[0] == 'A':
        instructions.A(instruction[1], instruction[2], instruction[3])
    elif instruction[0] == 'E':
        instructions.E()
