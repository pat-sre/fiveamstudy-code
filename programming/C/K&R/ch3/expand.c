#include <stdio.h>

#define N 10000
/*
Exercise 3-3. 
Write a function expand(s1,s2) that expands shorthand notations like a-z in the
 string s1 into the equivalent complete list abc...xyz in s2. 

Allow for letters of either case and digits, and be prepared to handle cases like 
 a-b-c and a-z0−9 and -a-z. 

Arrange that a leading or trailing - is taken literally.
*/

void expand(char str[], char expanded_str[]);

int main() {
    char s1[N] = "0-9a-z hello e-g whast your name";
    char expanded[N];
    expand(s1, expanded);

    printf("%s\n", expanded);
}

void expand(char s[], char exp[]) {
    int letters;
    int i = 0, j = 0, start, end;
    int k = 0;
    while(s[i] != '\0'){
        if (i + 3 > N) return; // anti buffer overflow
        letters = 0;
        // s[i] in a, y
        // s[i+1] == '-'
        // s[i+2] in b, z
        char start = s[i];
        char end = s[i+2];
        if ('a' <= s[i] && s[i] < 'z' && s[i+1] == '-' && 'a' < s[i+2] && s[i+2] <= 'z' ){
            letters = s[i+2] - s[i];
            printf("%d\n", letters);
            for(j = s[i]; j <= s[i+2]; j++)
                exp[k++] = j;
            i += 2;
        } 
        // s[i] in 0,8
        // s[i+1] == '-'
        // s[i+2] in 1, 9
        else if ('0' <= s[i] && s[i] < '9' && s[i+1] == '-' && '0' < s[i+2] && s[i+2] <= '9' ){
            letters = s[i+2] - s[i];
            printf("%d\n", letters);
            for(j = s[i] - '0'; letters >= 0; letters--, j++)
                exp[k++] = j + '0';
            i += 2;
        }
        else {
            exp[k++] = s[i];
        }
        i++;
    }
    exp[k] = '\0';
}