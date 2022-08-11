#include<stdio.h>
#include<math.h>
#include"exercises/Factorial.h"

int main(){
    int times = 0;
    int n = 31;
    printf("logn=%d", log2(n));
    printf("n=%d\n", n);
    printf("n*logn=%.0f\n", n*log2(n));
    printf("n*n=%d\n", n*n);
    printf("n*n*n=%d\n", n*n*n);
    printf("2^n=%.0f\n", exp2(n));
    printf("n!=%d\n", Factorial(n));
    return 0;
}