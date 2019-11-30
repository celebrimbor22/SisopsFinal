import sys
from instructionReader import parse_instructions
import instructions

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
parsed_instructions = parse_instructions()
for instruction in parsed_instructions:
    print("\n", ' '.join(str(x) for x in instruction), sep="")
# Add calls to each instruction
    if instruction[0] == 'P':
        instructions.P(instruction[1], instruction[2])
    elif instruction[0] == 'A':
        instructions.A(instruction[1], instruction[2], instruction[3])
    elif instruction[0] == 'E':
        instructions.E()