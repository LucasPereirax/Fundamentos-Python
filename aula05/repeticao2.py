senha_Digitada = input("Digite a senha: ")
senha = "Senai@403"

while senha_Digitada != senha:
    print("Senha incorreta, tente novamente:")
    senha_Digitada = input("Digite a senha: ")

print("Acesso liberado!")
