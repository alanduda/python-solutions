values = input().split(' ')
A = float(values[0]); B = float(values[1]); C = float(values[2])
delta = (B**2) - (4*A*C)
if( delta >= 0 and A != 0.0):
    print((-B + delta**0.5))
    print(f'R1 = {((-B + delta**0.5)/(2*A)):0.5f}\nR2 = {((-B - delta**0.5)/(2*A)):0.5f}')
else:
    print('Impossivel calcular')