#include <stdio.h>

int main() {
    printf("%c\n", '\x31');
    printf("%d\n", '\0');
    printf("%s\n", "hello,"  "world");
    float b = 0.9999;
    int a = b;
    printf("%d", a);
}