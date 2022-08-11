#include<stdlib.h>
#include<stdio.h>


// 可根据需要自定义数据类型
typedef struct{
    float coefficient;  // 系数
    float index;        // 指数
}DataType;

typedef struct{
    int maxSize;//最大元素个数
    int listSize;//当前元素个数
    int curr;//当前元素的位置
    DataType *listArray;//容纳顺序表元素
}AList;

AList create(int size);     //创建顺序表
void clear(AList *alist);   //清空顺序表的内容

void append(AList *alist, DataType value);      //在末尾添加元素
void insert(AList *alist, DataType value);      //插入一个元素
DataType delete(AList *alist);                  //删除并返回当前元素
void moveToStart(AList *alist);                 //当前元素的位置移到首位
void moveToEnd(AList *alist);                   //当前元素的位置移到末尾
void next(AList *alist);                        //当前元素向后移
void prev(AList *alist);                        //当前元素向前移
void moveToPos(AList *alist, int i);            //当前元素移到位置i
DataType getValue(AList alist);                 //获取当前元素的值
void traverse(AList alist);                     //遍历

AList add(AList p1, AList p2);                  //两个多项式相加

AList create(int size){
    AList *alist = (AList *)malloc(sizeof(AList));
    alist->maxSize = size;
    alist->listSize = 0;
    alist->curr = 0;    
    alist->listArray = (DataType *)malloc(alist->maxSize*sizeof(DataType));    
    return *alist;
}

void clear(AList *alist){
    free(alist->listArray);
    alist->listSize = 0;
    alist->curr = 0;
    alist->listArray = (DataType *)calloc(alist->maxSize, sizeof(DataType));
}

void append(AList *alist, DataType value){
    if(alist->listSize >= alist->maxSize){
        printf("%s", "list capacity exceeded");
        exit(0);
    }
    alist->listArray[alist->listSize] = value;
    alist->listSize++;   
}

void insert(AList *alist, DataType value){
    if(alist->listSize >= alist->maxSize){
        printf("%s", "list capacity exceeded");
        exit(0);
    }
    for(int i = alist->listSize; i >= alist->curr; i--){
        alist->listArray[i] = alist->listArray[i-1]; 
    }
    alist->listArray[alist->curr] = value;
    alist->listSize++;
}

DataType delete(AList *alist){
    if(alist->curr < 0 || alist->curr >= alist->listSize){
        printf("%s", "no element");
        exit(0);
    }
    DataType res = alist->listArray[alist->curr];
    for(int i = alist->curr; i < alist->listSize - 1; i++){
        alist->listArray[i] = alist->listArray[i+1];
    }
    alist->listSize--;
    return res;
}

void moveToStart(AList *alist){
    alist->curr = 0;
}

void moveToEnd(AList *alist){
    alist->curr = alist->listSize;
}

void next(AList *alist){
    if(alist->curr < alist->listSize){
        alist->curr++;
    }
}

void prev(AList *alist){
    if(alist->curr > 0){
        alist->curr--;
    }
}

void moveToPos(AList *alist, int i){
    if(i < 0 || i >= alist->listSize){
        printf("%s", "index out of range");
        exit(0);
    }
    alist->curr = i;
}

DataType getValue(AList alist){   
    // if(alist->curr < 0 || alist->curr > alist->listSize){
    //     printf("%s", "no current element");
    //     exit(0);
    // }
    return alist.listArray[alist.curr];
}

void traverse(AList alist){
    moveToStart(&alist);
    printf("coefficient \t index\n");
    for(moveToStart(&alist); alist.curr < alist.listSize; next(&alist)){
        printf("%f \t %f\n", getValue(alist).coefficient, getValue(alist).index);
    }
}

AList add(AList p1, AList p2){
    AList result = create(p1.listSize + p2.listSize);
    while(p1.curr < p1.listSize && p2.curr < p2.listSize){
        if(getValue(p1).index < getValue(p2).index){
            append(&result, getValue(p1));
            next(&p1);
        }
        else if(getValue(p1).index == getValue(p2).index){
            DataType temp = {getValue(p1).coefficient + getValue(p2).coefficient, getValue(p1).index};
            append(&result, temp);
            next(&p1);
            next(&p2);
        }
        else{
            append(&result, getValue(p2));
            next(&p2);
        }
    }
    while(p1.curr < p1.listSize){
        append(&result, getValue(p1));
        next(&p1);
    }
    while(p2.curr < p2.listSize){
        append(&result, getValue(p2));
        next(&p2);
    }
    return result;
}