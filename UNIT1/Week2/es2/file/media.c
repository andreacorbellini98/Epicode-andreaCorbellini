#include <stdio.h>

int main() {
    int num1, num2;
    float media;
    
    printf("Inserisci il primo numero intero: ");
    scanf("%d", &num1);
    
    printf("Inserisci il secondo numero intero: ");
    scanf("%d", &num2);
    
    media = (float)(num1 + num2) / 2;
    
    printf("La media aritmetica è: %.2f\n", media);
    
    return 0;
}