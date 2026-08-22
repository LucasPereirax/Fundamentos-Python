alunos = int(input("Digite a quantidade de alunos: "))
while alunos <= 0 :
    print("Essa quantidade não é permitida!")
    alunos = int(input("Digite a quantidade de alunos: "))
    
total = 0
for notas in range(1,alunos + 1):
    recebe_notas = float(input(f"Digite a nota do aluno {notas}: "))
    total += recebe_notas
media = total/alunos
print(f"Média final: {media:.2f}")