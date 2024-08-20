def par_impar(num):

    if num % 2 == 0:
        return "par"
    else:
        return "ímpar"
    
num = int(input("Digite um número e diremos se ele é par ou ímpar: "))

resultado = par_impar(num)

print("O número é", resultado)
    