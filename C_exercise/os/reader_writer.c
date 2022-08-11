#include<pthread.h>
#include<stdio.h>
#include<unistd.h>  /*sleep*/

/*
读者作者问题--  
1、某一时刻，可以有多个读者进入临界区阅读（同步）
2、某一时刻，有且仅有一个作家能够进入临界区写作（同步）
3、某一时刻，当有作家在临界区内写作，读者不能进入临界区阅读（互斥）
4、某一时刻，当有读者在临界区内阅读，或有其他作家在临界区内写作，作家不能进入临界区写作（互斥）

缺点--同步问题和互斥问题都没有解决。
*/

void *writer(void *arg){
    while(1){
        /* critical section */
        printf("\t\t\t\twriting is performed......\n");
        sleep(1);
    }
}

void *reader(void *arg){
    while(1){      
        /* critical section */
        printf("reading is performed......\n");
        sleep(1);
    }
}

int main(){
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
    return 0;
}