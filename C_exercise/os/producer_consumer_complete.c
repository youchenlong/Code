#include<pthread.h>
#include<semaphore.h>
#include<stdio.h>
#include<unistd.h>  /*sleep*/
#include<stdlib.h>  /*srand*/

/*
方法--信号量解决同步问题
*/

#define BUFFER_SIZE 10
int buffer[BUFFER_SIZE];    // 共享变量
int in = 0;
int out = 0;
sem_t empty, full, mutex;


void *producer(void *arg){
    while(1){
        int item = rand() % 10;
        sem_wait(&empty);
        sem_wait(&mutex);
        buffer[in] = item;
        printf("producing an item %d......\n", item);
        sem_post(&mutex);
        sem_post(&full);    
        in = (in + 1) % BUFFER_SIZE;
        
        sleep(1);
    }
}

void *consumer(void *arg){
    while(1){
        sem_wait(&full);
        sem_wait(&mutex);
        int item = buffer[out];
        printf("\t\t\t\tconsuming an item %d......\n", item);
        sem_post(&mutex);
        sem_post(&empty);
        out = (out + 1) % BUFFER_SIZE;
        sleep(1);
    }
}

int main(){
    sem_init(&empty, 0, BUFFER_SIZE);
    sem_init(&full, 0, 0);
    sem_init(&mutex, 0, 1);
    srand((unsigned)time(NULL));
    pthread_t tid_producer, tid_consumer;
    pthread_create(&tid_producer, 0, producer, NULL);
    pthread_create(&tid_consumer, 0, consumer, NULL);
    pthread_join(tid_producer, NULL);
    pthread_join(tid_consumer, NULL);
    sem_destroy(&empty);
    sem_destroy(&full);
    sem_destroy(&mutex);
    return 0;
}