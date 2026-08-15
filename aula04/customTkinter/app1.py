#python -m pipe install customTkinter
import customtkinter as ctk

ctk.set_appearance_mode("system")

#Cria a janela principal do app
janela = ctk.CTk()

#Definir o tamanho da janela
janela.geometry("400x300")

#Criar um texto para incluir na janela
texto = ctk.CTkLabel(janela, text="===SENAI===")

#Inclui um texto na janela
texto.pack()

janela.mainloop()