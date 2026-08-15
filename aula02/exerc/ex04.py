tempo_total = int(input("Digite o tempo em segundos(s): "))

minutos = tempo_total//60
horas = minutos //60



print(tempo_total%60,"s")
print(minutos%60,"m")
print(horas,"h")