numbers = input().split()
sortedNumbers = [int(x) for x in numbers]
sortedNumbers.sort()
print(f'{sortedNumbers[0]}\n{sortedNumbers[1]}\n{sortedNumbers[2]}\n\n{numbers[0]}\n{numbers[1]}\n{numbers[2]}')
