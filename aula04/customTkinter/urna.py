import customtkinter as ctk

numeroVotosCand1 = 0
numeroVotosCand2 = 0
def contaVotos1():
    global numeroVotosCand1
    numeroVotosCand1 = numeroVotosCand1 + 1
    return numeroVotosCand1

def contaVotos2():
    global numeroVotosCand2
    numeroVotosCand2 = numeroVotosCand2 + 1
    return numeroVotosCand2
    
def resultado():
    if numeroVotosCand1 > numeroVotosCand2:
        resposta.configure(text = f"Candidato 1 ganhou por {numeroVotosCand1 - numeroVotosCand2} votos de diferença")
    elif numeroVotosCand1 == numeroVotosCand2:
        resposta.configure(text = f"Empate entre os candidatos! cada candidato recebeu {numeroVotosCand2} votos!")
    else:
        resposta.configure(text = f"Candidato 2 ganhou por {numeroVotosCand2 - numeroVotosCand1} votos de diferença")


ctk.set_appearance_mode("system")

tela = ctk.CTk()
tela.geometry("500x500")
tela.title("Urna")

titulo = ctk.CTkLabel(tela, text=("Escolha o seu eleitor"))
titulo.pack(pady = 25)

candidato1 = ctk.CTkLabel(tela, text=("Candidato X"))
candidato2 = ctk.CTkLabel(tela, text=("Candidato y"))
candidato1.pack()
candidato2.pack()

botao1 = ctk.CTkButton(tela,text="Votar em candidato1", command= contaVotos1 )
botao1.pack()

botao2 = ctk.CTkButton(tela,text="Votar em candidato2", command= contaVotos2 )
botao2.pack(pady = 25)

botao3 = ctk.CTkButton(tela,text="Resultado", command= resultado, fg_color= "green" )
botao3.pack()

resposta = ctk.CTkLabel(tela, text="")
resposta.pack(pady = 20)



tela.mainloop()