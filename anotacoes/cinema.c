#include <stdio.h>

// Funcao retorna true se a idade for maior ou igual a classificaçao
int podeAssistir(int idade, int classificacao) {
    return idade >= classificacao;
}

int main() {
    int opcaoFilme, quantidade;
    int idade;
    char estudante;
    float precoBase, precoFinal, total = 0;
    int ingressosValidos = 0;
    int classificacao;

    float precos[10] = {22, 25, 16, 14, 14, 18, 18, 28, 16, 14};

    // Mapa da sala (matriz)
    char sala[5][10];

    // Inicializa como livre
    for(int i = 0; i < 5; i++) {
        for(int j = 0; j < 10; j++) {
            sala[i][j] = 'O';
        }
    }

    // 10 assentos ocupados
    sala[0][2] = 'X'; 
    sala[1][5] = 'X'; 
    sala[2][7] = 'X'; 
    sala[3][1] = 'X'; 
    sala[4][9] = 'X'; 
    sala[0][8] = 'X'; 
    sala[2][3] = 'X'; 
    sala[3][6] = 'X'; 
    sala[1][0] = 'X';
    sala[4][4] = 'X'; 

    printf("=== CINEMA ===\n\n");

    // Menu com preços
    printf("Escolha o filme:\n");
    printf("1 - Todo Mundo em Panico (+16) - R$ %.2f\n", precos[0]);
    printf("2 - It: A Coisa (+16) - R$ %.2f\n", precos[1]);
    printf("3 - Como Treinar Seu Dragao (+10) - R$ %.2f\n", precos[2]);
    printf("4 - Divertidamente (Livre) - R$ %.2f\n", precos[3]);
    printf("5 - Shrek (Livre) - R$ %.2f\n", precos[4]);
    printf("6 - O Diabo Veste Prada 2 (+12) - R$ %.2f\n", precos[5]);
    printf("7 - As Branquelas (+12) - R$ %.2f\n", precos[6]);
    printf("8 - 365 Dias (+18) - R$ %.2f\n", precos[7]);
    printf("9 - As Guerreiras do Kpop (+10) - R$ %.2f\n", precos[8]);
    printf("10 - Toy Story (Livre) - R$ %.2f\n", precos[9]);

    printf("Opcao: ");
    scanf("%d", &opcaoFilme);

    // switch verifica todas as classes
    switch(opcaoFilme) {
        case 1:
        case 2:
            classificacao = 16;
            break;
        case 3:
        case 9:
            classificacao = 10;
            break;
        case 4:
        case 5:
        case 10:
            classificacao = 0;
            break;
        case 6:
        case 7:
            classificacao = 12;
            break;
        case 8:
            classificacao = 18;
            break;
        default:
            printf("Opcao invalida!\n");
            return 0;
    }

    precoBase = precos[opcaoFilme - 1];

    printf("Quantos ingressos deseja comprar? ");
    scanf("%d", &quantidade);

    // Validação das pessoas
    for(int i = 1; i <= quantidade; i++) {
        printf("\n--- Pessoa %d ---\n", i);

        printf("Digite a idade: ");
        scanf("%d", &idade);

        if(!podeAssistir(idade, classificacao)) {
            printf("Ingresso cancelado (classificacao %d+).\n", classificacao);
            continue;
        }

        printf("Possui carteira estudantil? (s/n): ");
        scanf(" %c", &estudante);

        if(estudante == 's' || estudante == 'S') {
            precoFinal = precoBase / 2;
        } else {
            precoFinal = precoBase;
        }

        total += precoFinal;
        ingressosValidos++;
    }

    if(ingressosValidos == 0) {
        printf("\nNenhum ingresso valido.\n");
        return 0;
    }

printf("\nMAPA DE ASSENTOS (O = livre | X = ocupado)\n\n");

//colunas
printf("  ");
for(int j = 1; j <= 10; j++) {
    printf("%d ", j);
}
printf("\n");

//linhas
for(int i = 0; i < 5; i++) {
    printf("%c ", 'A' + i);
    for(int j = 0; j < 10; j++) {
        printf("%c ", sala[i][j]); // O ou X
    }
    printf("\n");
}

    char linha;
    int coluna;

    for(int i = 0; i < ingressosValidos; i++) {
        printf("\nEscolha o assento da pessoa %d (ex: A5): ", i + 1);
        scanf(" %c%d", &linha, &coluna);

        int l = linha - 'A';
        int c = coluna - 1;

        if(l < 0 || l >= 5 || c < 0 || c >= 10) {
            printf("Assento invalido!\n");
            i--;
            continue;
        }

        if(sala[l][c] == 'X') {
            printf("Assento ocupado! Escolha outro.\n");
            i--;
            continue;
        }

        sala[l][c] = 'X';
    }

    printf("\n=== RESUMO ===\n");
    printf("Ingressos validos: %d\n", ingressosValidos);
    printf("Total a pagar: R$ %.2f\n", total);

    printf("\nBom filme!\n");

    return 0;
}
