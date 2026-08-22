import random

numero_secreto = random.randint(0, 100)
chute = int(input("Digite um número: "))
tentativas = 0
while chute != numero_secreto:
    tentativas+=1
    if chute < numero_secreto:
        print("Tente um número maior!")
    else:
        print("Tente um número menor!")
    chute = int(input("Digite um número: "))

print("Achou!")
