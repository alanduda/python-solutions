number = float(input())
if( number >= 0 and number <= 100):
    if( number<=25 ):
        print('Intervalo [0,25]')
    if( number>25 and number<=50):
        print('Intervalo (25,50]')
    if( number>50 and number<=75):
        print('Intervalo (50,75]')
    if( number>75 and number<=100):
        print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
    