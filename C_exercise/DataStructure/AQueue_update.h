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
    int maxSize;                    // 最大元素个数
    int front;                      // 队首位置
    int rear;                       // 队尾位置
    DataType *listArray;            // 容纳队列元素(数组是循环的--允许从最高位置延续到最低位置)
}AQueue;

AQueue create(int size);                            // 创建队列
void clear(AQueue *q);                              // 清空队列
void enqueue(AQueue *q, DataType val);              // 入队列
DataType dequeue(AQueue *q);                        // 出队列
DataType frontValue(AQueue q);                      // 队列首元素
int length(AQueue q);                               // 已有元素长度

AQueue create(int size){
    AQueue *q = (AQueue *)malloc(sizeof(AQueue));
    q->maxSize = size + 1;
    q->front = 1;
    q->rear = 0;
    // 循环数组会引入一个问题--无法判断数组是空还是满(因为两种情况下队首和队尾的相对相同)
    // 为此，设置数组大小为size+1，但是只存储size个元素，用来区分空和满的情况
    q->listArray = (DataType *)malloc(sizeof(DataType)*(size+1));
    return *q;
}

void clear(AQueue *q){
    q->front = 1;
    q->rear = 0;
}

void enqueue(AQueue *q, DataType val){
    // 如果数组已满--队尾在队首后面一个位置(相对位置)
    if((q->rear + 2) % q->maxSize == q->front){
        printf("AQueue is full");
        exit(0);
    }
    q->rear = (q->rear + 1) % q->maxSize;
    q->listArray[q->rear] = val;
}

DataType dequeue(AQueue *q){
    // 如果数组为空--队尾在队首后面两个位置(相对位置)
    if(length(*q) == 0){
        printf("AQueue is empty");
        exit(0);
    }
    DataType val = q->listArray[q->front];
    q->front = (q->front + 1) % q->maxSize;
    return val;
}

DataType frontValue(AQueue q){
    if(length(q) == 0){
        printf("AQueue is empty");
        exit(0);
    }
    return q.listArray[q.front];
}

int length(AQueue q){
    return (q.rear + 1 - q.front + q.maxSize) % q.maxSize;
}