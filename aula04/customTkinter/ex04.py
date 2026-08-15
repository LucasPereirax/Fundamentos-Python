import customtkinter as ctk

def conversao():
    metros = float(num1.get())
    centimetros = metros * 100
    resultado.configure(text=(f"O valor convertido de {metros:.2f}m em centímetrosé {centimetros:.2f}cm"))

tela = ctk.CTk()
tela.geometry("500x500")
tela.title("ex04")

titulo = ctk.CTkLabel(tela, text=("Conversor de metros para centímetros"))
titulo.pack()

num1 = ctk.CTkEntry(tela,placeholder_text="Digite o valor em metros")
num1.pack(pady = 25)

calcular = ctk.CTkButton(tela,text="Calcular", command= conversao )
calcular.pack()

resultado = ctk.CTkLabel(tela,text="")
resultado.pack()

tela.mainloop()