#include <stdio.h>

/*
Exercise 1-20. 

Write a program detab that replaces tabs in the input with 
the proper number of blanks to space to the next tab stop. 

Assume a fixed set of tab stops, say every n columns. 
Should n be a variable or a symbolic parameter?
*/

#define TAB 8

int main() {
    int c, i, col;
    i = col = 0;

    while((c = getchar()) != EOF) {
        if (c == '\t') {
            while(col < TAB) {
                putchar(' ');
                ++col;
            }
            col = 0;    
        } else {
            putchar(c);
            if (c == '\n')  col = 0;
            else            col = (col + 1) % TAB;
        }
    }
}


