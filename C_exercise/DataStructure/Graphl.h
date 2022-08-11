#include"LList_Graphl.h"
#include<stdlib.h>
#include<stdio.h>

#define UNVISITED 0
#define VISITED 1

typedef struct{
    int numVertex;              // 点数
    int numEdge;                // 边数
    LList **vertex;             // 邻接矩阵
    int *mark;                  // 标记点
}Graphl;

Graphl create_Graphl(int numVertex);                         // 创建图
int n(Graphl g);                                             // 获取点数
int e(Graphl g);                                             // 获取边数
int isVertex(Graphl g, int v);                               // 判断点v是否是图中的点(点从0开始)
int isEdge(Graphl g, int v1, int v2);                        // 判断v1->v2是否是图中的边
void setEdge(Graphl *g, int v1, int v2, int w);              // 创建边并初始化边的权重
void delEdge(Graphl *g, int v1, int v2);                     // 删除边
int getWeight(Graphl g, int v1, int v2);                     // 获取边的权重
void setMark(Graphl *g, int v, int val);                     // 设置点的值
int getMark(Graphl g, int v);                                // 获取点的值
int firstNeighbor(Graphl g, int v);                          // 返回v的第一个邻接点
int nextNeighbor(Graphl g, int v, int w);                    // 返回v的w之后的下一个邻接点


Graphl create_Graphl(int numVertex){
    Graphl *g = (Graphl *)malloc(sizeof(Graphl));
    g->numVertex = numVertex;
    g->numEdge = 0;
    g->mark = (int *)malloc(sizeof(int)*numVertex);
    g->vertex = (LList **)malloc(sizeof(LList *)*numVertex);
    for(int i = 0; i < numVertex; i++){
        g->vertex[i] = (LList *)malloc(sizeof(LList));
    }
    for(int i = 0; i < numVertex; i++){
        g->mark[i] = UNVISITED;
    }
    for(int i = 0; i < numVertex; i++){
        *g->vertex[i] = create_LList();
    }
    return *g;
}

int n(Graphl g){
    return g.numVertex;
}

int e(Graphl g){
    return g.numEdge;
}

int isVertex(Graphl g, int v){
    if(v >= n(g) || v < 0){
        return 0;
    }
    return 1;
}

int isEdge(Graphl g, int v1, int v2){
    if(!isVertex(g, v1) || !isVertex(g, v2)){
        printf("error! vertex doesn't exist\n");
        exit(0);
    }
    // 注意，在判断v1->v2是否是图中的边时，改变了链表的当前位置
    for(moveToStart(g.vertex[v1]); currPos(*g.vertex[v1]) < length(*g.vertex[v1]); next(g.vertex[v1])){
        Edge temp = getValue(*g.vertex[v1]);
        if(_vertex(temp) == v2){
            return 1;
        }
    }
    return 0;
}

void setEdge(Graphl *g, int v1, int v2, int w){
    if(!isVertex(*g, v1) || !isVertex(*g, v2)){
        printf("error! vertex doesn't exist\n");
        exit(0);
    }
    // 边的权重必须大于0
    if(w <= 0){
        printf("error! weight must be larger than 0\n");
        exit(0);
    }
    Edge currEdge = create_Edge(v2, w);
    // 如果v1->v2存在
    if(isEdge(*g, v1, v2)){
        delete(g->vertex[v1]);
        insert(g->vertex[v1], currEdge);
    }
    // 如果v1->v2不存在
    else{
        g->numEdge++;
        for(moveToStart(g->vertex[v1]); currPos(*g->vertex[v1]) < length(*g->vertex[v1]); next(g->vertex[v1])){
            Edge temp = getValue(*g->vertex[v1]);
            if(_vertex(temp) > v2){
                break;
            }
        }
        insert(g->vertex[v1], currEdge);
    }
}

void delEdge(Graphl *g, int v1, int v2){
    if(isEdge(*g, v1, v2)){
        delete(g->vertex[v1]);
        g->numEdge--;
    }
}

int getWeight(Graphl g, int v1, int v2){
    if(isEdge(g, v1, v2)){
        Edge temp = getValue(*g.vertex[v1]);
        return _weight(temp);
    }
    // 如果边v1->v2不存在
    return 0;
}

void setMark(Graphl *g, int v, int val){
    if(!isVertex(*g, v)){
        printf("error! vertex doesn't exist\n");
        exit(0);
    }
    g->mark[v] = val;
}

int getMark(Graphl g, int v){
    if(!isVertex(g, v)){
        printf("error! vertex doesn't exist\n");
        exit(0);
    }
    return g.mark[v];
}

int firstNeighbor(Graphl g, int v){
    if(!isVertex(g, v)){
        printf("error! vertex doesn't exist\n");
        exit(0);
    }
    // 如果v没有邻接点
    if(length(*g.vertex[v]) == 0){
        return n(g);
    }
    moveToStart(g.vertex[v]);
    Edge temp = getValue(*g.vertex[v]);
    return _vertex(temp);
}

int nextNeighbor(Graphl g, int v, int w){
    if(isEdge(g, v, w)){
        if(currPos(*g.vertex[v]) + 1 < length(*g.vertex[v])){
            next(g.vertex[v]);
            Edge temp = getValue(*g.vertex[v]);
            return _vertex(temp);
        }
    }
    // 如果w后面没有邻接点，或者w不是v的邻接点
    return n(g);
}