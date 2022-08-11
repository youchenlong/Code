#include"process_queue.h"

int timer = 0;     // 当前时间

void FCFS(process_queue q);                                 // First-Come-First-Served
void nonpremptive_SJF(process_queue q);                     // nonpremptive Shortest-Job-First
void premptive_SJF(process_queue q);                        // premptive Shortest-Job-First
void nonpremptive_PS(process_queue q);                      // nonpremptive Priority-Scheduling
void premptive_PS(process_queue q);                         // premptive Priority-Scheduling
void RR(process_queue q);                                   // Round-Robin

void FCFS(process_queue q){
    while(q.count > 0){
        // 选择方式--选择队列中第一个到达的进程，直到该进程执行结束
        process p = FCFS_POP(&q, timer);
        // 如果当前没有进程到达
        if(p.arrival_time > timer){
            timer++;
            printf("No process running......\n");
            insert(&q, p);
            continue;
        }
        while(p.remaining_execution_time > 0){
            // 某一时刻，只有一个进程处于运行状态，其他进程处于等待状态
            running_process(&p);
            waiting_queue(&q);
            timer++;
        }
    }
}

void nonpremptive_SJF(process_queue q){
    while(q.count > 0){
        // 选择方式--选择队列中剩余执行时间最短的进程
        process p = SJF_POP(&q, timer);
        if(p.arrival_time > timer){
            timer++;
            printf("No process running......\n");
            insert(&q, p);
            continue;
        }
        // 执行该进程直到结束
        while(p.remaining_execution_time > 0){
            // 某一时刻，只有一个进程处于运行状态，其他进程处于等待状态
            running_process(&p);
            waiting_queue(&q);
            timer++;
        }
    }
}

void premptive_SJF(process_queue q){
    while(q.count > 0){
        // 选择方式--选择队列中剩余执行时间最短的进程
        process p = SJF_POP(&q, timer);
        if(p.arrival_time > timer){
            timer++;
            printf("No process running......\n");
            insert(&q, p);
            continue;
        }
        // 执行该进程一个时间片
        running_process(&p);
        waiting_queue(&q);
        timer++;
        // 如果进程没有执行完成，返回到队列原位置
        if(p.remaining_execution_time > 0){
            insert(&q, p);
        }
    }
}

void nonpremptive_PS(process_queue q){
    while(q.count > 0){
        // 选择方式--选择队列中优先级最高的进程
        process p = PS_POP(&q, timer);
        if(p.arrival_time > timer){
            timer++;
            printf("No process running......\n");
            insert(&q, p);
            continue;
        }
        // 执行该进程直到结束
        while(p.remaining_execution_time > 0){
            // 某一时刻，只有一个进程处于运行状态，其他进程处于等待状态
            running_process(&p);
            waiting_queue(&q);
            timer++;
        }
    }
}

void premptive_PS(process_queue q){
    while(q.count > 0){
        // 选择方式--选择队列中优先级最高的进程
        process p = PS_POP(&q, timer);
        if(p.arrival_time > timer){
            timer++;
            printf("No process running......\n");
            insert(&q, p);
            continue;
        }
        // 执行该进程一个时间片
        running_process(&p);
        waiting_queue(&q);
        timer++;
        // 如果进程没有执行完成，返回到队列原位置
        if(p.remaining_execution_time > 0){
            insert(&q, p);
        }
    }
}

void RR(process_queue q){
    while(q.count > 0){
        // 选择方式--轮流执行队列中的进程(队列中第一个到达的进程)       
        process p = RR_POP(&q, timer);
        if(p.arrival_time > timer){
            timer++;
            printf("No process running......\n");
            insert(&q, p);
            continue;
        }
        // 执行该进程一个时间片
        running_process(&p);       
        waiting_queue(&q);
        timer++;
        // 如果进程没有执行完成，返回到队列末尾
        if(p.remaining_execution_time > 0){
            append(&q, p);
        }
    }
}