#include<stdio.h>
#include<stdint.h>

int main(){
    int n = 20;
    int a[n];
    for(int i = 0; i < n; i++){
        a[i] = i;
    }
    for(int i = 0; i < n; i++){
        printf("%d ", a[i]);
    }
    return 0;
}