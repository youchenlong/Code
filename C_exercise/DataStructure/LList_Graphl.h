#include<stdio.h>
#include<stdlib.h>

typedef struct{
    int v;              // 边的终点
    int w;              // 边的权重
}Edge;

typedef struct node{
    Edge value;
    struct node *next;
}node;

typedef struct{
    node *head;         // 头节点
    node *tail;         // 尾节点
    node *curr;         // 当前节点(为了方便进行插入或删除操作，实际上操作的是当前节点的下一个节点)
    int count;          // 链表当前节点数(空节点除外)
}LList;

LList create_LList();                                   // 创建链表
void clear(LList *llist);                               // 清空链表
void append(LList *llist, Edge value);                  // 在链表末尾添加节点
void insert(LList *llist, Edge value);                  // 在当前位置插入节点
Edge delete(LList *llist);                              // 在当前位置删除节点
int currPos(LList llist);                               // 获取当前位置
void moveToStart(LList *llist);                         // 移到表头
void moveToEnd(LList *llist);                           // 移到表位
void moveToPos(LList *llist, int pos);                  // 移到指定位置(pos从0开始)
void next(LList *llist);                                // 当前位置向后移
Edge getValue(LList llist);                             // 获取当前节点的元素
int length(LList llist);                                // 获取链表长度

Edge create_Edge(int v, int w);                         // 创建边并初始化权重
int _vertex(Edge e);                                    // 获取边的终点
int _weight(Edge e);                                    // 获取边的权重


void init(LList *llist){
    // 当链表为空时，头节点、尾节点、当前节点无处可指，在插入删除操作时，需要增加额外的代码。
    // 为此，增加一个空节点
    node *n = (node *)malloc(sizeof(node));
    n->next = NULL;
    // 头节点，尾节点，当前节点指向空节点
    llist->head = n;
    llist->curr = n;
    llist->tail = n;
    llist->count = 0; 
}

void removeall(LList *llist){
    // 只要链表不为空，不断地从头删除节点
    while(llist->head != NULL){
        llist->curr = llist->head;
        llist->head = llist->head->next;
        free(llist->curr);
    }
}

LList create_LList(){  
    LList *llist = (LList *)malloc(sizeof(LList));
    init(llist);
    return *llist;
}

void clear(LList *llist){
    removeall(llist);
    init(llist);
}

void append(LList *llist, Edge value){
    node *n = (node *)malloc(sizeof(node));
    n->value = value;
    n->next = NULL;
    // 让链表尾节点指向它(注意指针与实际物理内存的联系，不然会产生疑惑)
    llist->tail->next = n;   
    llist->tail = llist->tail->next;
    llist->count++;
}

void insert(LList *llist, Edge value){
    node *n = (node *)malloc(sizeof(node));
    n->value = value;
    n->next = llist->curr->next;
    llist->curr->next = n;
    // 如果当前节点为尾节点，那么尾节点需要指向该节点(尾节点始终应该在链表末尾)
    if(llist->curr == llist->tail){
        llist->tail = llist->curr->next;
    }
    llist->count++;
}

int currPos(LList llist){
    node *temp = llist.head;
    int i;
    for(i = 0; temp != llist.curr; i++){
        temp = temp->next;
    }
    return i;
}

Edge delete(LList *llist){
    // getValue已经判断了是否为空的情况
    Edge value = getValue(*llist);
    node *n = llist->curr->next;
    // 如果待删除的节点为尾节点，那么尾节点需要指向当前节点(因为尾节点不应该无处可指)
    if(llist->curr->next == llist->tail){
        llist->tail = llist->curr;
    }
    llist->curr->next = llist->curr->next->next;
    free(n);
    llist->count--;
    return value;
}

void moveToStart(LList *llist){    
    llist->curr = llist->head;
}

void moveToEnd(LList *llist){
    llist->curr = llist->tail;
}

void moveToPos(LList *llist, int pos){
    if(pos < 0 || pos >= llist->count){
        printf("position out of range");
        exit(0);
    }
    moveToStart(llist);
    int i = 0;
    while(i < pos){
        llist->curr = llist->curr->next;
        i++;
    }
}

void next(LList *llist){
    if(llist->curr != llist->tail){
        llist->curr = llist->curr->next;
    }
}

Edge getValue(LList llist){
    if(llist.curr->next == NULL){
        printf("No value");
        exit(0);
    }
    // 返回的是当前节点的下一个节点的值
    return llist.curr->next->value;
}

int length(LList llist){
    return llist.count;
}

Edge create_Edge(int v, int w){
    Edge *e = (Edge *)malloc(sizeof(Edge));
    e->v = v;
    e->w = w;
    return *e;
}
int _vertex(Edge e){
    return e.v;
}
int _weight(Edge e){
    return e.w;
}