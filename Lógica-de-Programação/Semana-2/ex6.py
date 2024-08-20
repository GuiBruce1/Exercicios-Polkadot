somatorio = 0
num = float(input("Insira números e exibiremos seu somatório. #Digite 0 para parar "))

while num != 0:

    somatorio += num
    num = float(input("insira o próximo número. #Digite 0 para parar "))

print("O somatório é: ", somatorio)