a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))
print()

if (a+b) <= c or (b+c) <= a or (c+a) <= b:
    print("Isso não é um triângulo")
else:
    if a==b==c:
        print("Triângulo equilátero")
    elif a == b or b == c or a == c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")

