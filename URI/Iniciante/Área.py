values = input().split(' ')
print(f'TRIANGULO: {((float(values[0])*float(values[2]))/2):0.3f}\nCIRCULO: {(3.14159*float(values[2])**2):0.3f}\nTRAPEZIO: {(((float(values[0])+float(values[1]))*float(values[2]))/2):0.3f}\nQUADRADO: {(float(values[1])**2):0.3f}\nRETANGULO: {(float(values[0])*float(values[1])):0.3f}')
