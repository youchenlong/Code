#include<stdio.h>
#include<malloc.h>

#define END -1
#define size 100

typedef char valueType;

typedef struct BinNode{
    int key;
    valueType value[size];
    struct BinNode *lchild;
    struct BinNode *rchild;
}BinNode;

BinNode *init_value(BinNode *n){
    printf("input value of BinNode:");
    scanf("%s", &n->value);
    return n;
}

void print_value(BinNode *n){
    printf("%s\t", n->value);
}

BinNode *create_BT(BinNode *root){
    // 初始化节点
    int key;
    printf("input key of BinNode:");
    scanf("%d", &key);
    if(key == END){
        return NULL;
    }
    root = (BinNode *)malloc(sizeof(BinNode));
    root->key = key;
    root = init_value(root);
    // 递归处理子节点，注意递归的顺序
    root->lchild = create_BT(root->lchild);
    root->rchild = create_BT(root->rchild);
    return root;
}

void InOrder(BinNode *root){
    if(root == NULL){
        return;
    }
    InOrder(root->lchild);
    print_value(root);
    InOrder(root->rchild);
}

void PreOrder(BinNode *root){
    if(root == NULL){
        return;
    }
    print_value(root);
    PreOrder(root->lchild);
    PreOrder(root->rchild);
}

void PostOrder(BinNode *root){
    if(root == NULL){
        return;
    }
    PostOrder(root->lchild);
    PostOrder(root->rchild);
    print_value(root);
}