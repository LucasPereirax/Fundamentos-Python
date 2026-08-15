num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+(soma), -(subtração), x(multiplicação), /(divisão)): ")

match operacao:
    case "+":
        resultado = num1+num2
        print(f"O resultado da operação {num1}{operacao}{num2} = {resultado:.2f}")
    case "-":
        resultado = num1-num2
        print(f"O resultado da operação {num1}{operacao}{num2} = {resultado:.2f}")
    case "x":
        resultado = num1*num2
        print(f"O resultado da operação {num1}{operacao}{num2} = {resultado:.2f}")
    case "/":
        if num2 == 0:
            print("Operação não autorizada")
        else:
            resultado = num1/num2
            print(f"O resultado da operação {num1}{operacao}{num2} = {resultado:.2f}")
    
    