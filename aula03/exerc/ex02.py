idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
    
    if idade == 16 or idade == 17:
        anos_restantes = 18 - idade
        print(f"Faltam {anos_restantes} ano(s) para você completar 18 anos.")
