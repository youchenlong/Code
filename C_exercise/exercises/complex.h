#include<stdio.h>
#include<stdlib.h>
#include<windows.h>

typedef struct{
    float real;
    float imag;
}complex;

void construct(complex *z, float real, float imag);     //构造
void add(complex *z, complex z1, complex z2);           //加法
void sub(complex *z, complex z1, complex z2);           //减法
void multiply(complex *z, complex z1, complex z2);      //乘法
void divide(complex *z, complex z1, complex z2);        //除法
float getReal(complex z);                               //获取实部
float getImag(complex z);                               //获取虚部
void print_complex(complex z);                          //输出复数


void construct(complex *z, float real, float imag){
    z->real = real;
    z->imag = imag;
}
void add(complex *z, complex z1, complex z2){
    z->real = z1.real + z2.real;
    z->imag = z1.imag + z2.imag;
}
void sub(complex *z, complex z1, complex z2){
    z->real = z1.real - z2.real;
    z->imag = z1.imag - z2.imag;
}
void multiply(complex *z, complex z1, complex z2){
    z->real = z1.real * z2.real - z1.imag * z2.imag;
    z->imag = z1.imag * z2.real + z1.real * z2.imag;
}
void divide(complex *z, complex z1, complex z2){
    if(z2.real * z2.real + z2.imag * z2.imag == 0){
        // 以红色字体输出
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), FOREGROUND_RED);
        printf("%s", "divisor equals 0");
        SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), FOREGROUND_RED|FOREGROUND_GREEN|FOREGROUND_BLUE);
        exit(0);
    }
    z->real = (z1.real * z2.real + z1.imag + z2.imag) / (z2.real * z2.real + z2.imag * z2.imag);
    z->imag = (z1.imag * z2.real - z1.real * z2.imag) / (z2.real * z2.real + z2.imag * z2.imag);
}
float getReal(complex z){
    return z.real;
}
float getImag(complex z){
    return z.imag;
}
void print_complex(complex z){
    printf("%f+%fi\n", getReal(z), getImag(z));
}