snacks = {'1':4.0, '2':4.5, '3':5.0, '4':2.0, '5':1.5}
values = input().split()
print(f'Total: R$ {snacks[values[0]]*float(values[1]):.2f}')
