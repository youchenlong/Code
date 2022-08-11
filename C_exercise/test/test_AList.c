#include<stdio.h>
#include"../DataStructure/AList.h"

int main(){
    AList alist = create(10);
    int array[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    for(int i = 0; i < 10; i++){
        append(&alist, array[i]);
    }
    moveToPos(&alist, 5);
    delete(&alist);
    traverse(alist);
    clear(&alist);    
    return 0;
}