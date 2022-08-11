#include<stdio.h>
#include<string.h>

typedef unsigned char *byte_pointer;    // char类型占一个字节

void show_bytes(byte_pointer start, size_t len){
    size_t i;
    // 输出值
    for(i = 0; i < len; i++){
        printf("%.2x ", start[i]);
    }
    printf("\n");
    // 输出地址
    for(i = 0; i < len; i++){
        printf("%.2x ", &start[i]);
    }
    printf("\n");
}

int main(){
    char *s = "12345";
    show_bytes((byte_pointer)s, strlen(s));
    return 0;
}