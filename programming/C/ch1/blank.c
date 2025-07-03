#include<stdio.h>

int main() {
    int c, prev_c;
    prev_c = '\0';
    while ((c=getchar()) != EOF) {
        if(!(c == ' ' && prev_c == ' '))
            putchar(c);
        prev_c = c;
    }
}