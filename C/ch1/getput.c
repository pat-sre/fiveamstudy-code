#include<stdio.h>

// int main() {
//     int c;
//     c = getchar();
//     while (c != EOF) {
//         putchar(c);
//         c = getchar();
//     }
// }

int main() {
    int c;
    while((c=getchar()) != EOF) {
        putchar(c);
        //printf("%c\t%d", c, c);
    }
}