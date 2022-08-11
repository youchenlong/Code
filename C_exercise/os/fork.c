#include<unistd.h>
#include<wait.h>
#include<stdio.h>
#include<stdlib.h>

int main(){
	int pid;
	pid = fork();
	if(pid<0){
		printf("fork failed\n");
		return 1;
	}
	else if(pid==0){
		if(execlp("/home/ubuntu/Desktop/os/child_process", "hahahah", NULL) == -1){
			printf("error\n");
		}
	}
	else{
		waitpid(pid, NULL, 0);
		printf("Child exited\n");
		exit(0);
	}
}

