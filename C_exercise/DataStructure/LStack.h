#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int value;
    struct node *next;
}node;

typedef struct{
    int count;              // 栈内元素数量
    node *top;              // 栈顶元素
}LStack;

LStack create();                            // 创建栈
void clear(LStack *s);                      // 清空栈
void push(LStack *s, int val);              // 入栈
int pop(LStack *s);                         // 出栈
int topValue(LStack s);                     // 栈顶元素
int length(LStack s);                       // 已有元素的长度


LStack create(){
    LStack *s = (LStack *)malloc(sizeof(LStack));
    // 即使头指针无处可指，入栈出栈操作也不会受到影响。因此，不需要空节点
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

void push(LStack *s, int val){
    node *n = (node *)malloc(sizeof(node));
    n->value = val;
    n->next = s->top;
    s->top = n;
    s->count++;
}

int pop(LStack *s){
    if(s->top == NULL){
        printf("LStack is empty");
        exit(0);
    }
    int value = s->top->value;
    node *temp = s->top;
    s->top = s->top->next;
    free(temp);
    s->count--;
    return value;
}

int topValue(LStack s){
    return s.top->value;
}

int length(LStack s){
    return s.count;
}