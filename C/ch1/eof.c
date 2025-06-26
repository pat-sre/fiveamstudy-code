#include<stdio.h>

int main() {
    int c;
    printf("%d\n", EOF);
    while( (c = getchar()) != EOF) {
        printf("%d\n", c == EOF);
    }
}