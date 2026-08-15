print(f" -------------------------------------------------------------------------")
print(f"| Um restaurante quer estimar o custo mensal de energia de um equipamento.|")
print(f" -------------------------------------------------------------------------")

nome_equipamento = input("Digite o nome do equipamento: ").upper().strip()
potencia = float(input("Digite o valor em watts: "))
horas = float(input("Digite o valor de horas de uso: "))
dias = int(input("Digite os dias de uso no mês: "))
tarifa = float(input("Digite o valor da tarifa em R$/kWh: "))

potencia_kw = potencia /1000
consumoD = potencia_kw * horas
consumoT = consumoD *dias
custoTotal = consumoT * tarifa

semanas = (dias//7)
dias = dias%7

print(f" -------------------------------------------------------------------------")
print(f"|                           Relatório final                               |".upper())
print(f" -------------------------------------------------------------------------")

print(f"\nEquipamento: {nome_equipamento}\nPotência: {potencia_kw:.2f} kW\nConsumo diário: {consumoD} kWh\nConsumo total: {consumoT:.2f} kWh\nCusto total: R${custoTotal:.2f}\nPeríodo: {semanas} semanas e {dias} dia\n {type(consumoT)}>")