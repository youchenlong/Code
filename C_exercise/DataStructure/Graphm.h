#include<stdlib.h>
#include<stdio.h>

#define UNVISITED 0
#define VISITED 1   

typedef struct{
    int numVertex;          // 点数
    int numEdge;            // 边数
    int **matrix;           // 邻接矩阵
    int *mark;              // 标记点
}Graphm;

Graphm create_Graphm(int numVertex);                         // 创建图
int n(Graphm g);                                             // 获取点数
int e(Graphm g);                                             // 获取边数
int isVertex(Graphm g, int v);                               // 判断点v是否是图中的点(点从0开始)
int isEdge(Graphm g, int v1, int v2);                        // 判断v1->v2是否是图中的边
void setEdge(Graphm *g, int v1, int v2, int w);              // 创建边并初始化边的权重
void delEdge(Graphm *g, int v1, int v2);                     // 删除边
int getWeight(Graphm g, int v1, int v2);                     // 获取边的权重
void setMark(Graphm *g, int v, int val);                     // 设置点的值
int getMark(Graphm g, int v);                                // 获取点的值
int firstNeighbor(Graphm g, int v);                          // 返回v的第一个邻接点
int nextNeighbor(Graphm g, int v, int w);                    // 返回v的w之后的下一个邻接点


Graphm create_Graphm(int numVertex){
    Graphm *g = (Graphm *)malloc(sizeof(Graphm));
    g->numVertex = numVertex;
    g->numEdge = 0;
    g->mark = (int *)malloc(sizeof(int)*numVertex);
    g->matrix = (int **)malloc(sizeof(int *)*numVertex);
    for(int i = 0; i < numVertex; i++){
        g->matrix[i] = (int *)malloc(sizeof(int)*numVertex);
    }
    for(int i = 0; i < numVertex; i++){
        g->mark[i] = UNVISITED;
    }
    for(int i = 0; i < numVertex; i++){
        for(int j = 0; j < numVertex; j++){
            g->matrix[i][j] = 0;
        }
    }
    return *g;
}

int n(Graphm g){
    return g.numVertex;
}

int e(Graphm g){
    return g.numEdge;
}

int isVertex(Graphm g, int v){
    if(v >= n(g) || v < 0){
        return 0;
    }
    return 1;
}

int isEdge(Graphm g, int v1, int v2){
    if(!isVertex(g, v1) || !isVertex(g, v2)){
        printf("error! vertex doesn't exist\n");
        exit(0);
    }
    return g.matrix[v1][v2] != 0;
}

void setEdge(Graphm *g, int v1, int v2, int w){
    if(!isVertex(*g, v1) || !isVertex(*g, v2)){
        printf("error! vertex doesn't exist\n");
        exit(0);
    }
    if(w <= 0){
        printf("error! weight must be larger than 0\n");
        exit(0);
    }
    if(g->matrix[v1][v2] == 0){
        g->numEdge++;
    }
    g->matrix[v1][v2] = w;
}

void delEdge(Graphm *g, int v1, int v2){
    if(!isVertex(*g, v1) || !isVertex(*g, v2)){
        printf("error! vertex doesn't exist\n");
        exit(0);
    }
    if(g->matrix[v1][v2] != 0){
        g->numEdge--;
    }
    g->matrix[v1][v2] = 0;
}

int getWeight(Graphm g, int v1, int v2){
    if(!isVertex(g, v1) || !isVertex(g, v2)){
        printf("error! vertex doesn't exist\n");
        exit(0);
    }
    return g.matrix[v1][v2];
}

void setMark(Graphm *g, int v, int val){
    if(!isVertex(*g, v)){
        printf("error! vertex doesn't exist\n");
        exit(0);
    }
    g->mark[v] = val;
}

int getMark(Graphm g, int v){
    if(!isVertex(g, v)){
        printf("error! vertex doesn't exist\n");
        exit(0);
    }
    return g.mark[v];
}

int firstNeighbor(Graphm g, int v){
    if(!isVertex(g, v)){
        printf("error! vertex doesn't exist\n");
        exit(0);
    }
    for(int i = 0; i < g.numVertex; i++){
        if(g.matrix[v][i] != 0){
            return i;
        }
    }
    // 如果点v没有邻接点
    return g.numVertex;
}

int nextNeighbor(Graphm g, int v, int w){
    if(!isVertex(g, v) || !isVertex(g, w)){
        printf("error! vertex doesn't exist\n");
        exit(0);
    }
    for(int i = w + 1; i < g.numVertex; i++){
        if(g.matrix[v][i] != 0){
            return i;
        }
    }
    // 如果点v没有邻接点
    return g.numVertex;
}