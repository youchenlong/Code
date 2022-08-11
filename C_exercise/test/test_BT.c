#include"../DataStructure/BinNode.h"

int main(){
    BinNode *root = create_BT(root);
    printf("\nInOrder:\t");
    InOrder(root);
    printf("\nPreOrder:\t");
    PreOrder(root);
    printf("\nPostOrder:\t");
    PostOrder(root);
    return 0;
}