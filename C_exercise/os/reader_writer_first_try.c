#include<pthread.h>
#include<semaphore.h>
#include<stdio.h>
#include<unistd.h>  /*sleep*/

/*
方法--声明一个信号量rw_mutex解决同步问题和互斥问题

缺点--
1、读者的同步问题没有完全解决
考虑以下情形：
作者进入临界区写作，此时，有大批读者在等待进入临界区（卡在sem_wait处）。
当作者退出临界区时，卡在临界区外的读者（不考虑新来的读者）只有一个能够进入临界区，违背同步。
2、引入了另一个共享变量read_count，但没有进行保护

分析错误原因--允许多个读者执行执行P操作(sem_init)，实际上只需要第一个读者执行P操作
*/

int read_count = 0;
sem_t rw_mutex;

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
        if(read_count == 0){
            sem_wait(&rw_mutex);
        }
        read_count++;
        /* critical section */
        printf("reading is performed......\n");
        read_count--;
        if(read_count == 0){
            sem_post(&rw_mutex);
        }
        sleep(1);
    }
}

int main(){
    sem_init(&rw_mutex, 0, 1);
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
    return 0;
}