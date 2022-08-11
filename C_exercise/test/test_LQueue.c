#include"../DataStructure/LQueue.h"

int main(){
    LQueue q = create();
    for(int i = 0; i < 10; i++){
        enqueue(&q, i);
    }
    printf("%d\n", frontValue(q));
    while(length(q) != 0){
        printf("%d ", dequeue(&q));
    }
    
    return 0;
}