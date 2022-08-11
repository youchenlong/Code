#include<pthread.h>
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

/*
生产者消费者问题--
1、当缓冲区满时，生产者不能进入临界区生产（同步）
2、当缓冲区空时，消费者不能进入临界区消费（同步）
3、由于只考虑了一个生产者，一个消费者，互斥问题不存在

方法--声明一个长度为 n 的数组，但只能使用其中 n-1 个空间

缺点--
1、n个空间没有用完
2、忙等待
*/

#define BUFFER_SIZE 10
int buffer[BUFFER_SIZE];
int in = 0;
int out = 0;

void *producer(void *arg){
    while(1){
        while(((in + 1)%BUFFER_SIZE)==out){
            // 缓冲区已满
            printf("full\n");
            sleep(1);
        }
        int item = rand() % 10;
        buffer[in] = item;
        printf("producing an item %d......\n", item);
        in = (in + 1) % BUFFER_SIZE;
        sleep(1);
    }
}

void *consumer(void *arg){
    while(1){
        while(in == out){
            // 缓冲区为空
            printf("empty\n");
            sleep(1);
        }
        int item = buffer[out];
        printf("\t\t\t\tconsuming an item %d......\n", item);
        out = (out + 1) % BUFFER_SIZE;
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