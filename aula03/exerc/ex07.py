nome = input("Digite seu nome: ").strip().title()
idade = int(input("Digite sua idade: "))
valor_inteiro = float(input("Digite o valor em R$: "))
quantidade = int(input("Digite a quantidade de ingressos: "))
estudante = input("Você é estudante? (s/n): ")

if idade <= 12:
    faixa = "INFANTIL"
elif idade >= 13 and idade <= 59:
    faixa = "ADULTO"
else:
    faixa = "IDOSO"

meia_entrada = idade <= 12 or idade >= 60 or estudante == "s"

tipo_ingresso = "MEIA-ENTRADA" if meia_entrada else "INTEIRA"
preco_unitario = valor_inteiro / 2 if meia_entrada else valor_inteiro

total = preco_unitario * quantidade

print(f"\n--- COMPROVANTE ---\nNome:\t{nome}\nFaixa:\t{faixa}\nTipo:\t{tipo_ingresso}\nQtd:\t{quantidade}\nTotal:\tR$ {total:.2f}")

if faixa == "INFANTIL":
    print("Aviso: O cliente deve estar acompanhado de um responsável.")
