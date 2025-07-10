#include<stdio.h>

#define N 1000
/*
Exercise 3-2. 
Write a function escape(s,t) that converts characters 
like newline and tab into visible escape 
sequences like \n and \t as it copies the string s to t. 
Use a switch. 
Write a function for the other direction as well, converting escape sequences into the real characters.
*/

void escape(char s[], char t[]);
void escape_reverse(char s[], char t[]);

int main(){
    char s[N] = "hello\n my\tname    is   pat";
    char t[N];

    escape(s, t);

    printf("%s\n", t);
    char ss[N] = "hello\\nmy name\\t is \\tpat";
    escape_reverse(ss, t);
    printf("%s\n", t);
}

void escape(char s[], char t[]){
    int i = 0, j = 0;
    while(s[i] != '\0'){
        switch(s[i]){
            case '\n': 
                t[j++] = '\\';
                t[j++] = 'n';
                i++;
                break;
            case '\t':
                t[j++] = '\\';
                t[j++] = 't';
                i++;
                break;
            default:
                t[j++] = s[i++];
                break;
            
        }
    }
    t[j] = '\0';
}

void escape_reverse(char s[], char t[]){
    int i, j;
    i = j = 0;
    while(s[i] != '\0'){
        switch(s[i]){
            case '\\':
                i++;
                if (s[i] == 'n') {
                    t[j++] = '\n';
                } else if (s[i] == 't'){
                    t[j++] = '\t';
                } else {
                    return;
                }
                i++;
                break;
            default:
                t[j++] = s[i++];
                break;

        }
    }
    t[j] = '\0';
}