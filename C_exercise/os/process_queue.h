#include"process.h"

typedef struct node{
    process value;
    struct node *next;
}node;

typedef struct{
    node *head;         // 头节点
    node *tail;         // 尾节点
    node *curr;         // 当前节点(为了方便进行插入或删除操作，实际上操作的是当前节点的下一个节点)
    int count;          // 链表当前节点数(空节点除外)
}process_queue;

process_queue create();                                         // 创建链表
void clear(process_queue *q);                                   // 清空链表
void append(process_queue *q, process value);                   // 在链表末尾添加节点
void insert(process_queue *q, process value);                   // 在当前位置插入节点
process delete(process_queue *q);                               // 在当前位置删除节点
void moveToStart(process_queue *q);                             // 移到表头
void moveToEnd(process_queue *q);                               // 移到表位
void moveToPos(process_queue *q, int pos);                      // 移到指定位置(pos从0开始)
int currPos(process_queue q);                                   // 当前位置
void next(process_queue *q);                                    // 当前位置向后移
process getValue(process_queue q);                              // 获取当前节点的元素

process FCFS_POP(process_queue *q, int timer);                              // 最先到达的进程
process SJF_POP(process_queue *q, int timer);                               // 剩余执行时间最短的进程
process PS_POP(process_queue *q, int timer);                                // 优先级最高的进程
process RR_POP(process_queue *q, int timer);                                // 轮流执行
void waiting_queue(process_queue *q);                                       // 队列中所有进程等待一个时间片


void init(process_queue *q){
    // 当链表为空时，头节点、尾节点、当前节点无处可指，在插入删除操作时，需要增加额外的代码。
    // 为此，增加一个空节点
    node *n = (node *)malloc(sizeof(node));
    n->next = NULL;
    // 头节点，尾节点，当前节点指向空节点
    q->head = n;
    q->curr = n;
    q->tail = n;
    q->count = 0; 
}

void removeall(process_queue *q){
    // 只要链表不为空，不断地从头删除节点
    while(q->head != NULL){
        q->curr = q->head;
        q->head = q->head->next;
        free(q->curr);
    }
}

process_queue create(){  
    process_queue *q = (process_queue *)malloc(sizeof(process_queue));
    init(q);
    return *q;
}

void clear(process_queue *q){
    removeall(q);
    init(q);
}

void append(process_queue *q, process value){
    node *n = (node *)malloc(sizeof(node));
    n->value = value;
    n->next = NULL;
    // 让链表尾节点指向它(注意指针与实际物理内存的联系，不然会产生疑惑)
    q->tail->next = n;   
    q->tail = q->tail->next;
    q->count++;
}

void insert(process_queue *q, process value){
    node *n = (node *)malloc(sizeof(node));
    n->value = value;
    n->next = q->curr->next;
    q->curr->next = n;
    // 如果当前节点为尾节点，那么尾节点需要指向该节点(尾节点始终应该在链表末尾)
    if(q->curr == q->tail){
        q->tail = q->curr->next;
    }
    q->count++;
}

process delete(process_queue *q){
    // getValue已经判断了是否为空的情况
    process value = getValue(*q);
    node *n = q->curr->next;
    // 如果待删除的节点为尾节点，那么尾节点需要指向当前节点(因为尾节点不应该无处可指)
    if(q->curr->next == q->tail){
        q->tail = q->curr;
    }
    q->curr->next = q->curr->next->next;
    free(n);
    q->count--;
    return value;
}

void moveToStart(process_queue *q){    
    q->curr = q->head;
}

void moveToEnd(process_queue *q){
    q->curr = q->tail;
}

void moveToPos(process_queue *q, int pos){
    if(pos < 0 || pos >= q->count){
        printf("position out of range");
        exit(0);
    }
    moveToStart(q);
    int i = 0;
    while(i < pos){
        q->curr = q->curr->next;
        i++;
    }
}

int currPos(process_queue q){
    node *temp = q.head;
    int i;
    for(i = 0; q.curr != temp; i++){
        temp = temp->next;
    }
    return i;
}

void next(process_queue *q){
    if(q->curr != q->tail){
        q->curr = q->curr->next;
    }
}

process getValue(process_queue q){
    if(q.curr->next == NULL){
        printf("No value");
        exit(0);
    }
    // 返回的是当前节点的下一个节点的值
    return q.curr->next->value;
}

process FCFS_POP(process_queue *q, int timer){
    int pos = 0;    // 记录最先到达的进程所在的位置
    int i = 0;      // 记录当前位置
    int arrival_time = INT_MAX;
    moveToStart(q);
    while(q->curr != q->tail){
        // 只能在已经到达的进程中寻找
        if(getValue(*q).arrival_time <= timer && getValue(*q).arrival_time < arrival_time){
            arrival_time = getValue(*q).arrival_time;
            pos = i;
        }
        i++;
        next(q);
    }
    // 如果当前没有进程，则返回队列中第一个进程
    moveToPos(q, pos);
    return delete(q);
}

process SJF_POP(process_queue *q, int timer){
    int pos = 0;    // 记录剩余执行时间最短的进程所在的位置
    int i = 0;      // 记录当前位置
    int remaining_execution_time = INT_MAX;
    moveToStart(q);
    while(q->curr != q->tail){
        if(getValue(*q).arrival_time <= timer && getValue(*q).remaining_execution_time < remaining_execution_time){
            remaining_execution_time = getValue(*q).remaining_execution_time;
            pos = i;
        }
        i++;
        next(q);
    }
    // 如果当前没有进程，则返回队列中第一个进程
    moveToPos(q, pos);
    return delete(q);
}

process PS_POP(process_queue *q, int timer){
    int pos = 0;    // 记录剩余执行时间最短的进程所在的位置
    int i = 0;      // 记录当前位置
    int priority = INT_MIN;
    moveToStart(q);
    while(q->curr != q->tail){
        if(getValue(*q).arrival_time <= timer && getValue(*q).priority > priority){
            priority = getValue(*q).priority;
            pos = i;
        }
        i++;
        next(q);
    }
    // 如果当前没有进程，则返回队列中第一个进程
    moveToPos(q, pos);
    return delete(q);
}

process RR_POP(process_queue *q, int timer){
    moveToStart(q);
    while(q->curr != q->tail){
        if(getValue(*q).arrival_time <= timer){
            break;
        }
        next(q);
    }
    return delete(q);
}

void waiting_queue(process_queue *q){
    int pos = currPos(*q);
    for(moveToStart(q); q->curr != q->tail; next(q)){
        waiting_process(&(q->curr->value));
    }
    if(pos < q->count){
        moveToPos(q, pos);
    }
}