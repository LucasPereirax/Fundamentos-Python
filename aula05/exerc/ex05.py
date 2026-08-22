senha = input("Digite a senha do usuario: ")
senha_correta = "python123"

while senha != senha_correta:
    print("Senha incorreta, digite novamente a senha")
    senha = input("Digite a senha do usuario: ")
print("Acesso liberado! ")
