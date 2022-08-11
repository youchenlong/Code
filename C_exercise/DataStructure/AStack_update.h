#include<stdio.h>
#include<stdlib.h>

typedef struct{
    char *studentID;
    char *studentName;
    char *sex;
    int age;
    char *class;
}DataType;

typedef struct{
    int size;               // 栈大小
    int top;                // 栈顶元素索引(下标)
    DataType *array;             // 存放栈内元素
}AStack;

AStack create(int size);                            // 创建栈
void clear(AStack *s);                              // 清空栈
void push(AStack *s, DataType val);                      // 入栈
DataType pop(AStack *s);                            // 出栈
DataType topValue(AStack s);                        // 栈顶元素
int length(AStack s);                               // 已有元素的长度


AStack create(int size){
    AStack *s = (AStack *)malloc(sizeof(AStack));
    s->size = size;
    s->top = size;  // 从高地址到低地址
    s->array = (DataType *)malloc(sizeof(DataType)*size);
    return *s;
}

void clear(AStack *s){
    s->top = s->size;
}

void push(AStack *s, DataType val){
    if(s->top == 0){
        printf("AStack is full");
        exit(0);
    }
    s->top--;
    s->array[s->top] = val;
}

DataType pop(AStack *s){
    if(s->top == s->size){
        printf("AStack is empty");
        exit(0);
    }
    DataType val = s->array[s->top];
    s->top++;
    return val;
}

DataType topValue(AStack s){
    return s.array[s.top];
}

int length(AStack s){
    return s.size - s.top;
}