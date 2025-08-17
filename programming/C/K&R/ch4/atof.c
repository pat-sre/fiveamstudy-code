#include <stdio.h>
#include <ctype.h>
#include <math.h>

double atof(char s[]);
int atoi(char s[]);


int main() {
    char s[] = "-5.0e2";

    printf("atof: %f\natoi: %d\n", atof(s), atoi(s));
}

// `return` automatically converts to the type of the function
int atoi(char s[]) {
    return atof(s);
}
/*
Exercise 4-2. 
Extend atof to handle scientific notation of the form
123.45e−6
where a floating-point number may be followed by e or E and an optionally signed exponent.
*/
double atof(char s[]) {
    double val, power;
    int i, sign;

    //skip white space
    for(i = 0; isspace(s[i]); i++)
        ; 
    sign = (s[i] == '-') ? -1 : 1;
    // integer part
    if (s[i] == '+' || s[i] == '-')
        i++;
    for (val = 0.0; isdigit(s[i]); i++)
        val = 10.0 * val + (s[i] - '0');

    // floating point part
    if (s[i] == '.')
        i++;
    for (power = 1.0; isdigit(s[i]); i++) {
        val = 10.0 * val + (s[i] - '0');
        power *= 10.0; 
    }

    // scientific notation part (example: e−6, e6)
    int exp_val;
    int exp_sign = 1;

    if (s[i] == 'e' || s[i] == 'E')
        i++;
    if (s[i] == '-') {
        exp_sign = -1;
        i++;
    } else if (s[i] == '+') {
        i++;
    }
    for (exp_val = 0; isdigit(s[i]); i++)
        exp_val = 10 * exp_val + (s[i] - '0');      

    return sign * val / power * pow(10, exp_sign * exp_val);
}