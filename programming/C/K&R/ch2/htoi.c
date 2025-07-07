#include <stdio.h>
#include <string.h>
#include <math.h>
/*
Exercise 2-3. 
Write the function htoi(s), which converts a string of hexadecimal digits 
(including an optional 0x or 0X) into its equivalent integer value. 

The allowable digits are 0 through 9, a through f, and A through F.
*/

int htoi(char* hex_digits);

int main() {
    printf("%d\n", htoi("0xFF"));
}


int htoi(char* hex_str){
    int len = strlen(hex_str);
    int i, result, hex_digit;
    result = 0;

    if(hex_str[0] == '0' && hex_str[1] == 'x') {
        i = 2;
        while(hex_str[i]) {
            hex_str[i-2] = hex_str[i]; 
            ++i;
        }
        hex_str[i] = '\0';
    }
    printf("%s", hex_str);
    // printf("len: %d\n", len);
    // for (int i = 0; i < len; ++i) {
    //     hex_digit = hex_str[i];
    //     if ('A' <= hex_digit && hex_digit <= 'F'){
    //         hex_digit = hex_digit - 'A' + 10;
    //     } else if ('0' <= hex_digit && hex_digit <= '9') {
    //         hex_digit = hex_digit - '0';
    //     }
    //     printf("hex digit: %d\n", hex_digit);
    //     result += pow(16, len-i-1) * hex_digit;
    // }
    return result;
}