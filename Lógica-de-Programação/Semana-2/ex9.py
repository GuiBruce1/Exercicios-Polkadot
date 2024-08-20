def contador_de_Letras(frase, letra):
  
  contador = 0

  for caractere in frase:
    if caractere.lower() == letra.lower():
      contador += 1
  return contador

frase = input("Digite uma frase: ")

letra = input("Digite a letra que deseja contar: ")

resultado = contador_de_Letras(frase, letra)

print("A letra", letra, "aparece", resultado, "vezes na frase.")