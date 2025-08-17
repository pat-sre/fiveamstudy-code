#include <stdio.h>
#include <string.h>

#define MAXLINE 1000

int get_line(char line[], int max);
int strindex(char source[], char searchfor[]);
void reverse(char s[]);
int strindex_r(char s[], char pattern[]);



int get_line(char line[], int lim) {
    int c, i;

    i = 0;
    while (--lim > 0 && (c=getchar()) != EOF && c != '\n')
        line[i++] = c;
    if (c == '\n')
        line[i++] = c;
    line[i] = '\0';

    return i;
}

int strindex(char s[], char pattern[]) {
    int i, j, k;

    for (i = 0; s[i] != '\0'; i++) {
        for (j=i, k=0; pattern[k] != '\0' && s[j] == pattern[k]; j++, k++)
            ;
        if (k > 0 && pattern[k] == '\0')
            return i;
    }

    return -1;
}
/*
Exercise 4-1. 
Write the function strrindex(s,t), which returns the position of the rightmost occurrence of t in s, 
or −1 if there is none.
*/

int main() {
    char line[MAXLINE];
    int found = 0;
    char pattern[] = "hello";

    while (get_line(line, MAXLINE) > 0) {
        if (strindex_r(line, pattern) >= 0) {
            printf("%s\n", line);
            found++;
        }
    }
    return found;
}

void reverse(char s[]) {
    int len = strlen(s);
    char temp;
    for (int i = 0; i < len / 2; i++){
        temp = s[len - 1 - i];
        s[len - 1 - i] = s[i];
        s[i] = temp;
    }
    return;
}

int strindex_r(char s[], char pattern[]) {
    int i, j, k;
    int s_len = strlen(s);
    int p_len = strlen(pattern);

    for (i = s_len - 1; i >= 0; i--) {
        // Loop as long as j and k are positive and s matches pattern
        for (j = i, k = p_len - 1; j >= 0 && k >= 0 && s[j] == pattern[k]; j--, k--)
        ;
        if (k == -1) {
            printf("FOUND at %d (s: %s, pattern: %s)\n", j+1, s, pattern);
            return j+1;
        } 
    }
    return -1;
}