produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
preco = float(input("Digite o nome do produto: "))

total = quantidade * preco

print(f"Produto: {produto}\nQuantidade: {quantidade}\nTotal: R${total:.2f}")