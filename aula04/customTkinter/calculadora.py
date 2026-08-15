import customtkinter as ctk


def soma ():
    a = float(num1.get())
    b = float(num2.get())
    soma = a+b
    resultado.configure(text=(f"A soma de {a} + {b} = {soma:.2f}"))

def subtracao ():
    a = float(num1.get())
    b = float(num2.get())
    sub = a-b
    resultado.configure(text=(f"A subtração de {a} - {b} = {sub:.2f}"))

def divisao ():
    a = float(num1.get())
    b = float(num2.get())
    if b == 0:
        resultado.configure(text=(f"A divisão de {a} / {b} = não é possível"))
    else:
        div = a/b
        resultado.configure(text=(f"A divisão de {a} / {b} = {div:.2f}"))

def multiplicacao ():
    a = float(num1.get())
    b = float(num2.get())
    mult = a*b
    resultado.configure(text=(f"A multiplicação de {a} * {b} = {mult:.2f}"))

def apagarDados():
    num1.delete(0, "end")
    num2.delete(0, "end")
    resultado.configure(text="Resultado: ")

tela = ctk.CTk()
tela.geometry("500x500")
tela.title("Calculadora")

titulo = ctk.CTkLabel(tela, text=("Calculadora"))
titulo.pack()

num1 = ctk.CTkEntry(tela,placeholder_text="Primeiro número")
num2 = ctk.CTkEntry(tela,placeholder_text="Segundo número")
num1.pack()
num2.pack(pady = 15)

resultado = ctk.CTkLabel(tela, text="Resultado: ")
resultado.pack(pady = 20)


somar = ctk.CTkButton(tela,text="Somar", command= soma )
somar.pack()

subtrair = ctk.CTkButton(tela,text="Subtrair", command= subtracao )
subtrair.pack(pady = 25)

dividir = ctk.CTkButton(tela,text="Dividir", command= divisao)
dividir.pack()

multiplicar = ctk.CTkButton(tela,text="Multiplicar", command= multiplicacao)
multiplicar.pack(pady = 25)

apagar = ctk.CTkButton(tela,text="Apagar", fg_color="red", command=apagarDados)
apagar.pack(pady = 25)

tela.mainloop()