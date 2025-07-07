#include <stdio.h>
#define MAXLINE 1000
/*
 Exercise 1-19. 
 Write a function reverse(s) that reverses the character string s. 
 Use it to write a program that reverses its input a line at a time. 
 */



void reverse(char line[], int len);

int main() {
    // read a line
    int c, i, len;
    char line[MAXLINE];
    i = len = 0;

    while((c=getchar()) != EOF) {
        if (c == '\n') {
            line[i] = '\0';
            reverse(line, len);
            printf("%s", line);
            i = -1;
            len = 0;
        } else  if (i < MAXLINE-1) {
            line[i] = c;
            ++len;
        }
        ++i;
    }

    
}

void reverse(char line[], int len) {
    int i, j;
    char temp;
    for (i = 0, j = len - 1; i < j; ++i, --j){
        temp = line[len-i-1];
        line[len-i-1] = line[i]; 
        line[i] = temp;
    }
}
