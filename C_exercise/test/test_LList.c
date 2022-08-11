#include"../DataStructure/LList.h"

int main(){
    LList llist = create();
    for(int i = 0; i < 10; i++){
        append(&llist, i);
    }
    // traverse(llist);

    // remove(&llist);
    // moveToPos(&llist, 4);
    // printf("%d ", getValue(llist));

    // moveToPos(&llist, 3);
    // printf("currPos=%d\n", currPos(llist));

    return 0;
}