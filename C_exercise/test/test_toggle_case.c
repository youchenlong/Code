#include<stdio.h>
#include"exercises/toggle_case.h"

int main(){
    // char str[5] = "Hell&";
    char str[5] = "Basic";
    uppercase(str, 5);
    puts(str);
    lowercase(str, 5);
    puts(str);
    return 0;
}