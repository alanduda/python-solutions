spots = input().split()
x = float(spots[0]); y = float(spots[1])
if(x == y and x == 0 ):
    print('Origem')
elif( x == 0 and y != 0 ):
    print('Eixo Y')
elif( y == 0 and x != 0 ):
    print('Eixo X')
elif( x > 0 and y > 0 ):
    print('Q1')
elif( x < 0 and y < 0 ):
    print('Q3')
elif( x > 0 and y < 0 ):
    print('Q4')
else:
    print('Q2')