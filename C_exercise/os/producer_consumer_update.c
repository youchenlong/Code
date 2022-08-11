#include<pthread.h>
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

/*
方法--用一个变量 counter 来计数

缺点--race
*/

#define BUFFER_SIZE 10
int buffer[BUFFER_SIZE];
int in = 0;
int out = 0;
int counter = 0;

void *producer(void *arg){
    while(1){
        while(counter == BUFFER_SIZE){
            // 缓冲区已满
            printf("full\n");
            sleep(1);
        }
        int item = rand() % 10;
        buffer[in] = item;
        printf("producing an item %d......\n", item);
        in = (in + 1) % BUFFER_SIZE;
        counter++;
        sleep(1);
    }
}

void *consumer(void *arg){
    while(1){
        while(counter == 0){
            // 缓冲区为空
            printf("empty\n");
            sleep(1);
        }
        int item = buffer[out];
        printf("\t\t\t\tconsuming an item %d......\n", item);
        out = (out + 1) % BUFFER_SIZE;
        counter--;    
        sleep(1);
    }
}

int main(){
    srand((unsigned)time(NULL));
    pthread_t tid_producer, tid_consumer;
    pthread_create(&tid_producer, 0, producer, NULL);
    pthread_create(&tid_consumer, 0, consumer, NULL);
    pthread_join(tid_producer, NULL);
    pthread_join(tid_consumer, NULL);
    return 0;
}