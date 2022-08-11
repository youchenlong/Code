#include<stdio.h>
#include<stdint.h>

void inplace_swap(int *x, int *y){
    *y = *x ^ *y;
    *x = *x ^ *y;
    *y = *x ^ *y;
}

void reverse_array(int a[], int64_t cnt){
    int64_t first, last;
    for(first = 0, last = cnt - 1; first < last; first++, last--){
        inplace_swap(&a[first], &a[last]);
    }
}

int main(){
    int a[5] = {0, 1, 2, 3, 4};
    reverse_array(a, 5);
    for(int i = 0; i < 5; i++){
        printf("%d ", a[i]);
    }
    return 0;
}