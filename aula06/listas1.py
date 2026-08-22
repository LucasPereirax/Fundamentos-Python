#criando a lista
alunos = ["Lucas", "Dany", "Gabriela", "Beatriz"]

#mostrando a lista
print(alunos)

#acessando um item na lista
print(alunos[2])

#adicionando um item na lista
alunos.append("Teste")
print(alunos)

#remover item da lista
alunos.remove(alunos[0])
print(alunos)

#incluir item em uma posição específica
alunos.insert(0, "João")
print(alunos)

#usando um for para percorrer a lista
for aluno in alunos:
    print(aluno)

#Atualizando um item da lista
alunos[3] = "Lucas"
print(alunos)

#Atualizando por um nome específico
alunos[alunos.index("Dany")] = "Beatriz"
print(alunos)

#Tamanho da lista
print(len(alunos))