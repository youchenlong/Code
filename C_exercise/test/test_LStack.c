#include"../DataStructure/LStack.h"

int main(){
    LStack s = create();
    for(int i = 0; i < 10; i++){
        push(&s, i);
        // printf("%d ", topValue(s));
    }
    while(s.top != NULL){
        printf("%d ", pop(&s));
    }
    return 0;
}