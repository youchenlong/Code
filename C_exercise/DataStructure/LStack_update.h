#include<stdio.h>
#include<stdlib.h>

typedef struct{
    char *studentID;
    char *studentName;
    char *sex;
    int age;
    char *class;
}DataType;

typedef struct node{
    DataType value;
    struct node *next;
}node;

typedef struct{
    int count;              // 栈内元素数量
    node *top;              // 栈顶元素
}LStack;

LStack create();                                    // 创建栈
void clear(LStack *s);                              // 清空栈
void push(LStack *s, DataType val);                 // 入栈
DataType pop(LStack *s);                            // 出栈
DataType topValue(LStack s);                        // 栈顶元素
int length(LStack s);                               // 已有元素的长度


LStack create(){
    LStack *s = (LStack *)malloc(sizeof(LStack));
    s->top = NULL;
    s->count = 0;
    return *s;
}

void clear(LStack *s){
    while(s->top != NULL){
        node *temp = s->top;
        s->top = s->top->next;
        free(temp);
    }
    s->count = 0;
}

void push(LStack *s, DataType val){
    node *n = (node *)malloc(sizeof(node));
    n->value = val;
    n->next = s->top;
    s->top = n;
    s->count++;
}

DataType pop(LStack *s){
    if(s->top == NULL){
        printf("LStack is empty");
        exit(0);
    }
    DataType val = s->top->value;
    node *temp = s->top;
    s->top = s->top->next;
    free(temp);
    s->count--;
    return val;
}

DataType topValue(LStack s){
    return s.top->value;
}

int length(LStack s){
    return s.count;
}