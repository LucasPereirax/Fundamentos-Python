nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1+nota2)/2

if media >=6:
    print(f"Aprovado! com nota final {media:.1f}")
elif media <= 4 and media >=5.9:
    print(f"Recuperação! com nota final {media:.1f}")
else:
    print(f"Reprovado! com nota final {media:.1f}")