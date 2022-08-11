#include<stdlib.h>
#include<stdio.h>

void read(char *filename){
    FILE *fp;
    char ch;
    if((fp=fopen(filename, "r"))==NULL){
        printf("cannot open this file\n");
        exit(0);
    }
    while(!feof(fp)){
        ch = fgetc(fp);
        // do something
        // putchar(ch);
    }
    
    fclose(fp);
}