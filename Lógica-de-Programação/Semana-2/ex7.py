lista_de_compras = []

while True:
    item = input("Digite um item para adicioná-lo à sua lista de compras! Digite 0 para encerrar. ")
    if item != '0':
        lista_de_compras.append(item)
    else:
        break

print(lista_de_compras)
