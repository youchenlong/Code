#include<stdio.h>
#include<stdlib.h>

typedef struct{
    int size;               // 栈大小
    int top;                // 栈顶元素
    int *array;             // 存放栈内元素
}AStack;

AStack create(int size);                    // 创建栈
void clear(AStack *s);                      // 清空栈
void push(AStack *s, int val);              // 入栈
int pop(AStack *s);                         // 出栈
int topValue(AStack s);                     // 栈顶元素
int length(AStack s);                       // 已有元素的长度


AStack create(int size){
    AStack *s = (AStack *)malloc(sizeof(AStack));
    s->size = size;
    s->top = size;
    s->array = (int *)malloc(sizeof(int)*size);
    return *s;
}

void clear(AStack *s){
    s->top = s->size;
}

void push(AStack *s, int val){
    if(s->top == 0){
        printf("AStack is full");
        exit(0);
    }
    s->top--;
    s->array[s->top] = val;
}

int pop(AStack *s){
    if(s->top == s->size){
        printf("AStack is empty");
        exit(0);
    }
    int val = s->array[s->top];
    s->top++;
    return val;
}

int topValue(AStack s){
    return s.array[s.top];
}

int length(AStack s){
    return s.size - s.top;
}