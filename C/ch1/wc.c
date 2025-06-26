#include<stdio.h>

#define OUT 0
#define IN 1

int main() {
    int c, nc, nl, nw, state;
    nc=0;
    nl=0;
    nw=0;
    state = OUT;
    while( (c=getchar()) != ']' ){
        nc++;
        if (c == '\n')
            nl++;
        if (c == ' ' || c == '\n' || c == '\t')
            state = OUT;
        else if (state == OUT) {
            state = IN;
            nw++;
        }

    }
    printf("%d, %d, %d", nc, nl, nw);
}