#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int value;
    struct node *next;
}node;

typedef struct{
    node *head;         // 头节点
    node *tail;         // 尾节点
    node *curr;         // 当前节点(为了方便进行插入或删除操作，实际上操作的是当前节点的下一个节点)
    int count;          // 链表当前节点数(空节点除外)
}LList;

LList create();                                 // 创建链表
void clear(LList *llist);                       // 清空链表
void append(LList *llist, int value);           // 在链表末尾添加节点
void insert(LList *llist, int value);           // 在当前位置插入节点
int delete(LList *llist);                       // 在当前位置删除节点
int currPos(LList llist);                       // 获取当前位置
void moveToStart(LList *llist);                 // 移到表头
void moveToEnd(LList *llist);                   // 移到表位
void moveToPos(LList *llist, int pos);          // 移到指定位置(pos从0开始)
void next(LList *llist);                        // 当前位置向后移
int getValue(LList llist);                      // 获取当前节点的元素
int length(LList LList);                        // 获取链表长度
void traverse(LList llist);                     // 遍历链表


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

LList create(){  
    LList *llist = (LList *)malloc(sizeof(LList));
    init(llist);
    return *llist;
}

void clear(LList *llist){
    removeall(llist);
    init(llist);
}

void append(LList *llist, int value){
    node *n = (node *)malloc(sizeof(node));
    n->value = value;
    n->next = NULL;
    // 让链表尾节点指向它(注意指针与实际物理内存的联系，不然会产生疑惑)
    llist->tail->next = n;   
    llist->tail = llist->tail->next;
    llist->count++;
}

void insert(LList *llist, int value){
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

int delete(LList *llist){
    // getValue已经判断了是否为空的情况
    int value = getValue(*llist);
    node *temp = llist->curr->next;
    // 如果待删除的节点为尾节点，那么尾节点需要指向当前节点(因为尾节点不应该无处可指)
    if(llist->curr->next == llist->tail){
        llist->tail = llist->curr;
    }
    llist->curr->next = llist->curr->next->next;
    free(temp);
    llist->count--;
    return value;
}

int currPos(LList llist){
    node *temp = llist.head;
    int i;
    for(i = 0; temp != llist.curr; i++){
        temp = temp->next;
    }
    return i;
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

int getValue(LList llist){
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

void traverse(LList llist){
    for(moveToStart(&llist); llist.curr != llist.tail; next(&llist)){
        printf("%d ", getValue(llist));
    }
}