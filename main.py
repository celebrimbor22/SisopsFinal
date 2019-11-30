import sys
from instructionReader import parse_instructions
import instructions

#cambiar nombre de los archivos

def main():
    Estrategia = input('Dame la estrategia (fifo o lru): ')
    # print(Estrategia)
    if(Estrategia != 'fifo' and Estrategia != 'lru'):
        print('Solo se puede usar esas dos estrategias ')
        exit()
    print('Utilizando ', Estrategia, ' como estrategia de remplazo')

    #cAMBIAR NOMBRE DE INSTRUCTIONS
    instructions.strategy = True if Estrategia == 'fifo' else False

    parsed_instructions = parse_instructions()
    for instruction in parsed_instructions:
        print(' '.join(str(x) for x in instruction))
    # Add calls to each instruction
        if instruction[0] == 'P':
            instructions.P(instruction[1], instruction[2])
        elif instruction[0] == 'A':
            instructions.A(instruction[1], instruction[2], instruction[3])
        elif instruction[0] == 'E':
            instructions.E()

main()