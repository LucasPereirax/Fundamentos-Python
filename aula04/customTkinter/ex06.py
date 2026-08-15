import customtkinter as ctk

def gerarRelatorio():
    potenciaKVH = (float(potencia.get())/1000)
    consumoDiario = (potenciaKVH * float(horas.get()))
    resposta.configure(text = f"Nome do equipamento: {nome.get()}\nSetor: {setor.get().upper()}\nPotência: {potenciaKVH:.2f}\nConsumo diário: {consumoDiario:.2f}")

tela = ctk.CTk()
tela.geometry("500x500")
tela.title("ex06")

titulo = ctk.CTkLabel(tela, text=("Desafio: painel de equipamento"))
titulo.pack()

nome = ctk.CTkEntry(tela,placeholder_text="Digite o nome")
nome.pack(pady = 25)

setor = ctk.CTkEntry(tela,placeholder_text="Digite o setor")
setor.pack()

potencia = ctk.CTkEntry(tela,placeholder_text="Digite o valor da potencia")
potencia.pack(pady = 25)

horas = ctk.CTkEntry(tela,placeholder_text="Digite o valor em horas")
horas.pack()

relatorio = ctk.CTkButton(tela,text="Gerar relatorio", command= gerarRelatorio )
relatorio.pack()

resposta = ctk.CTkLabel(tela,text="")
resposta.pack()


tela.mainloop()