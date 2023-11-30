#include <stdio.h>

#define LINHAS 3
#define COLUNAS 3
#define TAMANHO_STRING 20

// Função para imprimir a tabela de análise preditiva M
void imprimirTabela(char tabela[LINHAS][COLUNAS][TAMANHO_STRING]) {
    printf("Tabela de Analise Preditiva M:\n");
    printf("----------------------------\n");
    for (int i = 0; i < LINHAS; ++i) {
        for (int j = 0; j < COLUNAS; ++j) {
            printf("  %-18s |", tabela[i][j]);
        }
        printf("\n");
    }
    printf("----------------------------\n");
}

int main() {
    char tabela[LINHAS][COLUNAS][TAMANHO_STRING] = {
        {"A->α", "B->β", "C->γ"},
        {"D->δ", "E->ε", "F->φ"},
        {"G->ζ", "H->η", "I->ι"}
    };

    imprimirTabela(tabela);

    return 0;
}
