X = input().split(' ')
Y = input().split(' ')
distance = ((float(Y[0]) - float(X[0]))**2 + (float(Y[1]) - float(X[1]))**2)**(1/2)
print(f'{distance:0.4f}')
