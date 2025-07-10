#include <stdio.h>

/*
Exercise 2-6. 
Write a function setbits(x,p,n,y) that returns x with the n bits that begin 
at position p set to the rightmost n bits of y, 
leaving the other bits unchanged.

Exercise 2-7. 
Write a function invert(x,p,n) that returns x with the n bits that begin
at position p inverted (i.e., 1 changed into 0 and vice versa), 
leaving the others unchanged.
*/

unsigned setbits(unsigned x, int p, int n, unsigned y);

unsigned invert(unsigned x, int p, int n);

int main() {
    unsigned x, y;
    x = 0b11111111;
    y = 0b00101000;
    printf("%x\n", setbits(x, 4, 4, y));

}

unsigned setbits(unsigned x, int p, int n, unsigned y) {
    unsigned mask = ~(~0 << n);
    y = y & mask;
    y <<= (p + 1 - n);
    // clear n bits from the p position in x
    mask = ~(~0 << n ) << (p + 1 - n);
    x = x & ~mask;
    return x | y;
}

unsigned invert(unsigned x, int p, int n){
    // create n length mask
    unsigned mask = ~(~0 << n);
    // shift mask to position p
    mask <<= (p + 1 - n);
    return x ^ mask;
}