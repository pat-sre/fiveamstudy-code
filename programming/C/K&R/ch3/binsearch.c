#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 1000000
#define ROUNDS 100000000

/* binsearch:  find x in v[0] <= v[1] <= ... <= v[n−1] */
int binsearch(int x, int v[], int n)
{
    int low, high, mid;

    low = 0;
    high = n - 1;
    while (low <= high) {
        mid = (low+high) / 2;
        if (x < v[mid])
            high = mid - 1;
        else if (x > v[mid])
            low = mid + 1;
        else    /* found match */
            return mid;
    }
    return -1;    /* no match */
}

int binsearch_onetest(int x, int v[], int n)
{
    int low, high, mid;

    low = 0;
    high = n - 1;
    while (low < high) {
        mid = (low+high) / 2;
        if (x <= v[mid])
            high = mid;
        else
            low = mid + 1;
    }
    return v[low] == x ? low : -1;    
}

double secs(clock_t ticks) {
    return (double)ticks / CLOCKS_PER_SEC;
}

int main() {

    int i, nums[N];
    for (i=0; i<N; ++i) nums[i] = i;
    
    srand(0xFAFA);

    clock_t t0 = clock();
    for(i=0; i<ROUNDS; ++i){
        binsearch(rand() % N, nums, N);
    }
    clock_t t1 = clock();
    printf("two tests: %.3f\n", secs(t1-t0));
    for(i=0; i<ROUNDS; ++i){
        binsearch_onetest(rand() % N, nums, N);
    }
    clock_t t2 = clock();

    
    printf("one test: %.3f\n", secs(t2-t1));
}