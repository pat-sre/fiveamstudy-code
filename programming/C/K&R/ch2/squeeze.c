#include <stdio.h>

void squeeze(char string[], const char* letters_to_delete);


int main() {
    char str1[] = "hello this is the five am study";
    const char* s2 = "abcde";
    squeeze(str1, s2);
    printf("%s\n", str1);
}

void squeeze(char s1[], const char* s2){
    int in = 0, out = 0;
    for (; s1[in] != '\0'; ++in) {
        int j;
        for (j = 0; s2[j] && s2[j] != s1[in]; j++)
        ;
        if (s2[j] == '\0')
            s1[out++] = s1[in];
    }
    s1[out] = '\0';
}
