def celsius_para_fahrenheit(c):
    conversao = c * 9 / 5 + 32
    return conversao

temperatura = float(input("Digite a temperatura em C°: "))
convertida = celsius_para_fahrenheit(temperatura)

print(f" O valor {temperatura}° convertido em fahrenheit é {convertida:.1f}°")