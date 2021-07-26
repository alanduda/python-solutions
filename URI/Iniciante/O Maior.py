def bigger(number1, number2):
    return (number1+number2+abs(number1-number2))/2

numbers = input().split(' ')
x = bigger(int(numbers[0]), int(numbers[1]))
bigger = bigger(x, int(numbers[2]))
print(f'{bigger:0.0f} eh o maior')
