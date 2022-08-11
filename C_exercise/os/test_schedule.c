#include"schedule.h"

int main(){
    process p[3];
    process_queue q = create();
    for(int i = 0; i < 3; i++){
        p[i] = create_process();
        append(&q, p[i]);
    }
    // FCFS(q);
    // nonpremptive_SJF(q);
    // premptive_SJF(q);
    // nonpremptive_PS(q);
    premptive_PS(q);
    // RR(q);
    return 0;
}