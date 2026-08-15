import customtkinter as ctk

#Funções:
def acao():
    texto = ctk.CTkLabel(tela, text="clicou")
    texto.pack()
    resposta.configure(text = "CLICOU!!!")
    return texto


ctk.set_appearance_mode("system")

tela = ctk.CTk()
tela.geometry("400x200")

tela.title("Teste de Botão")

titulo = ctk.CTkLabel(tela, text="APP PARA TESTE DE BOTAO", font=("Arial",22))
titulo.pack(pady = 20)

botao = ctk.CTkButton(tela,text="CLique aqui", command= acao )
botao.pack()

resposta = ctk.CTkLabel(tela, text="")
resposta.pack(pady = 20)


tela.mainloop()