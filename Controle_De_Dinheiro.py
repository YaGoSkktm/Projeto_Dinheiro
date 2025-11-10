num = int(input("Qual número você deseja saber a taboada? "))
num2 = int(input(f'você quer saber a taboada de {num} até qual número? '))
for i in range(1, num2+1):
    print(f'O resultado de {i} X {num} é igual: {i*num}')