#include<stdio.h>

float celsius_to_fahr(float celsius){
    return (9.0/5.0) * celsius + 32.0;
}

int main() {
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;
    upper = 300;
    step = 30;

    
    printf("-----------------");
    printf("| Temp converter |");
    printf("-----------------");
    fahr = lower;
    while (fahr <= upper) {
        celsius = (5.0/9.0) * (fahr - 32.0);
        printf("Fahr(%6.1f) = Celsius(%6.1f)\n", fahr, celsius);
        printf("Celsius(%6.1f) = Fahr(%6.1f)\n", celsius, celsius_to_fahr(celsius));
        printf("\n");
        fahr += step;
    }
}