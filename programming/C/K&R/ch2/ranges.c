#include <stdio.h>
#include <limits.h>

/*
Exercise 2-1. Write a program to determine the ranges of char, short, int, and long variables, 
both signed and unsigned, by printing appropriate values from standard headers and by direct computation. 
Harder if you compute them: determine the ranges of the various floating-point types.
*/

int main() {
    unsigned char min_uc = 0x00, max_uc = 0xFF;
    char min_c = 0x80, max_c = 0x7F;

    printf("U CHAR: %u | %u \nCHAR: %d | %d\n\n", min_uc, max_uc, min_c, max_c);

    unsigned short min_ush = 0x0, max_ush = 0xFFFF;
    short min_sh = 0x8000, max_sh = 0x7FFF;

    printf("U SHORT: %u | %u \nSHORT: %d | %d\n\n", min_ush, max_ush, min_sh, max_sh);

    unsigned int min_uint = 0x0, max_uint = 0xFFFFFFFF;
    int min_int = 0x80000000, max_int = 0x7FFFFFFF;

    printf("U INT: %u | %u \nINT: %d | %d\n\n", min_uint, max_uint, min_int, max_int);


    printf("U LONG: %lu | %lu \nLONG: %ld | %ld\n\n", 0, ULONG_MAX, LONG_MIN, LONG_MAX);

    
}