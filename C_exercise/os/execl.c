#include<unistd.h>

int main(){
    execl("/usr/bin/vim", "", NULL);
    return 0;
}