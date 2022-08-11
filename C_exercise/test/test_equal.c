#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int equal(int x, int y){
    if(!(x^y)){
        return 1;
    }
    return 0;
}

int main(){
    srand(time(0));
    int x = rand()%100;
    int y = rand()%100;
    printf("%d %d ", x, y);
    printf("%d", equal(x, y));
    return 0;
}