"""
Crie um programa com uma função que receba dois números e imprima na tela a soma deles
"""
def soma(num1, num2):
    resultado = num1 + num2
    print(f"O resultado da soma de {num1} + {num2} = {resultado}")

primeroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))
soma(primeroNumero, segundoNumero)