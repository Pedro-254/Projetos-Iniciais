#include <stdlib.h>
#include <string.h>
#include <stdio.h>


int main(void) {
  char palavra_secreta[46];
  char char_achados[46];
  printf("Entre com a palavra secreta:");
  scanf("%s",palavra_secreta);
  int i,j;

  //Tamanho da palavra com "-"
  char palavra[46];
  for(i=0;i<strlen(palavra_secreta);i++){
    palavra[i] = 45;
  }
  
  //Partes do boneco 
   //  O
   // /|\
   // / \
  
  char boneco[6][18];
  strcpy(boneco[0],"\t  O\n");
  strcpy(boneco[1],"\t /");
  strcpy(boneco[2],"|");
  strcpy(boneco[3],"\\ \n");
  strcpy(boneco[4],"\t /");
  strcpy(boneco[5]," \\ \n");


  int stop = 0;
  int erros = 0;
  int acertos = 0;
  // Jogo
  while (stop == 0){
    printf("\e[1;1H\e[2J");
    // Printar personagem
    for(i = 0; i<erros;i++){
      printf("%s",boneco[i]);
    }

    // Printar caracteres
    for(i = 0; i < strlen(char_achados); i++){
      for(j = 0; j<strlen(palavra_secreta);j++){
        if(char_achados[i]==palavra_secreta[j]){
          palavra[j] = char_achados[i];
        }
      }
    }
    printf("\n %s",palavra);

    // Printar resultado
    if (erros == 6){
      printf("\e[1;1H\e[2J");
      // Printar personagem
      for(i = 0; i<erros;i++){
        printf("%s",boneco[i]);
      }
      printf("\nPalavra secreta: %s\n",palavra_secreta);
      printf("Você perdeu!");
      stop = 1;
    }
    else if(acertos == strlen(palavra_secreta)){
      printf("\e[1;1H\e[2J");
      // Printar personagem
      for(i = 0; i<erros;i++){
        printf("%s",boneco[i]);
      }
      printf("\nPalavra secreta: %s\n",palavra_secreta);
      printf("Você ganhou!");
      stop = 1;
    }

    // Procura se letra in palavra_secreta
    if (stop == 1){}
    else{
    printf("\nLetra:\n");
    char letra;
    scanf(" %c",&letra);
    int resultado = 0;
    for (i = 0; i<strlen(palavra_secreta);i++){      
        if (letra != palavra_secreta[i]){
          resultado = -1;
        }
        else{
          i = strlen(char_achados);
          resultado = 1;
          char_achados[i] += letra;
          break;
    }
      }
    // Registra o resultado
    if (resultado == 1){
      acertos = 0;
      for(i = 0; i<strlen(char_achados); i++){
        for(j = 0; j<strlen(palavra_secreta); j++){
          if(char_achados[i] == palavra_secreta[j]){
            acertos += 1;
          }
        }
      }
    }
    else if(resultado == -1){
      erros += 1;
    }

  }
}
}
