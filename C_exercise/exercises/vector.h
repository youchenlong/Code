#include<stdio.h>
#include<stdlib.h>
#include<math.h>

typedef struct{
    int dimension;
    float *array;
}vector;

void create(vector *v, int d);                          // 创建一个向量
void init_vector(vector *v);                            // 初始化向量
vector add(vector v1, vector v2);                       // 加法
vector sub(vector v1, vector v2);                       // 减法
vector scalar_mul(vector v, float f);                   // 数乘向量
float norm(vector v);                                   // 向量的模长(二范数)
float dot(vector v1, vector v2);                        // 向量内积
vector *Schmidt_orthogonalization(vector *v, int n);    // 施密特标准正交化


void create(vector *v, int d){
    v->dimension = d;
    v->array = (float *)malloc(sizeof(float)*d);
    for(int i = 0; i < v->dimension; i++){
        v->array[i] = 0;
    }
}

void init_vector(vector *v){
    printf("vector(%d)  input element:\n", v->dimension);
    for(int i = 0; i < v->dimension; i++){
        scanf("%f", &v->array[i]);
    }
}

vector add(vector v1, vector v2){
    if(v1.dimension != v2.dimension){
        printf("the dimension of the two vectors doesn't equal!");
        exit(0);
    }
    vector res;
    create(&res, v1.dimension);
    for(int i = 0; i < res.dimension; i++){
        res.array[i] = v1.array[i] + v2.array[i];
    }
    return res;
}

vector sub(vector v1, vector v2){
    if(v1.dimension != v2.dimension){
        printf("the dimension of the two vectors doesn't equal!");
        exit(0);
    }
    vector res;
    create(&res, v1.dimension);
    for(int i = 0; i < res.dimension; i++){
        res.array[i] = v1.array[i] - v2.array[i];
    }
    return res;
}

vector scalar_mul(vector v, float f){
    vector res;
    create(&res, v.dimension);
    for(int i = 0; i < res.dimension; i++){
        res.array[i] = v.array[i] * f;
    }
    return res;
}

float norm(vector v){
    float res = 0;
    for(int i = 0; i < v.dimension; i++){
        res += v.array[i] * v.array[i];
    }
    return sqrt(res);
}

float dot(vector v1, vector v2){
    if(v1.dimension != v2.dimension){
        printf("the dimension of the two vectors doesn't equal!");
        exit(0);
    }
    float res = 0;
    for(int i = 0; i < v1.dimension; i++){
        res += v1.array[i] * v2.array[i];
    }
    return res;
}

vector *Schmidt_orthogonalization(vector *v, int n){  
    // 向量组中的向量维数必须相同
    int dimension = v[0].dimension;
    for(int i = 0; i < n - 1; i++){
        if(v[i].dimension != dimension){
            printf("the dimension of the vector group doesn't equal!");
            exit(0);
        }
    }
    vector *res = (vector *)malloc(sizeof(vector) * n);
    for(int i = 0; i < n; i++){
        create(&res[i], dimension);
    }
    // 正交化
    for(int i = 0; i < n; i++){
        res[i] = v[i];
        for(int j = 0; j < i; j++){
            float lambda = dot(v[i], res[j]) / dot(res[j], res[j]);
            res[i] = sub(res[i], scalar_mul(res[j], lambda)); 
        }
    }
    // 标准化
    for(int i = 0; i < n; i++){
        res[i] = scalar_mul(res[i], 1 / norm(res[i]));
    }
    return res;
}

void print_vector(vector v){
    for(int i = 0; i < v.dimension; i++){
        printf("%f ", v.array[i]);
    }
    printf("\n");
}