#include<sys/types.h>
#include<unistd.h>
#include<stdio.h>
#include<wait.h>

int main(){
    /* method1
    for(int i = 0; i < 3; i++){
        // each process will run following code when created
        int pid = fork();
        printf("%d\n", pid);
        wait(NULL);
    }
    */
    /* method2
    for(int i = 0; i < 3; i++){
        fork();
    }
    // each process will run following code when terminated
    printf("hello world\n");
    wait(NULL);
    */
    return 0;    
}