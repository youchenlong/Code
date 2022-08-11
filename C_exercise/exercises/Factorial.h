#include<stdlib.h>

int Factorial(int n);       // 计算阶乘

int Factorial(int n){
    if(n>31){
        printf("n is too large");
        exit(0);
    }
    if(n==1){
        return 1;
    }
    return n*Factorial(n-1);
}