def eh_primo(i):

    if i <= 1:

        return False

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:

            return False

    return True

intervalo = int(input("Digite um número e será impresso todos os números primos até o algarimos digitado: "))
intervalo += 1

for i in range(intervalo):
    if eh_primo(i):
        print(i)