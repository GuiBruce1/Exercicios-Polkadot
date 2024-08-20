#Não foi especificado a calssificação de 15 e 30 graus.

temp = float(input("Digite a temperatura atual: "))

if temp > 30:
    print("Está quente!")
elif temp >= 15:
    print("Está agradável!")
else:
    print("Está frio!")