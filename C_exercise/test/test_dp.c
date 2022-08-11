#include<stdio.h>
#include<malloc.h>
#include"../DataStructure/LList.h"


/*
    问题描述：有一个m*n的表格，起始位置在左上角，终止位置在右下角，每次只能向右或向下走一格。
            表格中每一格都有相应的价值，从起始位置到终止位置的每一条路径的价值为走过的格子价值之和。
            问：总共有多少条价值不同的路径，并给出每条路径的价值。
*/


#define M 3
#define N 3

int find(LList llist, int val){
    // 寻找链表中是否存在指定的值，存在返回true，不存在返回false
    for(moveToStart(&llist); llist.curr != llist.tail; next(&llist)){
        if(getValue(llist) == val){
            return 1;
        }
    }
    return 0;
}

int func(int a[][N]){

    int count[M][N];        // 记录种数
    LList length[M][N];     // 记录距离
    for(int i = 0; i < M; i++){
        for(int j = 0; j < N; j++){
            count[i][j] = 0;
            length[i][j] = create();
        }
    }
    // 初始化边界值
    for(int i = 0; i < M; i++){
        count[i][0] = 1;
        int len = 0;
        for(int k = 0; k <= i; k++){
            len = len + a[k][0];
        }
        append(&length[i][0], len);
    }
    for(int j = 0; j < N; j++){
        count[0][j] = 1;
        int len = 0;
        for(int k = 0; k <= j; k++){
            len = len + a[0][k];
        }
        append(&length[0][j], len);
    }
    // 开始填表
    for(int i = 1; i < M; i++){
        for(int j = 1; j < N; j++){
            // 上边一个位置
            for(moveToStart(&length[i-1][j]); length[i-1][j].curr != length[i-1][j].tail; next(&length[i-1][j])){
                if(!find(length[i][j], getValue(length[i-1][j]) + a[i][j])){
                    append(&length[i][j], getValue(length[i-1][j]) + a[i][j]);
                }
            }
            // 左边一个位置
            for(moveToStart(&length[i][j-1]); length[i][j-1].curr != length[i][j-1].tail; next(&length[i][j-1])){
                if(!find(length[i][j], getValue(length[i][j-1]) + a[i][j])){
                    append(&length[i][j], getValue(length[i][j-1]) + a[i][j]);
                }
            }
            count[i][j] = length[i][j].count;
        }
    }
    traverse(length[M - 1][N - 1]);
    printf("\n");
    return count[M - 1][N - 1];
}

int main(){
    int a[M][N] = {1, 3, 1, 1, 5, 1, 4, 2, 1};
    printf("%d", func(a));
    return 0;
}