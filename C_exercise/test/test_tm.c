#include<stdio.h>
#include<time.h>

int main(){
    time_t t = time(0);
    struct tm *p = localtime(&t);
    printf("%d\n", p->tm_year+1900);
    printf("%d\n", p->tm_mon+1);
    printf("%d\n", p->tm_mday);
    printf("%d\n", p->tm_hour);
    printf("%d\n", p->tm_min);
    printf("%d\n", p->tm_sec);
    printf("%d\n", p->tm_wday);
    return 0;
}