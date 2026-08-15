def medidas(base, altura):
    area = base*altura
    perimetro = 2* (base+altura)
    return area, perimetro

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

resultadoArea, resultadoPerimetro = medidas(base, altura)

print(f"A área é: {resultadoArea:.2f}")
print(f"O perímetro é: {resultadoPerimetro:.2f}")