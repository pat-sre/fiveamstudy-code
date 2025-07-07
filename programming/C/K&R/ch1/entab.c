#include <stdio.h>

/*
Exercise 1-21. Write a program entab that replaces strings of blanks by the minimum number of 
tabs and blanks to achieve the same spacing. Use the same tab stops as for detab. 

When either a tab or a single blank would suffice to reach a tab stop, 
which should be given preference?
*/

#define TAB 8

int main() {
    int i, c, col, spaces;
    col = spaces = 0;
    while ((c = getchar()) != EOF) {
        if (c == '\n') {
            col = spaces = 0;
            putchar(c);
        } else if (c == ' '){
            ++col;
            ++spaces;
            if(col % TAB == 0) {
                spaces = 0;
                putchar('\t');
            }
        } else {
            while(spaces) {
                putchar(' ');
                spaces--;
            }            
            putchar(c);
            col++;
        }
    }
    while(spaces) {
        putchar(' ');
        spaces--;
    }
}