#include<stdlib.h>
#include<stdio.h>

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
    node *front;        // 头指针
    node *rear;         // 尾指针
    int count;          // 队列中的节点数量(空节点除外)
}LQueue;

LQueue create();                                    // 创建队列
void clear(LQueue *q);                              // 清空队列
void enqueue(LQueue *q, DataType val);              // 入队列
DataType dequeue(LQueue *q);                        // 出队列
DataType frontValue(LQueue q);                      // 队列首元素
int length(LQueue q);                               // 已有元素长度

LQueue create(){
    LQueue *q = (LQueue *)malloc(sizeof(LQueue));
    // 与链表的实现类似，增加一个空节点，简化入队列出队列的实现
    node *n = (node *)malloc(sizeof(node));
    n->next = NULL;
    q->front = n;
    q->rear = n;
    q->count = 0;
    return *q;
}

void clear(LQueue *q){
    while(q->front->next != NULL){
        q->rear = q->front;
        q->front = q->front->next;
        free(q->rear);
    }
    q->rear = q->front;
    q->count = 0;
}

void enqueue(LQueue *q, DataType val){
    node *n = (node *)malloc(sizeof(node));
    n->value = val;
    n->next = NULL;
    q->rear->next = n;
    q->rear = q->rear->next;
    q->count++;
}

DataType dequeue(LQueue *q){
    if(q->count == 0){
        printf("LQueue is empty");
        exit(0);
    }
    DataType value = q->front->next->value;
    node *temp = q->front->next;
    q->front->next = q->front->next->next;
    free(temp);
    q->count--;
    return value;
}

DataType frontValue(LQueue q){
    if(q.count == 0){
        printf("LQueue is empty");
        exit(0);
    }
    return q.front->next->value;
}

int length(LQueue q){
    return q.count;
}