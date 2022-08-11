#include<pthread.h>
#include<stdio.h>
#include<stdlib.h>

int sum;
void *runner(void *arg){
    sum = 0;
    for(int i = 1; i <= atoi(arg); i++){
        sum = sum + i;
    }
    pthread_exit(0);
    // return (void *)0;
}

int main(int argc, char *argv[]){
    pthread_t tid;
    pthread_attr_t attr;
    pthread_attr_init(&attr);
    pthread_create(&tid, &attr, runner, argv[1]);
    // pthread_create(&tid, 0, runner, argv[1]);
    pthread_join(tid, NULL);
    printf("%d\n", sum);
    return 0;
}