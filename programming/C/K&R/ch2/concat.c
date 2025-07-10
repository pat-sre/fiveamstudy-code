#include<stdio.h>

void strcat(char s[], char t[]);

int main() {

}

void strcat(char s[], char t[]){
    int i, j;

    i = j = 0;
    while(s[i] != '\0')
        i++;
    while( (s[i++] = t[j++]) != '\0' )
        ;
        
}