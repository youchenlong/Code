#include<stdint.h>

void value_transmission(int a, int b){
    int temp;
    temp = a;
    a = b;
    b = temp;
}

void address_transmission(int *a, int *b){
    int64_t temp;
    temp = *a;
    *a = *b;
    *b = temp;
}