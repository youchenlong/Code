#include<stdio.h>
#include<stdint.h>

int main(){
    int64_t i = 64;
    size_t len = sizeof(i);
    printf("%d", len);
    return 0;
}