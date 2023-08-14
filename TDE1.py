print('1. Escreva um programa que imprima 2 números de sua escolha e que depois imprima a soma, a subtração, multiplicação, divisão, divisão inteira, o resto da divisão do maior pelo menor e coloque na mensagem a palavra resto ao invés de símbolo %.')


numero1 = int(input('Escolha o primeiro número:\n'))
numero2 = int(input('Escolha o segundo número:\n'))
print(f'Os números escolhidos foram {numero1} e {numero2}.')
print(f'A soma entre eles é {numero1+numero2}.')
print(f'Subtraindo o {numero1} de {numero2} o resultado é: {numero2-numero1}.')
print(f'O produto deles é: {numero1*numero2}.') 
if(numero1>numero2):
    print(f'A divisão de {numero1} por {numero2} é: {numero1/numero2}\nSua divisão inteira é: {numero1//numero2} e o resto da divisão é: {numero1%numero2}.')
elif(numero2>numero1):
    print(f'A divisão de {numero2} por {numero1} é: {numero2/numero1}\nSua divisão inteira é: {numero2//numero1} e o resto da divisão é: {numero2%numero1}.')


print('\n2. Faça um programa que peça as 4 notas bimestrais e mostre a média do aluno.')

nota1 = float(input('Insira a primeira nota:\n'))
nota2 = float(input('Insira a segunda nota:\n'))
nota3 = float(input('Insira a terceira nota:\n'))
nota4 = float(input('Insira a quarta nota:\n'))

media = ((nota1 + nota2 + nota3 + nota4)/4)

print(f'A média do aluno é: {media}.')


print('\n3. Crie um script Python que leia o dia, mês e ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.')

dia = int(input('Digite o dia do seu nascimento\n'))
mes = int(input('Digite o mês do seu nascimento\n'))
ano = int(input('Digite o ano do seu nascimento\n'))

if (mes == 2 and (dia < 1 or dia > 29)):
    print('Data inválida')
elif ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia < 1 or dia > 30)):
    print('Data inválida')
elif ((mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and (dia < 1 or dia > 31)):
    print('Data inválida')
else:
    print(f'A data de nascimento é {dia:02}/{mes:02}/{ano:02}.')


print('\n4. Organize os números 2,3,4,5,10,12 para obter a saída (resposta) 18 em uma única expressão:')

resultado = 4 - 2 + (3 + 5) * (12 - 10)

print(f'A expressão utilizada foi 4 - 2 + (3 + 5) * (12 - 10) onde o resultado é: {resultado}.')

