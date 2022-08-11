#include<stdio.h>
#include"../exercises/parameter_passing.h"

int main(){
    int a = 1;
    int b = 2;
    value_transmission(a, b);
    printf("a = %d, b = %d\n", a, b);
    address_transmission(&a, &b);
    printf("a = %d, b = %d\n", a, b);
    return 0;
}