#include <stdio.h>

int main(){
    int c;
    while ((c=getchar()) != '0'){
        if (c == ' ')
            putchar('\n');
        else
            putchar(c);
    }
    return 0;
}