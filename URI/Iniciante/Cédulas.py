value = int(input())
number = value
ballots100 = number//100; number = number - ((number//100) * 100)
ballots50 = number//50; number = number - ((number//50) * 50)
ballots20 = number//20; number = number - ((number//20) * 20)
ballots10 = number//10; number = number - ((number//10) * 10)
ballots5 = number//5; number = number - ((number//5) * 5)
ballots2 = number//2; number = number - ((number//2) * 2)
print(f'{value}\n{ballots100} nota(s) de R$ 100,00\n{ballots50} nota(s) de R$ 50,00\n{ballots20} nota(s) de R$ 20,00\n{ballots10} nota(s) de R$ 10,00\n{ballots5} nota(s) de R$ 5,00\n{ballots2} nota(s) de R$ 2,00\n{number} nota(s) de R$ 1,00')
