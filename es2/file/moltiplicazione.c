#include <stdio.h>

int main() {
    float num1, num2, risultato;
    
    printf("Inserisci il primo numero: ");
    scanf("%f", &num1);
    
    printf("Inserisci il secondo numero: ");
    scanf("%f", &num2);
    
    risultato = num1 * num2;
    
    printf("Il risultato della moltiplicazione è: %.2f\n", risultato);
    
    return 0;
}