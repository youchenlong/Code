#include<stdio.h>
#include<stdlib.h>
// 小写转大写
void uppercase(char *str, int N){
    for(int i = 0; i < N; i++){
        if(str[i] < 0x61 || str[i] > 0x7a){
            printf("%s", "Contains characters that are not lowercase letters");
            exit(0);
        }
    }
    for(int i = 0; i < N; i++){
        str[i] = str[i] & 0b11011111;
    }
}

// 大写转小写
void lowercase(char *str, int N){
    for(int i = 0; i < N; i++){
        if(str[i] < 0x41 || str[i] > 0x5a){
            printf("%s", "Contains characters that are not uppercase letters");
            exit(0);
        }
    }
    for(int i = 0; i < N; i++){
        str[i] = str[i] | 0b00100000;
    }
}