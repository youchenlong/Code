#include<pthread.h>
#include<semaphore.h>
#include<stdio.h>
#include<unistd.h>  /*sleep*/

/*
方法--声明另一个信号量mutex，只允许一个读者进行P操作（sem_init)，同时保护共享变量read_count
*/

int read_count = 0;
sem_t rw_mutex;
sem_t mutex;

void *writer(void *arg){
    while(1){
        sem_wait(&rw_mutex);
        /* critical section */
        printf("\t\t\t\twriting is performed......\n");
        sem_post(&rw_mutex);
        sleep(1);
    }
}

void *reader(void *arg){
    while(1){
        sem_wait(&mutex);
        if(read_count == 0){
            sem_wait(&rw_mutex);
        }
        read_count++;
        sem_post(&mutex);
        /* critical section */
        printf("reading is performed......\n");
        sem_wait(&mutex);
        read_count--;
        if(read_count == 0){
            sem_post(&rw_mutex);
        }
        sem_post(&mutex);
        sleep(1);
    }
}

int main(){
    sem_init(&rw_mutex, 0, 1);
    sem_init(&mutex, 0, 1);
    pthread_t tid_writer[2], tid_reader[5];
    for(int i = 0; i < 2; i++){
        pthread_create(&tid_writer[i], NULL, writer, NULL);
    }
    for(int j = 0; j < 3; j++){
        pthread_create(&tid_reader[j], NULL, reader, NULL);
    }
    for(int i = 0; i < 2; i++){
        pthread_join(tid_writer[i], NULL);
    }
    for(int j = 0; j < 3; j++){
        pthread_join(tid_reader[j], NULL);
    }
    sem_destroy(&rw_mutex);
    sem_destroy(&mutex);
    return 0;
}