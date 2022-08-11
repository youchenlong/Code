#include<unistd.h>
#include<wait.h>
#include<stdlib.h>
#include<stdio.h>

#define READ_END 0
#define WRITE_END 1

int main(){
    int fd[2];
    pid_t pid;
    char buf;
    if(pipe(fd)==-1){
        perror("pipe");
        exit(-1);
    } 
    if((pid=fork())<0){
        perror("fork");
        exit(-1);
    }
    if(pid==0){
        close(fd[WRITE_END]);
        while(read(fd[READ_END], &buf, 1)>0){
            // sleep(1);
            write(STDOUT_FILENO, &buf, 1);
        }
        close(fd[READ_END]);
        exit(0);
    }
    else{
        close(fd[READ_END]);
        write(fd[1], "Hello, child\n", 13);
        close(fd[WRITE_END]);
        waitpid(pid, NULL, 0);
        exit(0);
    }
}