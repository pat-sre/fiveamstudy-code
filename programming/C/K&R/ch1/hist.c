#include<stdio.h>

int main(){
    int c, i;
    int hist[36];
    for(i = 0; i < 36; ++i)
        hist[i] = 0;
    
    while((c = getchar()) != 'q'){
        // if letter
        if ('a' <= c && c <= 'z')
            ++hist[10 + c - 'a'];
        // else if number
        else if ('0' <= c && c <= '9')
            ++hist[c - '0'];
    }
    for(i = 0; i < 36; i++){
        printf("%c | ", i);
        for(int j=0; j < hist[i]; j++)
            printf("=");
        printf("\n");
    }
}