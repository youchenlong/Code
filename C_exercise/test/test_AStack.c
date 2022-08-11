#include"../DataStructure/AStack.h"

int main(){
    AStack s = create(10);
    for(int i = 0; i < 10; i++){
        push(&s, i);
    }
    while(s.top != s.size){
        printf("%d ", pop(&s));
    }
    return 0;
}