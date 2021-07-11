product1 = input().split(" ")
product2 = input().split(" ")
calculation = (float(product1[1])*float(product1[2])+float(product2[1])*float(product2[2]))
print(f'VALOR A PAGAR: R$ {calculation:0.2f}')