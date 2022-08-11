#include<unistd.h>
#include<stdio.h>
#include<stdlib.h>

#define NZERO 20
#define PRI_USER_MAX 127
#define PRI_USER_MIN 0

typedef struct{
    int pid;                                // 进程号
    int arrival_time;                       // 到达时间
    int remaining_execution_time;           // 剩余执行时间
    int execution_time;                     // 已经执行时间
    int waiting_time;                       // 已经等待时间
    int nice;                               // 静态优先级(数值越低，优先级越高)
    int priority;                           // 动态优先级(数值越高，优先级越高)
}process;

process create_process();                           // 创建一个进程
void setpriority(process *p, int prio);             // 设置静态优先级(-NZERO, NZERO - 1)
int getpriority(process *p);                        // 获取静态优先级
void running_process(process *p);                   // 运行一个时间片
void waiting_process(process *p);                   // 等待一个时间片

process create_process(){
    printf("creating a process....\n");
    process p;
    printf("input pid of process: ");
    scanf("%d", &p.pid);
    printf("input arrival time of the process: ");
    scanf("%d", &p.arrival_time);
    printf("input remaining execution time of the process: ");
    scanf("%d", &p.remaining_execution_time);
    if(p.remaining_execution_time <= 0){
        printf("create process error! Remaining execution time <= 0");
        exit(-1);
    }
    p.execution_time = 0;
    p.waiting_time = 0;
    printf("input priority of the process: ");
    int prio;
    scanf("%d", &prio);
    setpriority(&p, prio);
    p.priority = PRI_USER_MAX - p.execution_time / 4 - p.nice * 2;
    return p;
}

void setpriority(process *p, int prio){
    if(prio < 0 || prio >= 2*NZERO){
        printf("setpriority error!");
        exit(0);
    }
    p->nice = prio - NZERO;
}

int getpriority(process *p){
    return p->nice + NZERO;
}

void running_process(process *p){
    printf("running process %d......\n", p->pid);
    // 更新剩余执行时间和已经执行时间，和动态优先级
    // sleep(1);
    p->remaining_execution_time--;
    p->execution_time++;
    p->priority = PRI_USER_MAX - p->execution_time / 4 - p->nice * 2;
}

void waiting_process(process *p){
    // 更新等待时间
    // sleep(1);
    p->waiting_time++;
}