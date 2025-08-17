#include <stdio.h>

int bitwise_division(int dividend, int divisor);

int main() {
    printf("%d", bitwise_division(251231210, 5));
}

int bitwise_division(int dividend, int divisor){
    int i, result;
    result = 0;
    unsigned udivisor = divisor;
    for(i = sizeof(int) * 8 - 1; i >= 0; i--){
        if ((dividend >> i) >= udivisor){
            dividend -= (udivisor << i);
            result |= (1 << i);
        }
    }
    return result;
}
