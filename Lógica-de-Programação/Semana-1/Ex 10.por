programa {

  funcao inicio() {
      
    inteiro num, contador = 0

    
    para (inteiro i = 0; i < 5; i++){

      escreva("Digite um número e exibiremos o seu fatorial: ")
      leia(num)
      
      se (num > 0){

        contador++

      }
    }

    escreva("Foram digitados ", contador, " números inteiros!")

  }
}
