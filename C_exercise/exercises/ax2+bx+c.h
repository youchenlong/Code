#include<stdio.h>
#include<stdlib.h>
#include<math.h>

float* solve(float a, float b, float c){
    // 判断a是否等于0
    if(a == 0){
        printf("%s", "not quadratic equation of one unknown");
        exit(0);
    }
    // 计算delta
    float delta = b*b - 4*a*c;
    // 判断delta，并返回结果
    if(delta < 0){
        printf("%s", "quadratic equation has no real root");
        exit(0);
    }
    float *result = (float *)malloc(sizeof(float)*2);
    result[0] = -b/(2*a) + sqrt(delta)/(2*a);
    result[1] = -b/(2*a) - sqrt(delta)/(2*a);
    return result;
}